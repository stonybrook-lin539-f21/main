#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import *
import re
from shutil import copy2
import subprocess as sp

# set some subfolder names
source = Path("source")
build = Path("build")
notebooks = Path("notebooks")
pdf = Path("pdf")
includes = Path("includes")

# generator for all standalone tikz files
tikz_exts = (".tikz", ".forest")
tikz = (f for f in source.glob('**/*') if f.suffix in tikz_exts)

# generator for all mdown files
mdown_exts = (".mdown", ".md")
mdown = (f for f in source.glob('**/*') if f.suffix in mdown_exts)

# list of all styling files (list because generator can only be processed once)
style_exts = (".css")
styles = [f for f in includes.glob('**/*') if f.suffix in style_exts]


def change_subfolder(path: Path, subfolder: Path,
                     with_file: bool = False) -> Path:
    """
    Prepend path with a subfolder.

    This is a helper function for replicating the path to some file F inside
    some subfolder A in another subfolder B. It takes the path to F, excluding
    A, and prepends B. F is also omitted by default.

    Parameters
    ----------
    path: Path
        path to be recreated
    subfolder: Path
        folder under which the path is to be created
    with_file: bool
        whether the output path should include the file
    """
    return subfolder / Path(*path.parts[1:]) if with_file\
        else subfolder / Path(*path.parts[1:-1])


def mirror_subfolders(path: Path, subfolder: Path) -> None:
    """Replicate a folder hiearchy inside another folder."""
    change_subfolder(path, subfolder).mkdir(
        mode=0o755, parents=True, exist_ok=True)


def create_mycommands(f: Path, build_dir: Path) -> None:
    """
    Convert mycommands.mdown to .sty file.

    This function produces a sty file where line-initial and line-final $ have
    been stripped out. The file is saved in the specified build directory.

    Parameters
    ----------
    f: Path
        path to mdown file
    build_dir: Path
        path to the build directory
    """
    with f.open("r") as mdown:
        clean = [re.sub(r"(^\$)|(\$\n)", "", line)
                 for line in mdown.readlines()]
        stypath = build_dir / Path(f.name).with_suffix(".sty")
        with stypath.open("w") as styfile:
            styfile.write("\n".join(clean))


def process_tikzfile(f: Path, mycommands: Path = Path(
                        "./includes/mycommands.mdown")) -> None:
    """
    Convert tikz file to svg image.

    This requires latexmk and pdf2svg to be installed and available in the
    user's PATH.
    """
    for folder in [build, notebooks]:
        mirror_subfolders(f, folder)

    # where to save pdf, relative path
    pdf = change_subfolder(f, build, with_file=True).with_suffix('.pdf')
    # where to save svg, relative path
    svg = change_subfolder(f, notebooks, with_file=True).with_suffix('.svg')

    # create mycommands in build folder
    build_dir = pdf.parent
    create_mycommands(mycommands, build_dir)

    # use sp.call so that latexmk gets to finish before we call pdf2svg
    sp.call(["latexmk", "-pdf", "-quiet", str(f.absolute())],
            cwd=str(pdf.parent),  # put compilation files in same subfolder
            stdout=sp.DEVNULL)    # and don't print output to shell
    sp.Popen(["pdf2svg", str(pdf), str(svg)],
             stdout=sp.DEVNULL)


def load_template(file_list: List[str], folder: Path = includes) -> str:
    """Read in boilerplate text from mdown file."""
    text = "\n"
    for f in file_list:
        path = folder / Path(f + '.mdown')
        with path.open("r") as template:
            text += template.read()
            text += "\n"
    return text


def header_preprocess(line: str) -> str:
    """
    Rewrite some parts of header files.

    Right now this only removes ensuremath commands, which aren't understood by
    MathJax.
    """
    return re.sub(r"\\ensuremath{([^}]*)}", r"\1", line)


def regexes(line: str, target: str="ipynb") -> str:
    """Modify code for processing with notedown or Latex."""
    if target == "ipynb":
        # replace input tikz/forest by image link to svg, with size as alt text
        line = re.sub(r"\\input_(.*?){(.*?).(tikz|forest)}",
                      r"![\1](\2.svg)", line)
        # replace math environments by div containers
        line = re.sub(r"\\begin{(definition|theorem|lemma|proof|example|remark|advice|exercise)}",
                      r"<div class=\1>", line)
        line = re.sub(r"\\end{(definition|theorem|lemma|proof|example|remark|advice|exercise)}",
                      r"</div>", line)
        # wrap math environments between $$
        line = re.sub(r"(\\begin{(multline|array)\*?})",
                      r"$$\1", line)
        line = re.sub(r"(\\end{(multline|array)\*?})",
                      r"\1$$", line)
        # replace --- by - in markdown
        line = re.sub(r" --- ", " - ", line)
    if target == "latex":
        # remove underscore from \input_{small,mid,large};
        # this is needed to avoid Latex complaints
        line = re.sub(r"\\input_.*?{(.*?)}",
                      r"\\begin{center}\\input{\1}\\end{center}", line)
        # replace <li>xyz</li> by \item xyz
        line = re.sub(r"<li>(.*?)</li>", r"\\item \1", line)
        # replace <ul> and </ul> by itemize
        line = re.sub(r"<ul>", r"\\begin{itemize}", line)
        line = re.sub(r"</ul>", r"\\end{itemize}", line)
        # replace <ol> and </ol> by enumerate
        line = re.sub(r"<ol>", r"\\begin{enumerate}", line)
        line = re.sub(r"</ol>", r"\\end{enumerate}", line)
    return line


def mdown2ipynb(f: Path,
                header: List[str]=[],
                footer: List[str]=[],
                copy_css: bool=False) -> None:
    """
    Convert markdown file to Jupyter notebook.

    This requires notedown to be installed and available in the user's PATH.
    The markdown file is concatenated with specified header and footer files,
    preprocessed by regexes, and then fed into notedown.

    The notebook is created in the folder indicated by the notebooks variable,
    replicating the same folder hierarchy as in the source directory: if
    markdown file F is found at source/A/B/C/F, then the corresponding notebook
    file N is at notebook/A/B/C/N.

    Parameters
    ----------
    f: Path
        path to file
    header:
        list of header snippets to prepend
    footer:
        list of footer snippets to append
    copy_css:
        whether css files should be copied into each notebook folder
    """
    with f.open("r") as text:
        for folder in [build, notebooks]:
            mirror_subfolders(f, folder)
        preproc_path = change_subfolder(f, build, with_file=True)
        preproc = open(str(preproc_path), "w")
        # add header
        if header:
            preproc.write(header_preprocess(load_template(header)))

        # replace latex by html or markdown
        for line in text:
            preproc.write(regexes(line, target="ipynb"))

        # add footer
        if footer:
            preproc.write(load_template(footer))

        # clean-up
        preproc.close()

        # run conversion
        target = change_subfolder(
            f, notebooks, with_file=True).with_suffix('.ipynb')
        # we use sp.call so that notedown finishes before nbconvert starts
        sp.call(["notedown",
                 str(preproc_path),
                 "--match=fenced",
                 '-o', str(target)],
                stdout=sp.DEVNULL)

        # copy stylesheets to notebook folder
        if copy_css:
            for style in styles:
                copy2(str(style), str(target.parent))

        # execute all cells
        sp.Popen(["jupyter", "nbconvert",
                  "--to", "notebook",
                  "--inplace",
                  "--execute",
                  "--allow-errors",
                  str(target)],
                 stdout=sp.DEVNULL)


def mdown2pdf(f: Path,
              yaml: Path,
              header: Path,
              footer: List[str] = [],
              mycommands: Path = Path("./includes/mycommands.mdown")) -> None:
    """
    Convert markdown file to pdf.

    This requires Latex and pandoc to be installed and available in the user's
    PATH. The markdown file is concatenated with specified footer files,
    preprocessed by regexes, and then fed into pandoc using the supplied header
    and yaml.

    The notebook is created in the folder indicated by the notebooks variable,
    replicating the same folder hierarchy as in the source directory: if
    markdown file F is found at source/A/B/C/F, then the corresponding notebook
    file N is at notebook/A/B/C/N.

    Parameters
    ----------
    f: Path
        path to file
    yaml: Path
        yaml file with layout information for pandoc
    header: Path
        Latex header to be prepended by pandoc
    footer: List[str]
        list of footer snippets to append
    """
    with f.open("r") as text:
        for folder in [build, pdf]:
            mirror_subfolders(f, folder)
        preproc_path = change_subfolder(f, build, with_file=True)
        preproc = open(str(preproc_path), "w")

        # replace html by Latex
        for line in text:
            preproc.write(regexes(line, target="latex"))

        # add footer
        if footer:
            preproc.write(load_template(footer))

        # clean-up
        preproc.close()

        # create mycommands.sty in build folder
        create_mycommands(mycommands, build)
        mycommands = change_subfolder(
            mycommands, build, with_file=True).with_suffix('.sty')

        # run conversion
        target = change_subfolder(
            f, pdf, with_file=True).with_suffix('.pdf')
        # we use sp.Popen for asynchronous processing
        sp.Popen(["pandoc",
                  "--verbose",
                  "--latex-engine=xelatex",
                  "-H", str(header.absolute()),
                  "-H", str(mycommands.absolute()),
                  str(yaml.absolute()),
                  str(preproc_path.absolute()),
                  "-o", str(target.absolute())],
                 stdout=sp.DEVNULL,
                 cwd=str(f.parent))


# time for the actual processing
for f in tikz:
    process_tikzfile(f)

for f in mdown:
    mdown2ipynb(f, header=['mycommands'])
#     mdown2pdf(f,
#               yaml= includes / Path("format.yaml"),
#               header= includes / Path("header.tex"))

# todo:
    # [ ] separate build directories for latex and notedown
    # [ ] more elegant path handling
    # [ ] commmand line parameters
    # [ ] documentation
    # [ ] easy way of processing only one file with sane defaults for file structure
    # [ ] absolute paths for robustness
    # [ ] dependency management

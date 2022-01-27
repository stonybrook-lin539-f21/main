"""
Doit task definition file for LIN 539 course notes.
"""

from pathlib import Path
from itertools import chain

DOIT_CONFIG = {"default_tasks": ["pdf_chaps", "html_chaps"]}
# DOIT_CONFIG = {"action_string_formatting": "new"}

TIKZ2SVG = "scripts/tikz2svg.sh"

LATEX_TEMPLATE = "templates/custom.tex"

CSTM_BLKS = "filters/custom-blocks.lua"
INCL_FILE = "filters/include-file.lua"
LATEX_TIPA = "filters/latex-tipa.lua"
STRIP_CODE = "filters/remove_code.lua"
EDGEMARKERS = "filters/edgemarkers.lua"

MYCOMMANDS = Path("includes/mycommands.mdown")
LATEX_PREAMBLE = Path("includes/preamble.tex")
YAMLHEADER = Path("includes/format.yaml")
WEBCSS = Path("includes/web-custom.css").resolve()  # must be absolute to load locally
MATHJAXCALL = Path("includes/include-mathjax.html")

SRCDIR = Path("source")
MD_EXTS = (".mdown", ".md")
SRC_MD = sorted(f for f in SRCDIR.glob('**/*') if f.suffix in MD_EXTS)
TIKZ_EXTS = (".tikz", ".forest")
SRC_TIKZ = sorted(f for f in SRCDIR.glob('**/*') if f.suffix in TIKZ_EXTS)

BUILDDIR = Path("build")
IMGDIR = BUILDDIR / "images"
TEXDIR = BUILDDIR / "latex"
PDFDIR = BUILDDIR / "pdf"
HTMLDIR = BUILDDIR / "html"
MODCMDS = BUILDDIR / "mycommands-preproc.mdown"

LATEX_DEPS = [CSTM_BLKS, INCL_FILE, LATEX_TIPA, EDGEMARKERS,
              LATEX_TEMPLATE, YAMLHEADER, LATEX_PREAMBLE, MODCMDS]
HTML_DEPS = [CSTM_BLKS, INCL_FILE,
             WEBCSS, MATHJAXCALL, MODCMDS]

# options shared by all Pandoc commands
PANDOC_OPTS = (
    "-s -f markdown-implicit_figures"
    " -V showanswers"
    f" -L {CSTM_BLKS} -L {INCL_FILE}")

# options for LaTeX/PDF only
LATEX_OPTS = (
    f"--template {LATEX_TEMPLATE}"
    f" --metadata-file={YAMLHEADER}"
    f" -H {LATEX_PREAMBLE} -H {MODCMDS}"
    f" -L {LATEX_TIPA}"
    f" -L {EDGEMARKERS}")

# options for HTML only
HTML_OPTS = (
    f"--shift-heading-level-by=1 -c {WEBCSS}"
    f" --mathjax -Vmath='' -H {MATHJAXCALL}"
    f" {MODCMDS}")

# source directories
BOOK_CHAPS = ["01_intro", "02_n-grams", "03_universals", "04_representations",
              "05_automata"]
BOOK_CHAPS += [f"background/{subch}" for subch in
               ["algebra", "functions", "general", "graphs", "logic", "multisets",
                "posets", "relations", "sets", "strings", "tuples"]]
# BOOK_CHAPS += ["solutions/01_intro", "solutions/02_n-grams", "solutions/03_universals", "solutions/04_representations",
#               "solutions/05_automata"]
# BOOK_CHAPS += [f"solutions/background/{subch}" for subch in
#                ["functions", "general", "graphs", "logic", "multisets",
#                 "posets", "relations", "sets", "strings", "tuples"]]


def task_modcommands():
    """
    Preprocess custom command file for PDF (LaTeX) and HTML conversion.

    At present, simply removes surrounding $ signs, which are needed
    for Jupyter only, and commented lines, which interfere with non-LaTeX
    build paths.
    """
    return {
        "targets": [MODCMDS],
        "file_dep": [MYCOMMANDS],
        "actions": [
            f"mkdir -p $(dirname {MODCMDS})",
            ("sed -e 's/\\(^\\$\\|\\$$\\)//g' -e '/^%%/d'"
             f" {MYCOMMANDS} > {MODCMDS}")],
            "clean": True}


def task_latex_book():
    """
    Build entire book as LaTeX. Intended mainly for debugging.
    """
    srcsubdirs = [SRCDIR / ch for ch in BOOK_CHAPS]
    infiles = sorted(str(f)
                     for f in chain.from_iterable(subdir.glob("*.md")
                                                  for subdir in srcsubdirs))
    outfile = f"{PDFDIR}/full-book.tex"
    cmd = (
        f"TEXINPUTS=.:{':'.join(str(sd) for sd in srcsubdirs)}:"
        f" pandoc -s -t latex --toc {PANDOC_OPTS} {LATEX_OPTS}"
        f" {' '.join(infiles)} -o {outfile}"
    )
    return {
        "targets": [outfile],
        "file_dep": [*infiles, *LATEX_DEPS],
        "actions": [f"mkdir -p $(dirname {outfile})", cmd],
        "clean": True}


def task_pdf_book():
    """
    Build entire book as PDF.

    If intermediate LaTeX is needed, use "latex_all" instead.
    """
    srcsubdirs = [SRCDIR / ch for ch in BOOK_CHAPS]
    infiles = sorted(str(f)
                     for f in chain.from_iterable(subdir.glob("*.md")
                                                  for subdir in srcsubdirs))
    outfile = f"{PDFDIR}/full-book.pdf"
    cmd = (
        f"TEXINPUTS=.:{':'.join(str(sd) for sd in srcsubdirs)}:"
        f" pandoc -s -t pdf --toc {PANDOC_OPTS} {LATEX_OPTS}"
        f" {' '.join(infiles)} -o {outfile}"
    )
    return {
        "targets": [outfile],
        "file_dep": [*infiles, *LATEX_DEPS],
        "actions": [f"mkdir -p $(dirname {outfile})", cmd],
        "clean": True}


def task_latex_chaps():
    """
    Build LaTeX standalone chapters. Intended mainly for debugging.
    """
    for ch in BOOK_CHAPS:
        infiles = [str(f)
                   for f in sorted(Path(f"{SRCDIR}/{ch}").glob("*.md"))]
        outfile = f"{TEXDIR}/{ch}.tex"
        cmd = (
            f"pandoc -t latex {PANDOC_OPTS} {LATEX_OPTS}"
            f" {' '.join(infiles)} -o {outfile}"
        )
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": [*infiles, *LATEX_DEPS],
            "actions": [f"mkdir -p $(dirname {outfile})", cmd],
            "clean": True}


def task_pdf_chaps(single_chapter=False):
    """
    Build PDF chapters directly from source using Pandoc.

    If intermediate LaTeX is needed, use "latex_chaps" instead.
    """
    for ch in BOOK_CHAPS:
        srcsubdir = SRCDIR / ch
        infiles = [str(f)
                   for f in sorted(Path(f"{SRCDIR}/{ch}").glob("*.md"))]
        if single_chapter:
            infiles = [' '.join(infiles)]
        for infile in infiles:
            if single_chapter:
                outfile = f"{PDFDIR}/{ch}.pdf"
            else:
                infile_name = Path(infile).stem
                outfile = f"{PDFDIR}/{ch}/{infile_name}.pdf"
            cmd = (
                f"TEXINPUTS=.:{srcsubdir}:"
                f" pandoc -s -t pdf {PANDOC_OPTS} {LATEX_OPTS}"
                f" {infile} -o {outfile}"
            )
            yield {
                "name": outfile,
                "targets": [outfile],
                "file_dep": [*infiles, *LATEX_DEPS],
                "actions": [f"mkdir -p $(dirname {outfile})", cmd],
                "clean": True}


def task_html_chaps():
    """
    Build HTML chapters using Pandoc.

    MODCMDS is inserted in the HTML body so that Pandoc will correctly add
    MATHJAX delimiters (it will not change included headers).

    There is a problem with the --mathjax command, which performs
    preprocessing, then inserts the Mathjax script *only if* LaTeX math is
    detected. This means that in a file with no math, the custom commands that
    we insert will appear as raw text. The author of Pandoc has refused to
    change this. As a workaround, we use -Vmath='' to manually clear the
    internal variable where Pandoc records whether math was detected, and
    insert the script ourselves.
    """
    for ch in BOOK_CHAPS:
        infiles = sorted(str(f)
                         for f in Path(f"{SRCDIR}/{ch}").glob("*.md"))
        incl_images = sorted(HTMLDIR / img.relative_to(SRCDIR).with_suffix(".svg")
                             for img in SRC_TIKZ)
        outfile = Path(f"{HTMLDIR}/{ch}/index.html")
        cmd = (
            f"pandoc -t html {PANDOC_OPTS} {HTML_OPTS}"
            f" --metadata title={ch}"
            f" {' '.join(infiles)} -o {outfile}"
        )
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": [*infiles, *incl_images, *HTML_DEPS],
            "actions": [f"mkdir -p $(dirname {outfile})",
                        cmd],
            "clean": True}


def task_html_images():
    """
    Copy pre-converted SVG images to proper directory.
    """
    for img in SRC_TIKZ:
        src = IMGDIR / img.relative_to(SRCDIR).with_suffix(".svg")
        dest = HTMLDIR / src.relative_to(IMGDIR)
        yield {
            "name": dest,
            "targets": [dest],
            "file_dep": [src],
            "actions": [
                f"mkdir -p $(dirname {dest})",
                f"cp {src} {dest}"],
            "clean": True}


def task_images():
    """
    Convert TikZ diagrams to SVG for HTML inclusion.
    """
    for infile in SRC_TIKZ:
        outfile = IMGDIR / infile.relative_to(SRCDIR).with_suffix(".svg")
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": [infile],
            "actions": [
                f"mkdir -p $(dirname {outfile})",
                f"{TIKZ2SVG} {infile} {outfile}"],
            "clean": True}


# def task_latex_sections():
#     for infile in SRC_MD:
#         outfile = TEXDIR / infile.relative_to(SRCDIR).with_suffix(".tex")
#         cmd = (
#             "pandoc -s -f markdown -t latex"
#             f" --metadata-file={YAMLHEADER}"
#             f" -H {LATEX_PREAMBLE} -H {MODCMDS}"
#             f" -L {CSTM_BLKS} -L {INCL_FILE} -L {LATEX_TIPA}"
#             f" {infile} -o {outfile}"
#         )
#         yield {
#             "name": outfile,
#             "targets": [outfile],
#             "file_dep": [infile, YAMLHEADER, LATEX_PREAMBLE, MODCMDS],
#             "actions": [f"mkdir -p $(dirname {outfile})", cmd],
#             "clean": True}


# def task_pdf_sections():
#     for infile in SRC_MD:
#         srcsubdir = infile.parent
#         outfile = PDFDIR / infile.relative_to(SRCDIR).with_suffix(".pdf")
#         cmd = (
#             f"TEXINPUTS=.:{srcsubdir}:"
#             " pandoc -s -f markdown -t pdf"
#             f" --metadata-file={YAMLHEADER}"
#             f" -H {LATEX_PREAMBLE} -H {MODCMDS}"
#             f" -L {CSTM_BLKS} -L {INCL_FILE} -L {LATEX_TIPA}"
#             f" {infile} -o {outfile}"
#         )
#         yield {
#             "name": outfile,
#             "targets": [outfile],
#             "file_dep": [infile, YAMLHEADER, LATEX_PREAMBLE, MODCMDS],
#             "actions": [f"mkdir -p $(dirname {outfile})", cmd],
#             "clean": True}

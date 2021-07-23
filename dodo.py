"""
Doit task definition file.
"""

from pathlib import Path

DOIT_CONFIG = {"default_tasks": ["pdf_chaps", "html_chaps"]}
# DOIT_CONFIG = {"action_string_formatting": "new"}

# CLEANAUX = "scripts/cleanaux.sh"
TIKZ2SVG = "scripts/tikz2svg.sh"

LATEX_PREPROC = "scripts/latex-preprocess.sed"
CSTM_BLKS = "filters/custom-blocks.lua"
INCL_FILE = "filters/include-file.lua"
LATEX_TIPA = "filters/latex-tipa.lua"

MYCOMMANDS = Path("includes/mycommands.mdown")
MYPACKAGES = Path("includes/environments.sty")
YAMLHEADER = Path("includes/format.yaml")
WEBCSS = Path("includes/web-custom.css").resolve()  # must be absolute to load locally
MATHJAXCALL = Path("includes/include-mathjax.html")

SRCDIR = Path("source")

MD_EXTS = (".mdown", ".md")
SRC_MD = sorted(f for f in SRCDIR.glob('**/*') if f.suffix in MD_EXTS)

TIKZ_EXTS = (".tikz", ".forest")
SRC_TIKZ = sorted(f for f in SRCDIR.glob('**/*') if f.suffix in TIKZ_EXTS)

BUILDDIR = Path("build")
# MODSRCDIR = BUILDDIR / "modsource"
IMGDIR = BUILDDIR / "images"
TEXDIR = BUILDDIR / "latex"
PDFDIR = BUILDDIR / "pdf"
HTMLDIR = BUILDDIR / "html"
MODCMDS = BUILDDIR / "mycommands-preproc.mdown"

BOOK_CHAPS = ["01_intro", "02_n-grams", "03_universals", "04_representations",
              "05_automata"]
BOOK_CHAPS += [f"background/{subch}" for subch in
               ["algebra", "functions", "general", "graphs", "logic", "multisets",
                "posets", "relations", "sets", "strings", "tuples"]]


def task_mkdirs():
    for dirname in (TEXDIR, PDFDIR, HTMLDIR):
        yield {
            "name": dirname,
            "targets": [dirname],
            "actions": [f"mkdir -p {dirname}"]}


def task_modcommands():
    """
    Remove surrounding $ signs.
    """
    return {
        "targets": [MODCMDS],
        "file_dep": [MYCOMMANDS],
        "actions": [
            f"mkdir -p $(dirname {MODCMDS})",
            ("sed -e 's/\\(^\\$\\|\\$$\\)//g' -e '/^%%/d'"
             f" {MYCOMMANDS} > {MODCMDS}")],
            "clean": True}


# def task_modsource():
#     for infile in SRC_MD:
#         outfile = MODSRCDIR / infile.relative_to(SRCDIR)
#         yield {
#             "name": outfile,
#             "targets": [outfile],
#             "file_dep": [infile],
#             "actions": [
#                 f"mkdir -p $(dirname {outfile})",
#                 f"sed -f {LATEX_PREPROC} {infile} > {outfile}"],
#             "clean": True}


def task_latex_chaps():
    for ch in BOOK_CHAPS:
        infiles = [str(f)
                   for f in sorted(Path(f"{SRCDIR}/{ch}").glob("*.mdown"))]
        outfile = f"{TEXDIR}/{ch}.tex"
        cmd = (
            "pandoc -s -f markdown -t latex"
            f" --metadata-file={YAMLHEADER}"
            f" -H {MYPACKAGES} -H {MODCMDS}"
            f" -L {CSTM_BLKS} -L {INCL_FILE} -L {LATEX_TIPA}"
            f" {' '.join(infiles)} -o {outfile}"
        )
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": infiles + [YAMLHEADER, MYPACKAGES, MODCMDS],
            "actions": [f"mkdir -p $(dirname {outfile})", cmd],
            "clean": True}


def task_pdf_chaps():
    """
    Build PDF chapters directly from source.
    """
    for ch in BOOK_CHAPS:
        srcsubdir = SRCDIR / ch
        infiles = [str(f)
                   for f in sorted(Path(f"{SRCDIR}/{ch}").glob("*.mdown"))]
        outfile = f"{PDFDIR}/{ch}.pdf"
        cmd = (
            f"TEXINPUTS=.:{srcsubdir}:"
            " pandoc -s -f markdown -t pdf"
            f" --metadata-file={YAMLHEADER}"
            f" -H {MYPACKAGES} -H {MODCMDS}"
            f" -L {CSTM_BLKS} -L {INCL_FILE} -L {LATEX_TIPA}"
            f" {' '.join(infiles)} -o {outfile}"
        )
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": infiles + [YAMLHEADER, MYPACKAGES, MODCMDS],
            "actions": [f"mkdir -p $(dirname {outfile})", cmd],
            "clean": True}


def task_html_chaps():
    for ch in BOOK_CHAPS:
        infiles = sorted(str(f)
                         for f in Path(f"{SRCDIR}/{ch}").glob("*.mdown"))
        incl_images = sorted(HTMLDIR / img.relative_to(SRCDIR).with_suffix(".svg")
                             for img in SRC_TIKZ)
        outfile = Path(f"{HTMLDIR}/{ch}/index.html")
        cmd = (
            "pandoc -s -f markdown -t html --shift-heading-level-by=1"
            f" --metadata title={ch}"
            f" --mathjax -Vmath='' -H {MATHJAXCALL}"
            f" -L {INCL_FILE}"
            f" -c {WEBCSS}"
            f" {MODCMDS} {' '.join(infiles)} -o {outfile}"
        )
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": [*infiles, *incl_images,
                         YAMLHEADER, MYPACKAGES, MODCMDS],
            "actions": [f"mkdir -p $(dirname {outfile})",
                        cmd],
            "clean": True}


def task_html_images():
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


def task_latex_sections():
    for infile in SRC_MD:
        outfile = TEXDIR / infile.relative_to(SRCDIR).with_suffix(".tex")
        cmd = (
            "pandoc -s -f markdown -t latex"
            f" --metadata-file={YAMLHEADER}"
            f" -H {MYPACKAGES} -H {MODCMDS}"
            f" -L {CSTM_BLKS} -L {INCL_FILE} -L {LATEX_TIPA}"
            f" {infile} -o {outfile}"
        )
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": [infile, YAMLHEADER, MYPACKAGES, MODCMDS],
            "actions": [f"mkdir -p $(dirname {outfile})", cmd],
            "clean": True}


def task_pdf_sections():
    for infile in SRC_MD:
        srcsubdir = infile.parent
        outfile = PDFDIR / infile.relative_to(SRCDIR).with_suffix(".pdf")
        cmd = (
            f"TEXINPUTS=.:{srcsubdir}:"
            " pandoc -s -f markdown -t pdf"
            f" --metadata-file={YAMLHEADER}"
            f" -H {MYPACKAGES} -H {MODCMDS}"
            f" -L {CSTM_BLKS} -L {INCL_FILE} -L {LATEX_TIPA}"
            f" {infile} -o {outfile}"
        )
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": [infile, YAMLHEADER, MYPACKAGES, MODCMDS],
            "actions": [f"mkdir -p $(dirname {outfile})", cmd],
            "clean": True}

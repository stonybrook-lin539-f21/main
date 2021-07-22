"""
Doit task definition file.
"""

from pathlib import Path
from glob import glob

DOIT_CONFIG = {"default_tasks": ["pdf_chaps", "latex_chaps", "html_chaps",
                                 "modsource"]}
# DOIT_CONFIG = {"action_string_formatting": "new"}

CLEANAUX = "scripts/cleanaux.sh"
LATEX_PREPROC = "scripts/latex-preprocess.sed"
CSTM_BLKS = "scripts/custom-blocks.lua"
INCL_FILE = "scripts/include-file.lua"

MYCOMMANDS = Path("includes/mycommands.mdown")
MYPACKAGES = Path("includes/environments.sty")
YAMLHEADER = Path("includes/format.yaml")
WEBCSS = Path("includes/web-custom.css").resolve()  # must be absolute to load locally
MATHJAXCALL = Path("includes/include-mathjax.html")

SRCDIR = Path("source")
SRC = SRCDIR.glob("**/*.mdown")

BUILDDIR = Path("build")
MODSRCDIR = BUILDDIR / "modsource"
TEXDIR = BUILDDIR / "latex"
PDFDIR = BUILDDIR / "pdf"
HTMLDIR = BUILDDIR / "html"
MODCMDS = BUILDDIR / "mycommands-preproc.mdown"
# MODCMDS_TEX = BUILDDIR / "mycommands-tex.mdown"
# MODCMDS_HTML = BUILDDIR / "mycommands-html.mdown"
# MODSRC = $(patsubst $(SRCDIR)/%.mdown, $(MODSRCDIR)/%.mdown, $(SRC))
# TEX = $(patsubst $(SRCDIR)/%.mdown, $(TEXDIR)/%.tex, $(SRC))
# PDF = $(patsubst $(SRCDIR)/%.mdown, $(PDFDIR)/%.pdf, $(SRC))
# HTML = $(patsubst $(SRCDIR)/%.mdown, $(HTMLDIR)/%.html, $(SRC))

BOOK_CHAPS = ["01_intro", "02_n-grams", "03_universals", "04_representations",
              "05_automata"]
BOOK_CHAPS += [f"background/{subch}" for subch in
               ["algebra", "functions", "general", "graphs", "logic", "multisets",
                "posets", "relations", "sets", "strings", "tuples"]]


def task_mkdirs():
    for dirname in (MODSRCDIR, TEXDIR, PDFDIR, HTMLDIR):
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


def task_modsource():
    for infile in SRC:
        outfile = MODSRCDIR / infile.relative_to(SRCDIR)
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": [infile],
            "actions": [
                f"mkdir -p $(dirname {outfile})",
                f"sed -f {LATEX_PREPROC} {infile} > {outfile}"],
            "clean": True}


def task_latex_chaps():
    for ch in BOOK_CHAPS:
        infiles = sorted(str(MODSRCDIR / f.relative_to(SRCDIR))
                         for f in Path(f"{SRCDIR}/{ch}").glob("*.mdown"))
        outfile = f"{TEXDIR}/{ch}.tex"
        cmd = (
            "pandoc -s -f markdown -t latex"
            f" --metadata-file={YAMLHEADER}"
            f" -H {MYPACKAGES} -H {MODCMDS}"
            f" -L {CSTM_BLKS} -L {INCL_FILE}"
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
        infiles = sorted(str(MODSRCDIR / f.relative_to(SRCDIR))
                         for f in Path(f"{SRCDIR}/{ch}").glob("*.mdown"))
        outfile = f"{PDFDIR}/{ch}.pdf"
        cmd = (
            "pandoc -s -f markdown -t pdf"
            f" --metadata-file={YAMLHEADER}"
            f" -H {MYPACKAGES} -H {MODCMDS}"
            f" -L {CSTM_BLKS} -L {INCL_FILE}"
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
        infiles = sorted(str(MODSRCDIR / f.relative_to(SRCDIR))
                         for f in Path(f"{SRCDIR}/{ch}").glob("*.mdown"))
        outfile = f"{HTMLDIR}/{ch}.html"
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
            "file_dep": infiles + [YAMLHEADER, MYPACKAGES, MODCMDS],
            "actions": [f"mkdir -p $(dirname {outfile})", cmd],
            "clean": True}

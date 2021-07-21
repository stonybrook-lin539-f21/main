"""
Doit task definition file.
"""

from pathlib import Path
from glob import glob

DOIT_CONFIG = {"default_tasks": ["pdf_chaps", "html_chaps"]}
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
BUILDDIR = Path("build")
MODSRCDIR = Path("build") / "modsource"
TEXDIR = Path("build") / "latex"
PDFDIR = Path("build") / "pdf"
HTMLDIR = Path("build") / "html"

SRC = SRCDIR.glob("**/*.mdown")
MODCMDS_TEX = TEXDIR / MYCOMMANDS.name
MODCMDS_HTML = HTMLDIR / MYCOMMANDS.name
# MODSRC = $(patsubst $(SRCDIR)/%.mdown, $(MODSRCDIR)/%.mdown, $(SRC))
# TEX = $(patsubst $(SRCDIR)/%.mdown, $(TEXDIR)/%.tex, $(SRC))
# PDF = $(patsubst $(SRCDIR)/%.mdown, $(PDFDIR)/%.pdf, $(SRC))
# HTML = $(patsubst $(SRCDIR)/%.mdown, $(HTMLDIR)/%.html, $(SRC))

BOOK_CHAPS = ["01_intro", "02_n-grams", "03_universals",
              "04_representations", "05_automata"]


def task_mkdirs():
    for dirname in (MODSRCDIR, TEXDIR, PDFDIR, HTMLDIR):
        yield {
            "name": dirname,
            "targets": [dirname],
            "actions": [f"mkdir -p {dirname}"]}


def task_modcommands_tex():
    return {
        "targets": [MODCMDS_TEX],
        "file_dep": [MYCOMMANDS],
        "actions": [
            f"mkdir -p $(dirname {MODCMDS_TEX})",
            f"sed 's/\\(^\\$\\|\\$$\\)//g' {MYCOMMANDS} > {MODCMDS_TEX}"]}


def task_modcommands_html():
    return {
        "targets": [MODCMDS_HTML],
        "file_dep": [MYCOMMANDS],
        "actions": [
            f"mkdir -p $(dirname {MODCMDS_HTML})",
            ("sed -e 's/^\\$/\\\\(/g' -e 's/\\$$/\\\\)/g' -e '/^%%/d'"
             f" {MYCOMMANDS} > {MODCMDS_HTML}")]}


def task_modsource():
    for infile in SRC:
        outfile = MODSRCDIR / infile.relative_to(SRCDIR)
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": [infile],
            "actions": [
                f"mkdir -p $(dirname {outfile})",
                f"sed -f {LATEX_PREPROC} {infile} > {outfile}"]}


def task_pdf_chaps():
    for ch in BOOK_CHAPS:
        infiles = glob(f"{MODSRCDIR}/{ch}/*.mdown")
        outfile = f"{PDFDIR}/{ch}.pdf"
        cmd = (
            "pandoc -s -f markdown -t pdf"
            f" --metadata-file={YAMLHEADER}"
            f" -H {MYPACKAGES} -H {MODCMDS_TEX}"
            f" -L {CSTM_BLKS} -L {INCL_FILE}"
            f" {' '.join(infiles)} -o {outfile}"
        )
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": infiles + [YAMLHEADER, MYPACKAGES, MODCMDS_TEX],
            "actions": [f"mkdir -p $(dirname {outfile})", cmd],
            "clean": True}


def task_html_chaps():
    for ch in BOOK_CHAPS:
        infiles = glob(f"{MODSRCDIR}/{ch}/*.mdown")
        outfile = f"{HTMLDIR}/{ch}.html"
        cmd = (
            "pandoc -s -f markdown -t html"
            f" --mathjax -Vmath='' -H {MATHJAXCALL}"
            f" -H {MODCMDS_HTML}"
            f" -L {INCL_FILE}"
            f" -c {WEBCSS}"
            f" {' '.join(infiles)} -o {outfile}"
        )
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": infiles + [YAMLHEADER, MYPACKAGES, MODCMDS_HTML],
            "actions": [f"mkdir -p $(dirname {outfile})", cmd],
            "clean": True}

# Makefile to convert full course notes

HTML2LATEX = scripts/html2latex.sed
CLEANAUX = scripts/cleanaux.sh

MYCOMMANDS = includes/mycommands.mdown
MYPACKAGES = includes/environments.sty
YAML = includes/format.yaml
WEBCSS = includes/web-custom.css
MATHJAXCALL = includes/include-mathjax.html

SRCDIR = source
BUILDDIR = build
MODSRCDIR = $(BUILDDIR)/modsource
TEXDIR = $(BUILDDIR)/latex
PDFDIR = $(BUILDDIR)/pdf
HTMLDIR = $(BUILDDIR)/html

SRC = $(shell find ${SRCDIR} -name *.mdown)
MODCMDS_TEX = $(TEXDIR)/$(shell basename $(MYCOMMANDS))
MODCMDS_HTML = $(HTMLDIR)/$(shell basename $(MYCOMMANDS))
MODSRC = $(patsubst $(SRCDIR)/%.mdown, $(MODSRCDIR)/%.mdown, $(SRC))
TEX = $(patsubst $(SRCDIR)/%.mdown, $(TEXDIR)/%.tex, $(SRC))
PDF = $(patsubst $(SRCDIR)/%.mdown, $(PDFDIR)/%.pdf, $(SRC))
HTML = $(patsubst $(SRCDIR)/%.mdown, $(HTMLDIR)/%.html, $(SRC))

.DELETE_ON_ERROR:

.PHONY: all
all: $(PDF_CHS)

.PHONY: testpdf
testpdf: $(filter $(PDFDIR)/test/%.pdf, $(PDF))

.PHONY: testhtml
testhtml: $(filter $(HTMLDIR)/test/%.html, $(HTML))

$(BUILDDIR) $(TEXDIR) $(PDFDIR) $(HTMLDIR):
	mkdir -p $@

$(MODCMDS_TEX): $(MYCOMMANDS)
	mkdir -p $(shell dirname "$@")
	sed 's/\(^\$$\|\$$$$\)//g' "$(MYCOMMANDS)" > "$(MODCMDS_TEX)"

$(MODCMDS_HTML): $(MYCOMMANDS)
	mkdir -p $(shell dirname "$@")
	sed -e 's/^\$$/\\(/g' -e 's/\$$$$/\\)/g' -e '/^%/d' \
		"$(MYCOMMANDS)" > "$(MODCMDS_HTML)"

$(MODSRC): $(MODSRCDIR)/%.mdown: $(SRCDIR)/%.mdown $(HTML2LATEX)
	mkdir -p $(shell dirname "$@")
	sed -f "$(HTML2LATEX)" "$<" > "$@"

$(TEX): $(TEXDIR)/%.tex: $(MODSRCDIR)/%.mdown $(MODCMDS_TEX)
	mkdir -p $(shell dirname $@)
	pandoc -f markdown -t latex --standalone \
		--metadata-file="$(YAML)" \
		-H "$(MYPACKAGES)" \
		-H "$(MODCMDS_TEX)" "$<" -o "$@"
	sed -i 's/\\input.*\.tikz}/REMOVED/g' $@

$(PDF): $(PDFDIR)/%.pdf: $(TEXDIR)/%.tex
	$(eval pdfsubdir=$(shell dirname $@))
	$(eval texsubdir=$(patsubst $(PDFDIR)/%, $(TEXDIR)/%, $(pdfsubdir)))
	$(eval srcsubdir=$(patsubst $(PDFDIR)/%, $(SRCDIR)/%, $(pdfsubdir)))
	mkdir -p $(pdfsubdir)
	TEXINPUTS=".:$(srcsubdir):" latexmk -pdf \
		-interaction=nonstopmode -halt-on-error \
		-outdir="$(pdfsubdir)" \
		"$<"

$(HTML): $(HTMLDIR)/%.html: $(SRCDIR)/%.mdown $(MODCMDS_HTML) $(WEBCSS)
	$(eval htmlsubdir=$(shell dirname $@))
	mkdir -p $(htmlsubdir)
	pandoc --verbose -s -f markdown -t html \
		--mathjax -Vmath="" -H $(MATHJAXCALL) \
		-H $(MODCMDS_HTML) \
		-c $(abspath $(WEBCSS)) \
		$< -o $@

.PHONY: clean
clean:
	rm -rf $(MODSRCDIR)
	rm -rf $(PDFDIR)
	rm -rf $(HTMLDIR)

.PHONY: cleanaux
cleanaux:
	bash $(CLEANAUX) $(shell find $(PDFDIR) -type d)

.PHONY: cleanhtml
cleanhtml:
	rm -rf $(HTMLDIR)

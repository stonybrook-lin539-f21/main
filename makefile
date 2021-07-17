# Makefile to convert full course notes

HTML2LATEX = html2latex.sed
MYCOMMANDS = templates/mycommands.mdown
MYPACKAGES = templates/environments.sty
YAML = templates/format.yaml
CLEANAUX = scripts/cleanaux.sh

SRCDIR = source
BUILDDIR = build
MODSRCDIR = $(BUILDDIR)/modsource
TEXDIR = $(BUILDDIR)/latex
PDFDIR = $(BUILDDIR)/pdf

SRC = $(shell find ${SRCDIR} -name *.mdown)
MODCOMMANDS = $(BUILDDIR)/$(shell basename $(MYCOMMANDS))
MODSRC = $(patsubst $(SRCDIR)/%.mdown, $(MODSRCDIR)/%.mdown, $(SRC))
TEX = $(patsubst $(SRCDIR)/%.mdown, $(TEXDIR)/%.tex, $(SRC))
PDF = $(patsubst $(SRCDIR)/%.mdown, $(PDFDIR)/%.pdf, $(SRC))

PDFSUBDIRS = $(shell find $(PDFDIR) -type d)

.DELETE_ON_ERROR:

all: $(PDF)

$(BUILDDIR):
	mkdir -p "$(BUILDDIR)"

$(MODCOMMANDS): $(MYCOMMANDS)
	sed 's/\(^\$\|\$$\)//g' "$(MYCOMMANDS)" > "$(MODCOMMANDS)"

$(MODSRC): $(MODSRCDIR)/%.mdown: $(SRCDIR)/%.mdown $(HTML2LATEX)
	mkdir -p $(shell dirname "$@")
	sed -f "$(HTML2LATEX)" "$<" > "$@"

$(TEX): $(TEXDIR)/%.tex: $(MODSRCDIR)/%.mdown
	mkdir -p $(shell dirname $@)
	pandoc -f markdown -t latex --standalone \
		--metadata-file="$(YAML)" \
		-H "$(MYPACKAGES)" \
		-H "$(MODCOMMANDS)" "$<" -o "$@"
	sed -i 's/\\input.*\.tikz}/REMOVED/g' $@

$(PDF): $(PDFDIR)/%.pdf: $(TEXDIR)/%.tex
# 	$(eval srcsubdir=$(shell dirname $(word 2,$^)))
	$(eval pdfsubdir=$(shell dirname $@))
	$(eval texsubdir=$(patsubst $(PDFDIR)/%, $(TEXDIR)/%, $(pdfsubdir)))
	$(eval srcsubdir=$(patsubst $(PDFDIR)/%, $(SRCDIR)/%, $(pdfsubdir)))
	mkdir -p $(shell dirname $@)
	TEXINPUTS=".:$(srcsubdir):" latexmk -pdf \
		-outdir="$(pdfsubdir)" \
		-interaction=nonstopmode -halt-on-error "$<"

.PHONY: cleanaux
cleanaux:
	bash $(CLEANAUX) $(PDFSUBDIRS)

.PHONY: clean
clean:
	rm -rf $(MODSRCDIR)
	rm -rf $(PDFDIR)

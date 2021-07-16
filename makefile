# Makefile to convert full course notes

HTML2LATEX = html2latex.sed
MYCOMMANDS = templates/mycommands.mdown
MYPACKAGES = templates/environments.sty
YAML = templates/format.yaml

SRCDIR = source
BUILDDIR = build
MODSRCDIR = $(BUILDDIR)/modsource
PDFDIR = $(BUILDDIR)/pdf

SRC = $(shell find ${SRCDIR} -name *.mdown)
MODCOMMANDS = $(BUILDDIR)/$(shell basename $(MYCOMMANDS))
MODSRC = $(patsubst $(SRCDIR)/%.mdown, $(MODSRCDIR)/%.mdown, $(SRC))
TEX = $(patsubst $(SRCDIR)/%.mdown, $(PDFDIR)/%.tex, $(SRC))
PDF = $(patsubst $(SRCDIR)/%.mdown, $(PDFDIR)/%.pdf, $(SRC))

.DELETE_ON_ERROR:

all: $(PDF)

$(BUILDDIR):
	mkdir -p "$(BUILDDIR)"

$(MODCOMMANDS): $(MYCOMMANDS)
	sed 's/\(^\$\|\$$\)//g' "$(MYCOMMANDS)" > "$(MODCOMMANDS)"

$(MODSRC): $(MODSRCDIR)/%.mdown: $(SRCDIR)/%.mdown
	mkdir -p $(shell dirname "$@")
	sed -f "$(HTML2LATEX)" "$<" > "$@"

$(TEX): $(PDFDIR)/%.tex: $(MODSRCDIR)/%.mdown $(MODCOMMANDS)
	mkdir -p $(shell dirname $@)
	pandoc -f markdown -t latex --standalone \
		--metadata-file="$(YAML)" \
		-H "$(MYPACKAGES)" \
		-H "$(MODCOMMANDS)" "$<" -o "$@"

$(PDF): $(PDFDIR)/%.pdf: $(PDFDIR)/%.tex $(SRCDIR)/%.mdown
	$(eval srcsubdir=$(shell dirname $(word 2,$^)))
	$(eval buildsubdir=$(shell dirname $@))
	mkdir -p $(shell dirname $@)
	TEXINPUTS=".:$(srcsubdir):" latexmk -pdf \
		-auxdir="$(buildsubdir)" -outdir="$(buildsubdir)" \
		-interaction=nonstopmode -halt-on-error "$<"

.PHONY: cleanaux
cleanaux:
	latexmk -c $(TEX)

.PHONY: clean
clean:
	rm -rf $(MODSRCDIR)
	rm -rf $(PDFDIR)

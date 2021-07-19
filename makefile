# Makefile to convert full course notes

HTML2LATEX = scripts/html2latex.sed
CLEANAUX = scripts/cleanaux.sh

MYCOMMANDS = templates/mycommands.mdown
MYPACKAGES = templates/environments.sty
YAML = templates/format.yaml
WEBCSS = templates/web-custom.css

SRCDIR = source
BUILDDIR = build
MODSRCDIR = $(BUILDDIR)/modsource
TEXDIR = $(BUILDDIR)/latex
PDFDIR = $(BUILDDIR)/pdf
HTMLDIR = $(BUILDDIR)/html

SRC = $(shell find ${SRCDIR} -name *.mdown)
MODCOMMANDS = $(BUILDDIR)/$(shell basename $(MYCOMMANDS))
MODSRC = $(patsubst $(SRCDIR)/%.mdown, $(MODSRCDIR)/%.mdown, $(SRC))
TEX = $(patsubst $(SRCDIR)/%.mdown, $(TEXDIR)/%.tex, $(SRC))
PDF = $(patsubst $(SRCDIR)/%.mdown, $(PDFDIR)/%.pdf, $(SRC))
HTML = $(patsubst $(SRCDIR)/%.mdown, $(HTMLDIR)/%.html, $(SRC))

PDFSUBDIRS = $(shell find $(PDFDIR) -type d)

.DELETE_ON_ERROR:

all: $(filter $(HTMLDIR)/test/%.html, $(HTML))

$(BUILDDIR):
	mkdir -p "$(BUILDDIR)"

$(MODCOMMANDS): $(MYCOMMANDS) $(BUILDDIR)
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
	$(eval pdfsubdir=$(shell dirname $@))
	$(eval texsubdir=$(patsubst $(PDFDIR)/%, $(TEXDIR)/%, $(pdfsubdir)))
	$(eval srcsubdir=$(patsubst $(PDFDIR)/%, $(SRCDIR)/%, $(pdfsubdir)))
	mkdir -p $(pdfsubdir)
	TEXINPUTS=".:$(srcsubdir):" latexmk -pdf \
		-interaction=nonstopmode -halt-on-error \
		-outdir="$(pdfsubdir)" \
		"$<"

$(HTML): $(HTMLDIR)/%.html: $(SRCDIR)/%.mdown $(MYCOMMANDS) $(WEBCSS)
	$(eval htmlsubdir=$(shell dirname $@))
	mkdir -p $(htmlsubdir)
	cp $(WEBCSS) $(htmlsubdir)/$(shell basename $(WEBCSS))
	pandoc --verbose -s -f markdown -t html \
		-c $(shell basename $(WEBCSS)) \
		$< -o $@

.PHONY: clean
clean:
	rm -rf $(MODSRCDIR)
	rm -rf $(PDFDIR)

.PHONY: cleanaux
cleanaux:
	bash $(CLEANAUX) $(PDFSUBDIRS)

.PHONY: cleanhtml
cleanhtml:
	rm -rf $(HTMLDIR)

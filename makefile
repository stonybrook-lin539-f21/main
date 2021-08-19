# Makefile to convert full course notes

TIKZ2SVG = scripts/tikz2svg.sh
CLEANAUX = scripts/cleanaux.sh

CSTM_BLKS = filters/custom-blocks.lua
INCL_FILE = filters/include-file.lua
LATEX_TIPA = filters/latex-tipa.lua

MYCOMMANDS = includes/mycommands.mdown
LATEX_PREAMBLE = includes/preamble.tex
YAMLHEADER = includes/format.yaml
WEBCSS = $(abspath includes/web-custom.css) # must be absolute to load locally
MATHJAXCALL = includes/include-mathjax.html

SRCDIR = source
BUILDDIR = build
TEXDIR = $(BUILDDIR)/latex
PDFDIR = $(BUILDDIR)/pdf
HTMLDIR = $(BUILDDIR)/html

SRC = $(shell find ${SRCDIR} -name *.mdown)
MODCMDS = $(BUILDDIR)/mycommands-preproc.mdown
MODCMDS_MATHJAX = $(BUILDDIR)/mycommands-mathjax.mdown
TEX = $(patsubst $(SRCDIR)/%.mdown, $(TEXDIR)/%.tex, $(SRC))
PDF = $(patsubst $(SRCDIR)/%.mdown, $(PDFDIR)/%.pdf, $(SRC))
HTML = $(patsubst $(SRCDIR)/%.mdown, $(HTMLDIR)/%.html, $(SRC))

TESTDIR = test
TESTMD = $(TESTDIR)/full-style-and-feature-test.mdown
TESTTEX = $(patsubst %.mdown, %.tex, $(TESTMD))
TESTPDF = $(patsubst %.mdown, %.pdf, $(TESTMD))
TESTHTML = $(patsubst %.mdown, %.html, $(TESTMD))

.DELETE_ON_ERROR:

.PHONY: all
all: $(HTML)

.PHONY: test
test: $(TESTHTML) $(TESTPDF)

$(BUILDDIR) $(TEXDIR) $(PDFDIR) $(HTMLDIR):
	mkdir -p $@

$(MODCMDS): $(MYCOMMANDS)
	mkdir -p $(shell dirname "$@")
	sed -e 's/\(^\$$\|\$$$$\)//g' -e '/^%/d' $< > $@

$(MODCMDS_MATHJAX): $(MYCOMMANDS)
	mkdir -p $(shell dirname "$@")
	sed -e 's/^\$$/\\(/g' -e 's/\$$$$/\\)/g' -e '/^%/d' $< > $@

# $(TEX): $(TEXDIR)/%.tex: $(MODSRCDIR)/%.mdown $(MODCMDS)
# 	mkdir -p $(shell dirname $@)
# 	pandoc -f markdown -t latex --standalone \
# 		--metadata-file="$(YAMLHEADER)" \
# 		-H "$(MYPACKAGES)" \
# 		-H "$(MODCMDS)" "$<" -o "$@"
# 	sed -i 's/\\input.*\.tikz}/REMOVED/g' $@

# $(PDF): $(PDFDIR)/%.pdf: $(TEXDIR)/%.tex
# 	$(eval pdfsubdir=$(shell dirname $@))
# 	$(eval texsubdir=$(patsubst $(PDFDIR)/%, $(TEXDIR)/%, $(pdfsubdir)))
# 	$(eval srcsubdir=$(patsubst $(PDFDIR)/%, $(SRCDIR)/%, $(pdfsubdir)))
# 	mkdir -p $(pdfsubdir)
# 	TEXINPUTS=".:$(srcsubdir):" latexmk -pdf \
# 		-interaction=nonstopmode -halt-on-error \
# 		-outdir="$(pdfsubdir)" \
# 		"$<"

# $(HTML): $(HTMLDIR)/%.html: $(SRCDIR)/%.mdown $(MODCMDS) $(WEBCSS)
# 	$(eval htmlsubdir=$(shell dirname $@))
# 	mkdir -p $(htmlsubdir)
# 	pandoc --verbose -s -f markdown -t html \
# 		--mathjax -Vmath="" -H $(MATHJAXCALL) \
# 		-H $(MODCMDS) \
# 		-c $(WEBCSS) \
# 		$< -o $@

TEXDEPS = $(YAMLHEADER) $(LATEX_PREAMBLE) $(MODCMDS) \
		  $(CSTM_BLKS) $(INCL_FILE) $(LATEX_TIPA)
HTMLDEPS = $(MATHJAXCALL) $(INCL_FILE) $(WEBCSS) $(MODCMDS_MATHJAX)

$(TESTTEX): %.tex: %.mdown $(TEXDEPS)
	TEXINPUTS=".:$(TESTDIR):" \
		pandoc -s -f markdown-implicit_figures -t latex \
		--number-sections \
		--resource-path=.:$(TESTDIR) \
		--metadata-file=$(YAMLHEADER) \
		-H $(LATEX_PREAMBLE) -H $(MODCMDS) \
		-L $(CSTM_BLKS) -L $(INCL_FILE) -L $(LATEX_TIPA) \
		$< -o $@
		
$(TESTPDF): %.pdf: %.mdown $(TEXDEPS)
	TEXINPUTS=".:$(TESTDIR):" \
		pandoc -s -f markdown-implicit_figures -t pdf \
		--number-sections \
		--resource-path=.:$(TESTDIR) \
		--metadata-file=$(YAMLHEADER) \
		-H $(LATEX_PREAMBLE) -H $(MODCMDS) \
		-L $(CSTM_BLKS) -L $(INCL_FILE) -L $(LATEX_TIPA) \
		$< -o $@

$(TESTHTML): %.html: %.mdown $(HTMLDEPS)
	pandoc --verbose -s -f markdown-implicit_figures -t html \
		--shift-heading-level-by=1 \
		--mathjax -Vmath="" -H $(MATHJAXCALL) \
		-L $(INCL_FILE) \
		-c $(WEBCSS) \
		-H $(MODCMDS_MATHJAX) $< -o $@

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

.PHONY: cleantest
cleantest:
	rm -f $(TESTHTML) $(TESTPDF)

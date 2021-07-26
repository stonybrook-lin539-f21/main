# replace source markup with form suitable for PDFLaTeX

# remove underscore from \input_{small,mid,large};
# this is needed to avoid Latex complaints
s/\\input_[^{]*{\([^}]*\)}/\\begin{center}\\input{\1}\\end{center}/g

# IPA replacements
s/ʃ/\\textipa{S}/g

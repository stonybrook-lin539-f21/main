# convert LaTeX environments to Markdown custom divs

s/\\begin{definition}/::: definition/g
s/\\begin{example}/::: example/g
s/\\begin{exercise}/::: exercise/g
s/\\begin{theorem}/::: theorem/g

s/\\end{definition}/:::/g
s/\\end{example}/:::/g
s/\\end{exercise}/:::/g
s/\\end{theorem}/:::/g

# convert \input_SIZE{FILENAME} to custom include block
s/\\input_\([[:alpha:]]*\){\([^}]*\)}/~~~ {.include-tikz size=\1}\n\2\n~~~/g

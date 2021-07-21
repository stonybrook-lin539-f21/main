# convert LaTeX environments to Markdown custom divs

s/\\begin{theorem}/::: definition/g
s/\\begin{theorem}/::: example/g
s/\\begin{theorem}/::: exercise/g
s/\\begin{theorem}/::: theorem/g

s/\\end{theorem}/:::/g
s/\\end{theorem}/:::/g
s/\\end{theorem}/:::/g
s/\\end{theorem}/:::/g

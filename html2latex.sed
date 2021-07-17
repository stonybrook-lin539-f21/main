# replace source markup with form suitable for LaTeX

# remove underscore from \input_{small,mid,large};
# this is needed to avoid Latex complaints
s/\\input_[^{]*{\([^}]*\)}/\\begin{center}\\input{\1}\\end{center}/g
# replace <i>X</i> by \emph{X}
s/<i>/\\emph{/g
s/<\/i>/}/g
# replace <b>X</b> by \textbf{X}
s/<b>/\\textbf{/g
s/<\/b>/}/g
# replace HTML lists by Latex
s/<ul>/\\begin{itemize}/g
s/<\/ul>/\\end{itemize}/g
s/<ol>/\\begin{enumerate}/g
s/<\/ol>/\\end{enumerate}/g
# replace <li>X</li> by \item X
s/<li>/\\item /g
s/<\/li>//g
# delete all <br> and <br />
s/<br\s*\/\?>//g
# IPA replacements
s/ʃ/\\textipa{S}/g

s/\\input_[^{]*{\([^}]*\)}/\\begin{center}\\input{\1}\\end{center}/g
# replace <i>
s/<\/i>/\x00/g  # replace by NUL for single character match of end
s/<i>\([^\x00]*\)\x00/\\emph{\1}/g  # replace <i>X</i> by \emph{X}
# replace <b>
s/<\/b>/\x00/g  # replace by NUL for single character match of end
s/<b>\([^\x00]*\)\x00/\\textbf{\1}/g # replace <b>X</b> by \textbf{X}
# replace HTML lists by Latex
s/<ul>/\\begin{itemize}/g
s/<\/ul>/\\end{itemize}/g
s/<ol>/\\begin{enumerate}/g
s/<\/ol>/\\end{enumerate}/g
s/<\/li>/\x00/g  # replace by NUL for single character match of end
s/<li>\([^\x00]*\)\x00/\\item \1/g
# delete all <br> and <br />
s/<br\s*\/\?>//g
# IPA replacements
s/ʃ/\\textipa{S}/g

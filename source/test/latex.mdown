
# Latex commands

## Raw Latex passthrough

Latex commands will be parsed as a "RawBlock" if the extension "raw_tex" is enabled.

Here is a custom Latex environment. 

\begin{myenvironment}
This is a custom Latex environment.
\end{myenvironment}

Here is an \\input call.

\input{mydiagram.tikz}

Here is a random undefined macro.

\mymacro{some text}

Here is one with an optional argument.

\mymacro[optional argument]{some text}

## Latex command expansion

Latex commands will be expanded if the extension "latex_macros" is enabled.

\newcommand{\newmacro}[1]{>>>#1<<<}

Before the macro \newmacro{in the macro} after the macro.

The end.

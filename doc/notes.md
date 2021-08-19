# Pandoc problems

- Pandoc breaks raw TeX at underscores, and furthermore splits it into two blocks in the case of \input_whatever. In other cases it makes both inline elements, which might result in okay LaTeX output.
- Headers inserted at build time are not subjected to most processing, including TeX math conversion and LaTeX command expansion.
- Custom LaTeX commands are finicky in general. In general, they must be part of an input document rather than a header and must not be wrapped with dollars or backslash + parens. For LaTeX they can be included as a header since Pandoc's pre-processing is not needed. For HTML + Mathjax, if you have only custom math macros, it is possible to use backslash + parens, in which case they *must* be included as a header.
- There is a problem with the --mathjax command, which performs preprocessing, then inserts the Mathjax script *only if* LaTeX math is detected. This means that in a file with no math, the custom commands that we insert will appear as raw text. The author of Pandoc has refused to change this. As a workaround, we use -Vmath='' to manually clear the internal variable where Pandoc records whether math was detected, and insert the script ourselves.
- The title must be included as metadata.
	- if you shift heading levels, the top heading will become a title, but then the new top heading level will be `<h1>` in HTML, which is wrong.

# GNU Make problems
- can't apply a rule to list of targets with different dependencies. all workarounds are ugly.
- have to escape dollar signs.

# PyDoit problems

- new style (curly bracket) string interpolation not available in Doit 0.31
- inserting some variables in commands in task definition and letting doit interpolate "targets" and "dependencies" later requires extra escapes, and is generally messy
- can't depend on a directory to trigger task to make it (!!!)
- have to escape percent sign

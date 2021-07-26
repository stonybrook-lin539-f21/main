pandoc problems
- headers inserted at build time are not subjected to most processing, including TeX math conversion and (?) LaTeX command expansion
- breaks raw tex at underscore, and furthermore splits into two blocks in the case of \input_whatever. In othercases it makes both inline elements, which might result in okay latex output.
- There is a problem with the --mathjax command, which performs preprocessing, then inserts the Mathjax script *only if* LaTeX math is detected. This means that in a file with no math, the custom commands that we insert will appear as raw text. The author of Pandoc has refused to change this. As a workaround, we use -Vmath='' to manually clear the internal variable where Pandoc records whether math was detected, and insert the script ourselves.

make problems
- can't apply a rule to list of targets with different dependencies. all workarounds are ugly
- have to escape dollar signs

doit problems
- new style (curly bracket) string interpolation not available in Doit 0.31
- inserting some variables in commands in task definition and letting doit interpolate "targets" and "dependencies" later requires extra escapes, and is generally messy
- can't depend on a directory to trigger task to make it (!!!)

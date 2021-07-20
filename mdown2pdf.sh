#!/usr/bin/env bash
set -u

if [ $# -ne 1 ]; then
    echo "Usage: $0 SRCFILE"
    exit 1
fi

projectroot="$(dirname $(realpath $0))"
sedscript="${projectroot}/html2latex.sed"
mycommands="${projectroot}/includes/mycommands.mdown"
mypackages="${projectroot}/includes/environments.sty"
yaml="${projectroot}/includes/format.yaml"

sourcefile="$1"
sourcedir=$(dirname "$sourcefile")
tempdir="$(mktemp -dt lin539-mdown2pdf-XXXXX)"

builddir="$projectroot/build/pdf/${sourcedir##source/}"
mkdir -p "$builddir"

# exit

# preprocess mycommands
# delete line-initial and line-final $
modcommands="$tempdir/$(basename "$mycommands")"
sed 's/\(^\$\|\$$\)//g' "$mycommands" > "$modcommands"

# regex substitutions in source file
modsource="$tempdir/$(basename "$sourcefile")"
sed -f "$sedscript" "$sourcefile" > "$modsource"

# convert with pandoc
tex="$builddir/$(basename "$sourcefile" .mdown).tex"
pdf="$builddir/$(basename "$modsource" .mdown).pdf"
pandoc "$modsource" -t latex --standalone --metadata-file="$yaml" -H "$mypackages" -H "$modcommands" -o "$tex"
# cd "$builddir"
# latexmk -pdf "$tex"
latexmk -pdf -outdir="$builddir" -interaction=nonstopmode  "$tex"
latexmk -c "$tex"
# popd

# remove temporary files
# rm "$tex" 2> /dev/null
# rm "$modcommands" 2> /dev/null
# rm "$modsource" 2> /dev/null
rm -rf "$tempdir" 2> /dev/null

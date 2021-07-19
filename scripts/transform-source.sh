#!/usr/bin/env sh

for f in $(find source -name "*.mdown"); do
	sed -i -f $1 $f
done

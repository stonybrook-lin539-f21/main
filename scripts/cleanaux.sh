#!/usr/bin/env bash

for dir in ${@}; do
	for f in ${dir}/*.{aux,fdb_latexmk,fls,log,sta,thm}; do
		if [ -f $f ]; then rm $f; fi
	done
done

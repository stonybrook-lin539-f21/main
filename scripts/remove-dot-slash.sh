for f in source/**/**/*.mdown; do
	sed -i 's/\\input_small{\.\//\\input_small{/g' $f
	sed -i 's/\\input_mid{\.\//\\input_mid{/g' $f
	sed -i 's/\\input_med{\.\//\\input_med{/g' $f
	sed -i 's/\\input_large{\.\//\\input_large{/g' $f
done

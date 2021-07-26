# replace inline HTML with Markdown

# replace <i>X</i> by *X*
s/<i>/*/g
s/<\/i>/*/g

# replace <b>X</b> by **X**
s/<b>/**/g
s/<\/b>/**/g

# remove HTML list delimiters
s/<ul>//g
s/<\/ul>//g
s/<ol>//g
s/<\/ol>//g

# replace <li>X</li> by - X
s/<li>/- /g
s/<\/li>//g

# delete all <br> and <br />
s/<br\s*\/\?>//g

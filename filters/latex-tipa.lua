-- Filter to handle IPA characters blocks
-- Convert unicode characters to TIPA commands for pdflatex.
if FORMAT:match "latex" then
  function Str(elem)
    text = elem.text
    text = string.gsub(text, "ʃ", "\\textipa{S}")
    return pandoc.RawInline("latex", text)
  end
end

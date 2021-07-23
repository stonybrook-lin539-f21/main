-- Filter to handle IPA characters blocks
-- Convert unicode characters to TIPA commands for pdflatex.
if FORMAT:match "latex" then
  function Str(elem)
    text = elem.text
    text, count = string.gsub(text, "ʃ", "\\textipa{S}")
    if count > 0 then
      return pandoc.RawInline("latex", text)
    else
      return elem
    end
  end
end

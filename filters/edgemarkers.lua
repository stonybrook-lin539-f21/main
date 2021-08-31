-- Filter to handle convet some unicode math symbols to LaTeX
if FORMAT:match "latex" then
  function Str(elem)
    text = elem.text
    -- Convert edge markers to LaTeX math for pdflatex
    text, countL = string.gsub(text, "{{{L}}}", "\\ensuremath{\\rtimes}")
    text, countR = string.gsub(text, "{{{R}}}", "\\ensuremath{\\ltimes}")
    if countL > 0 or countR > 0 then
      return pandoc.RawInline("latex", text)
    else
      return elem
    end
  end
  function Math(elem)
    text = elem.text
    -- Convert edge markers to LaTeX math for pdflatex
    text, countL = string.gsub(text, "{{{L}}}", "\\ensuremath{\\rtimes}")
    text, countR = string.gsub(text, "{{{R}}}", "\\ensuremath{\\ltimes}")
    if countL > 0 or countR > 0 then
        elem.text = text
    end
    return elem
  end
end

if FORMAT:match "html" then
  function Str(elem)
    text = elem.text
    -- Convert edge markers to LaTeX math for pdflatex
    text, count = string.gsub(text, "{{{L}}}", "⋊")
    text, count = string.gsub(text, "{{{R}}}", "⋉")
    if count > 0 then
      return pandoc.RawInline("latex", text)
    else
      return elem
    end
  end
end

-- Filter to handle custom blocks

-- Convert custom div blocks to LaTeX environments
-- Convert only for LaTeX output. Pass through unchanged for HTML
if FORMAT:match "latex" then
  function Div(elem)
    cls = elem.classes[1]
    table.insert(elem.content, 1,
      pandoc.RawBlock("latex", "\\begin{" .. cls .. "}"))
    table.insert(elem.content,
      pandoc.RawBlock("latex", "\\end{" .. cls .. "}"))
    return elem
  end
end

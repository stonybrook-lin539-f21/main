-- Convert custom div blocks to LaTeX environments
if FORMAT:match "latex" then
  function Div(elem)
    envcls = elem.classes[1]
      table.insert(elem.content, 1,
        pandoc.RawBlock("latex", "\\begin{" .. envcls .. "}"))
      table.insert(elem.content,
        pandoc.RawBlock("latex", "\\end{" .. envcls .. "}"))
    return elem
  end
end

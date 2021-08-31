-- Filter to handle custom div blocks

-- Convert custom div blocks to LaTeX environments.
if FORMAT:match "latex" then
  function Div(elem)
    cls = elem.classes[1]
    if cls == "jupyterpython" then
        elem.content = {}
    else
        table.insert(elem.content, 1,
          pandoc.RawBlock("latex", "\\begin{" .. cls .. "}"))
        table.insert(elem.content,
          pandoc.RawBlock("latex", "\\end{" .. cls .. "}"))
    end
    return elem
  end
end

-- Convert exercise answer blocks for HTML. Leave other classes unchanged.
if FORMAT:match "html" then
  function Div(elem)
    cls = elem.classes[1]
    if cls == "exranswer" then
      table.insert(elem.content, 1,
        pandoc.RawBlock("html", "<details class=\"exr-answer\">"))
      table.insert(elem.content, 2,
        pandoc.RawBlock("html", "<summary>Show Answer</summary>"))
      table.insert(elem.content,
        pandoc.RawBlock("html", "</details>"))
      return elem.content
    else
      return elem
    end
  end
end

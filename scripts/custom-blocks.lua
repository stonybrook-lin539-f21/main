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

-- Identify directive to include a TikZ file
-- For LaTeX, insert an \input command
-- For HTML, insert an image tag pointing to an SVG of the same name
if FORMAT:match "latex" then
  function CodeBlock(elem)
    cls = elem.classes[1]
    if cls == "include-tikz" then
      filename = elem.text
      size = elem.attributes.style
      return pandoc.RawBlock("latex", "\\input{" .. filename .. "}")
    else
      return elem
    end
  end
end

if FORMAT:match "html" then
  function CodeBlock(elem)
    cls = elem.classes[1]
    if cls == "include-tikz" then
      filename = string.gsub(elem.text, "%..*$", ".svg")
      -- size = elem.attributes.style
      return pandoc.Para({pandoc.Image({pandoc.Str(filename)}, filename)})
    else
      return elem
    end
  end
end

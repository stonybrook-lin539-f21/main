-- Correctly insert image according to output format
-- For now, simply redact the image for HTML output
-- if FORMAT:match "latex" then
function RawBlock(elem)
  if string.match(elem.text, "\\input.*{.*%.tikz}") then
    return pandoc.Para("*****TikZ diagram removed*****")
  end
  if string.match(elem.text, "\\input.*{.*%.forest}") then
    return pandoc.Para("*****Forest diagram removed*****")
  end
  return elem
end
-- end
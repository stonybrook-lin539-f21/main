---
title: Style and Feature Test
---

This document is for testing styling in web (HTML/CSS) and PDF (LaTeX) output.

# Sections

Text in section.

## Subsection

Text in subsection.


# Text formatting

Start of section.

New paragraph.

- List item
- List item
- List item
    - List subitem
    - List subitem

Paragraph after list.

1. Numbered list item
2. Numbered list item
3. Numbered list item

Here is a quote block.

> This is a quote block.

Here is a code block.

```This is a code block.```

Here is a table.

| Right | Left | Default | Center |
|------:|:-----|---------|:------:|
|   12  |  12  |    12   |    12  |
|  123  |  123 |   123   |   123  |
|    1  |    1 |     1   |     1  |           

Before horizontal rule

---

After horizontal rule

# Math

Here is some inline math: $y = mx + b$.

And some display math:

$$y = mx + b$$

Now for some math using custom macros.

$\tuple{a, b, c}$

$\setof{a, b, c}$


# Images

PNG image at natural size.

![test image](images/sbuling-logo.png)

Image with custom size.

![small image](images/sbuling-logo.png){width=1in}


# Custom blocks

::: advice
This is some advice.
:::

::: theorem
This is a theorem.
:::

::: lemma
This is a lemma.
:::

::: definition
This is a definition.
:::

::: proof
This is a proof.
:::

::: example
This is a theorem.
:::

::: exercise
This is an exercise.
:::

::: exercise
This is an exercise with an answer. The answer will appear at the bottom of the document.

::: exranswer
This is the answer to an exercise.
:::
:::


# Custom includes

Simple included .tikz file.

~~~ include-tikz
images/abaa.tikz
~~~

Custom size. (Not yet implemented.)

~~~ {.include-tikz width=2in}
images/abaa.tikz
~~~

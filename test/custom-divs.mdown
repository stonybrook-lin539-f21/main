
# Custom div blocks

Here is a custom block.

::: theorem
This is a theorem.
:::

Here is a theorem with extra attributes.

::: {.theorem .fancy}
This is a theorem with extra attributes.
:::

The following does not work.

::: theorem {.fancy}
This is a block that mixes the simple and full syntax.
:::

Here is a block inside a block.

::: theorem
This is a theorem.

:::: theorem
This is a theorem inside a theorem.
::::
:::

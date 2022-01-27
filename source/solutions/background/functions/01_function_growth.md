# Function growth and Big O notation

::: exercise
Explain why every constant function is also a linear function.
:::

::: solution
A constant function is of the form $f(x) = d$ for every input $x$.
This is equivalent to $f(x) = 0x + d$, which is a linear function.
:::

::: exercise
Rewrite the formulas from the previous example so that they fit this pattern.
For instance, $f(x) = x^2$ can be rewritten as $f(x) = 1 x^2 + 0 x^1 + 0 x^0$.

*Reminder*: $(a + b)^2 = a^2 + 2ab + b^2$
:::

::: solution
- $f(x) = x^3 - 5x = 1 x^3 + 0 x^2 + (-5)x^1 + 0 x^0$
- $f(x) = -5x^4 + 7x^2 + (2x + 3)^2 = (-5)x^4 + 0x^3 + 11x^2 + 6x^1 + 0x^0$
- $f(x) = \frac{3x^4 + x^3}{17} = \frac{3}{17}x^4 + \frac{1}{17}x^3 + 0x^2 + 0x^1 + 0x^0$
:::

::: exercise
Explain why every linear function is also a polynomial function.
:::

::: solution
Every linear function is of the form $f(x) = kx + d$.
This can be rewritten as $f(x) = k x^1 + d x^0$.
:::

::: exercise
Give an example of a polynomial function $f$ and an exponential function $g$ such that $f(x) > g(x)$ for relatively small values of $x$ (e.g. $x < 100$) but $f(x) < g(x)$ for larger values.
:::

::: solution
The polynomial $f(x) = x^1 + 1024 x^0$ yields larger values than $g(x) = 2^x$ for all $x \leq 10$, but smaller values for $x > 10$.
:::

::: exercise
For each one of the formulas below, right down its simplified version in Big-O notation.

1. $O(x \times x) = O(x^2)$
1. $O(x(3x + 5) = O(3x^2)$
1. $O(x^2 + 17(x - \frac{2^x}{x}) = O(-\frac{2^x}{x})$
1. $O(2^x + 17 - (1 + 2^x) = O(2^x)$
:::

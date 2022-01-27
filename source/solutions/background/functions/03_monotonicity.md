# Monotonicity

::: exercise
For each one of the following functions, say whether it is monotonic.

~~~ {.include-tikz size=mid}
monotonicity_i.tikz
~~~
~~~ {.include-tikz size=mid}
monotonicity_j.tikz
~~~
~~~ {.include-tikz size=mid}
monotonicity_k.tikz
~~~
~~~ {.include-tikz size=mid}
monotonicity_l.tikz
~~~
:::

::: solution
- Not monotonic.
- Not monotonic.
- Both monotonically increasing and monotonically decreasing
- Not monotonic.
:::

::: exercise
Give another example of a function that is not monotonic.
:::

::: solution
A very simple, non-monotonic function is $f(x) = x^2$.
Here $f(-1) = 1$, $f(0) = 0$, and $f(1) = 1$.

A more interesting option is the function $f$ that maps $n$ to $n$ if $n$ is even and to $-n$ if $n$ is odd.
:::

::: exercise
For each one of the following functions say whether it is isotonic, antitonic, or neither.


- $f: \mathbb{N} \rightarrow \mathbb{N}$, $x \mapsto -x$
- $f: \mathbb{R} \rightarrow \mathbb{R}$, $x \mapsto x - 10$
- $f: \mathbb{R} \rightarrow \mathbb{R}$, $x \mapsto x^2$
- $f: \mathbb{R} \rightarrow \mathbb{R}$, $x \mapsto \frac{x}{2}$
- $f: \mathbb{N} \rightarrow \mathbb{N}$, $f(n)$ is $1$ if $n = 0$ and $n \mult f(n-1)$ otherwise

:::

::: solution
- $f: \mathbb{N} \rightarrow \mathbb{Z}$, $x \mapsto -x$ is antitonic
- $f: \mathbb{R} \rightarrow \mathbb{R}$, $x \mapsto x - 10$ is isotonic
- $f: \mathbb{R} \rightarrow \mathbb{R}$, $x \mapsto x^2$ is neither antitonic nor isotonic
- $f: \mathbb{R} \rightarrow \mathbb{R}$, $x \mapsto \frac{x}{2}$ is isotonic
- $f: \mathbb{N} \rightarrow \mathbb{N}$, $f(n)$ is $1$ if $n = 0$ and $n \mult f(n-1)$ is isotonic ($f$ is just $n!$)
:::

::: exercise
Given an example of a function that is both isotonic and antitonic.
:::

::: solution
Every constant function is both isotonic and antitonic.
:::

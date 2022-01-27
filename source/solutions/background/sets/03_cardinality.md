# Cardinality

::: exercise
Show that
$\card{\setof{ 0 \leq n < 10 \mid n \text{ is odd}} = \card{\setof{ 0 \leq n < 10 \mid n \text{ is even}}}}$.
:::

::: solution
The simple solution is to simply define both sets via list notation: $\setof{1,3,5,7,9}$ and $\setof{0,2,4,6,8}$.
Since both contain $5$ elements, they have the same cardinality.

Alternatively, we can define a function $f$ from the first set to the second such that $f(x) = x - 1$.
This is a bijection because for every element $y$ in the co-domain of $f$ there is exactly one $x$ in the domain of $f$ such that $f(x) = y$.
:::

::: exercise
Show that the set of natural numbers has the same cardinality as the set of all even natural numbers.
:::

::: solution
We define a function $f: \mathbb{N} \rightarrow \mathbb{N}$ with $n \mapsto 2n$.
For every natural number $y$, there is exactly one natural number $x$ such that $f(x) = y$.
Hence $f$ is a bijection.
:::

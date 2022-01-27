# Sets: The basics

::: exercise
Write the following as a set:

- the first names of your three favorite actors/actresses,
- the colors of the rainbow,
- all prime numbers between 1 and 10 (remember, 1 is not a prime number!)

:::

::: solution

- $\setof{\text{Lauren}, \text{Michael}, \text{Peter}}$
- $\setof{\text{red}, \text{orange}, \text{yellow}, \text{green}, \text{blue}, \text{indigo}, \text{violet}}$
- $\setof{2, 3, 5, 7}$

:::

::: exercise
Put $\in$, $\ni$, $\notin$, $\not\ni$ in the gaps below as appropriate:

- $5 \_ \setof{1,2,4,5,8}$
- $6 \_ \setof{1,2,4,5,8}$
- $\setof{5} \_ \setof{1,2,4,5,8}$
- $5 \_ \setof{1,2,4,5,8} \_ 6$

:::

::: solution

- $5 \in \setof{1,2,4,5,8}$
- $6 \notin \setof{1,2,4,5,8}$
- $\setof{5} \notin \setof{1,2,4,5,8}$
- $5 \in \setof{1,2,4,5,8} \not\ni 6$

:::

::: exercise
For each one of the following, fill the gap with $=$ or $\neq$ as appropriate:

- $\setof{a,b} \_ \setof{a,b}$
- $\setof{b,a} \_ \setof{a,b}$
- $\setof{b,a,c,d} \_ \setof{e,a,b,d}$

:::

::: solution

- $\setof{a,b} = \setof{a,b}$
- $\setof{b,a} = \setof{a,b}$
- $\setof{b,a,c,d} \neq \setof{e,a,b,d}$

:::

::: exercise
For each one of the following, fill the gap with $=$ or $\neq$ as appropriate:

- $\setof{a,b} \_ \setof{a,a,b,b}$
- $\setof{b,a} \_ \setof{a,b,a}$
- $\setof{c,b,a,a,d,c} \_ \setof{a,a,b,d,c,c,c}$
- $\setof{a} \_ \setof{a,a,a,a,a,a,c,a,a,a,a,a,a}$

:::

::: solution

- $\setof{a,b} = \setof{a,a,b,b}$
- $\setof{b,a} = \setof{a,b,a}$
- $\setof{c,b,a,a,d,c} = \setof{a,a,b,d,c,c,c}$
- $\setof{a} \neq \setof{a,a,a,a,a,a,c,a,a,a,a,a,a}$

:::

::: exercise
The sentence *If police police police, then police police police* actually uses two different word types.
It just just so happens that both are pronounced and spelled *police*.
But one is the noun *police*, the other one the verb *police*.
So we might want to annotate the string as follows:
*If police[N] police[V] police[N], then police[N] police[V] police[N]*.
Assume that words are annotated with their part of speech in this fashion.
Then what would be the corresponding set of words?
:::

::: solution

$\setof{
\text{if},
\text{police[N]},
\text{police[V]},
\text{then}}$

:::

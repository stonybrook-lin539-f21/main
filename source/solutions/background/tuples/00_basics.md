# Tuples: Basics

::: exercise
Fill in the gaps with $=$ and $\neq$ as appropriate, assuming that $a$ and $b$ are distinct elements:

- $\tuple{a} \neq \tuple{b}$ (different components) 
- $\tuple{a,b,a} \neq \tuple{a,b,b}$ (third component differs)
- $\tuple{a,b,a,a} = \tuple{a,b,a,a}$
- $\tuple{a,a,b,a} \neq \tuple{a,b,a,a}$ (second and third component switched)
- $\tuple{a,a,b,a} \neq \tuple{a,a,\setof{b},a}$ ($b \neq \setof{b}$)
- $\tuple{a,a,b,a} \neq \tuple{a,\tuple{a,b},a}$ (one is 4-tuple, the other a 3-tuple)
:::

::: exercise
If $A \is \setof{a}$, then what is $A^5$?
:::

::: solution
$A^5 = \setof{a}^5 = \setof{ \tuple{u,v,x,y,z} \mid u,v,x,y,z \in \setof{a} } = \setof{\tuple{a, a, a, a, a}}$
:::

::: exercise
If $A \is \setof{\setof{a}}$, then what is $A^1$?
:::

::: solution
$A^1 = \setof{\setof{a}}^1 = \setof{ \tuple{x} \mid x \in \setof{\setof{a}}} = \tuple{\setof{a}}$

::: exercise
Calculate the result of the following concatenations:

- $\tuple{a,b} \tuplecat ((\tuple{c} \tuplecat \tuple{a,b}) \tuplecat \tuple{a,c,e})$
- $(\tuple{a,b} \tuplecat \tuple{c}) \tuplecat (\tuple{a,b} \tuplecat \tuple{a,c,e})$

:::

::: solution
They both yield the same result.

- $\tuple{a,b} \tuplecat ((\tuple{c} \tuplecat \tuple{a,b}) \tuplecat \tuple{a,c,e}) = 
\tuple{a,b} \tuplecat (\tuple{c,a,b}\tuplecat \tuple{a,c,e}) = 
\tuple{a,b} \tuplecat \tuple{c,a,b,a,c,e} = 
\tuple{a,b,c,a,b,a,c,e}$
- $\tuple{a,b} \tuplecat \tuple{c}) \tuplecat (\tuple{a,b} \tuplecat \tuple{a,c,e}) =
\tuple{a,b,c} \tuplecat (\tuple{a,b} \tuplecat \tuple{a,c,e}) =
\tuple{a,b,c} \tuplecat \tuple{a,b,a,c,e} =
\tuple{a,b,c,a,b,a,c,e}$

:::

::: exercise
Write down all possible ways of obtaining $\tuple{a,b,c,d}$ via concatenation of tuples whose length is at least $1$.
For instance, one possible way is $\tuple{a,b} \tuplecat \tuple{c, d}$, but there's several more.
:::

::: solution
If one excludes the empty tuple $\tuple{}$, there are only finitely many options:

- $\tuple{a} \tuplecat \tuple{b} \tuplecat \tuple{c} \tuplecat \tuple{d}$
- $\tuple{a,b} \tuplecat \tuple{c} \tuplecat \tuple{d}$
- $\tuple{a} \tuplecat \tuple{b,c} \tuplecat \tuple{d}$
- $\tuple{a} \tuplecat \tuple{b} \tuplecat \tuple{c,d}$
- $\tuple{a,b} \tuplecat \tuple{c,d}$
- $\tuple{a,b,c} \tuplecat \tuple{d}$
- $\tuple{a} \tuplecat \tuple{b,c,d}$

If one allows the empty tuple, then there are infinitely many options, e.g.:

- $\tuple{a,b,c,d} \tuplecat \tuple{}$
- $\tuple{a,b,c,d} \tuplecat \tuple{} \tuplecat \tuple{}$
- and so on

:::

::: exercise
Tuple concatenation is not commutative.
That is to say, for some tuples $a$ and $b$ it is not the case that $a \tuplecat b = b \tuplecat a$.
Illustrate this with an example.
:::

::: solution
The simplest solution is $\tuple{a} \tuplecat \tuple{b} = \tuple{a,b} \neq \tuple{b,a} = \tuple{b} \tuplecat \tuple{a}$ (assuming $a \neq b$).
:::

::: exercise
Compute $\tuple{a} \tuplecat \tuple{}$ and $\tuple{} \tuplecat \tuple{a,a,a}$.
:::

::: solution

- $\tuple{a} \tuplecat \tuple{} = \tuple{a}$
- $\tuple{} \tuplecat \tuple{a,a,a} = \tuple{a,a,a}$

:::

::: exercise
What is the length of the following tuples?

- $\tuple{a,b,c}$
- $\tuple{a, \tuple{b,c}}$
- $\tuple{\tuple{a}, \tuple{b}, \tuple{c}}$
- $\tuple{\tuple{a,b,c}}$
- $\tuple{\tuple{}, \tuple{}, \tuple{}}$

:::

::: solution

- $\tuple{a,b,c}$ has length $3$
- $\tuple{a, \tuple{b,c}}$ has length $2$
- $\tuple{\tuple{a}, \tuple{b}, \tuple{c}}$ has length $3$
- $\tuple{\tuple{a,b,c}}$ has length $1$
- $\tuple{\tuple{}, \tuple{}, \tuple{}}$ has length $3$

:::

::: exercise
Does the concatenation of $\tuple{a,b}$ and $\tuple{c}$ yield the same result as the concatenation of $\tuple{a,b}$ and $\tuple{\tuple{c}}$?
Justify your answer!
:::

::: solution
No, they are distinct:

- $\tuple{a,b} \tuplecat \tuple{c} = \tuple{a,b,c}$
- $\tuple{a,b} \tuplecat \tuple{\tuple{c}} = \tuple{a,b,\tuple{c}}$

:::

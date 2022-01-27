## Range

For many functions it won't be the case that the every value in their domain is actually a possible output of a function.
Given a function $f: D \rightarrow C$, we use the term **range** to refer to the set of elements of $C$ that are an output for at least one input in $D$.

::: example
Consider the function $f: \mathbb{N} \rightarrow \mathbb{N}$ with $x \mapsto 2x$.
Not every natural number is a possible output of this function:

1. $f(0) = 0$
1. $f(1) = 2$
1. $f(2) = 4$
1. $f(3) = 6$
1. and so on

The range thus does not contain all members of $\mathbb{N}$.
Instead, it consists of all even natural numbers, and nothing else.
:::

::: example
Now suppose that we have $f: \mathbb{R} \rightarrow \mathbb{N}$ with $x \mapsto 2x$.
For every natural number $n$, $\frac{n}/2$ is a real number and thus an element of $\mathbb{R}$.
Hence it must be the case that for every natural number $n$ there is at least one element $e$ in the domain of $f$ such that $f(e) = n$.
So this is an example where a function's range is identical to its co-domain.
:::

::: exercise
For each one of the following functions, describe its range and say whether it is the same as the function's co-domain.
Justify your answer.
As in many other exercises, getting the correct answer is less important than giving a good argument for you answer.

1. $f: \mathbb{N} \rightarrow \mathbb{N}$, $x \mapsto x + 1$
1. $f: \mathbb{N} \rightarrow \mathbb{N}$, $x \mapsto x - 1$
1. $\mathrm{len}: \Sigma^* \rightarrow \mathbb{N}$ with $s \mapsto \length{s}$ (remember that $\length{s}$ denotes the length of string $s$)
1. the child-of kinship relation among humans, limited to women (for instance, $\mathrm{child}(\mathrm{Sue}) = \mathrm{Mary}$ iff Sue is a child of Mary)
1. a benchmark that sorts graphics card models by their speed for neutral network training

:::

## Range

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

::: solution
1. The range of $f$ is the set of positive natural numbers, which is distinct from the co-domain $\mathbb{N}$.
1. The range of $f$ is the same as the co-domain $\mathbb{N}$.
   For every $x \in \mathbb{N}$, there is some $y \in \mathbb{N}$ such that $y - 1 = x$.
   Hence the range is at least $\mathbb{N}$.
   Since $0 - 1 = -1$ is not a member of the co-domain $\mathbb{N}$, $f(0)$ is undefined and $-1$ is not part of the range of $f$.
1. For every natural number $n$ there is at least one string in $\Sigma^*$ whose length is $n$ (including the empty string $\emptystring$ with length 0).
   Hence the range of $\mathrm{len}$ is identical to its co-domain $\mathbb{N}$.
:::

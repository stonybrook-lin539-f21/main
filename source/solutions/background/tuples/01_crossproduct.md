# Crossproduct

::: exercise
Why shouldn't we use a set $\setof{s,c}$ instead of the pair $\tuple{s,c}$?
What might go wrong in this case depending on our choice of $S$ and $C$?
:::

::: solution
Suppose that we have a language where some color terms are also terms for shapes.
For example, *green* could also refer to an octagon.
Then sets won't always provide enough information to infer whether *green* specifies the color or a shape.

Or more formally:
Suppose $S \cap C$ contains at least two elements $x$ and $y$.
Then $\tuple{x,y} \neq \tuple{y,x}$ but $\setof{x,y} = \setof{y,x}$.
:::

::: exercise
Suppose $S$ consists of \emph{John}, \emph{Mary}, and \emph{the old man}, whereas $V$ contains only *slept* and *left*.
Compute $S \times V$.
:::

::: solution
The set $S \times V$ contains all of the following, and only those:

- $\tuple{\text{John}, \text{slept}}$
- $\tuple{\text{John}, \text{left}}$
- $\tuple{\text{Mary}, \text{slept}}$
- $\tuple{\text{Mary}, \text{left}}$
- $\tuple{\text{the old man}, \text{slept}}$
- $\tuple{\text{the old man}, \text{left}}$

:::

::: example
Now suppose that we also have a set $A \is \setof{ \text{awesome} }$.
Then $S \times C \times A$ would be a set containing the following triples:


- $\tuple{\text{square}, \text{blue}, \text{awesome}}$
- $\tuple{\text{circle}, \text{blue}, \text{awesome}}$
- $\tuple{\text{square}, \text{red},  \text{awesome}}$
- $\tuple{\text{circle}, \text{red},  \text{awesome}}$

:::

::: exercise
List all 8 members of $A \times C \times S \times A \times C \times A$.
:::

::: solution
With
$A \is \setof{ \text{awesome} }$,
$S \is \setof{ \text{square}, \text{circle} }$,
and
$C \is \setof{ \text{blue}, \text{red} }$,
the set $A \times C \times S \times A \times C \times A$ contains all of the following, and nothing else:

- $\tuple{\text{awesome}, \text{blue}, \text{circle}, \text{awesome}, \text{blue}, \text{awesome}}$
- $\tuple{\text{awesome}, \text{blue}, \text{circle}, \text{awesome}, \text{red}, \text{awesome}}$
- $\tuple{\text{awesome}, \text{blue}, \text{square}, \text{awesome}, \text{blue}, \text{awesome}}$
- $\tuple{\text{awesome}, \text{blue}, \text{square}, \text{awesome}, \text{red}, \text{awesome}}$
- $\tuple{\text{awesome}, \text{red}, \text{circle}, \text{awesome}, \text{blue}, \text{awesome}}$
- $\tuple{\text{awesome}, \text{red}, \text{circle}, \text{awesome}, \text{red}, \text{awesome}}$
- $\tuple{\text{awesome}, \text{red}, \text{square}, \text{awesome}, \text{blue}, \text{awesome}}$
- $\tuple{\text{awesome}, \text{red}, \text{square}, \text{awesome}, \text{red}, \text{awesome}}$

Or more succinctly:

- $\setof{\tuple{\text{awesome}, c_1, s, \text{awesome}, c_2, \text{awesome}} \mid c_1, c_2 \in C, s \in S}$

:::

::: exercise
In a certain sense, the crossproduct is the result of generalizing concatenation from tuples to sets of 1-tuples.
Explain why.
:::

::: solution
As defined, $A_1 \times A_2 \times \cdots \times A_n \is \setof{ \tuple{a_1, a_2, \ldots, a_n} \mid a_i \in A_i, 1 \leq i \leq n}$.
But $\tuple{a_1, a_2, \ldots, a_n} = \tuple{a_1} \tuplecat \tuple{a_2} \cdots \tuplecat \tuple{a_n}$.
Hence $A_1 \times A_2 \times \cdots \times A_n \is \setof{ \tuple{a_1} \tuplecat \tuple{a_2} \tuplecat \cdots \tuplecat \tuple{a_n} \mid a_i \in A_i, 1 \leq i \leq n}$.
If we assume that each $A_i$ is already a set of 1-tuples, then the set expression can be simplified to $\setof{ a_1 \tuplecat a_2 \tuplecat \cdots \tuplecat a_n \mid a_i \in A_i, 1 \leq i \leq n}$, which just combines the 1-tuples of these sets via concatenation.
:::

::: exercise
If $A$ has $m$ members and $B$ has $n$ members, then the number of tuples in $A \times B$ is $m$ multiplied by $n$.
Explain why.
:::

::: solution
Each tuple in $A \times B$ has two components.
Given some $a_i \in A$, we have one tuple $\tuple{a_i,b_j}$ for each $b_j \in B$.
Since $B$ has $n$ members, there are $n$ distinct tuples whose first component is $a_i$: $\tuple{a_i, b_1}, \ldots, \tuple{a_i, b_n}$.
But as $A$ contains $m$ elements, there are $m$ different choices for $a_i$, each one of which is the first component of $n$ distinct tuples.
Overall, then, there are exactly $m \times n$ tuples in $A \times B$.
:::

::: example
Let $A \is \setof{a,b,c}$, $B \is \setof{T,F}$, and $C \is \setof{1}$.
Then $A \times (B \times C)$ contains 6 pairs:


- $\tuple{a, \tuple{T,1}}$
- $\tuple{a, \tuple{F,1}}$
- $\tuple{b, \tuple{T,1}}$
- $\tuple{b, \tuple{F,1}}$
- $\tuple{c, \tuple{T,1}}$
- $\tuple{c, \tuple{F,1}}$


While $(A \times B) \times C$ also contains 6 pairs, they are different pairs:


- $\tuple{\tuple{a, T}, 1}$
- $\tuple{\tuple{a, F}, 1}$
- $\tuple{\tuple{b, T}, 1}$
- $\tuple{\tuple{b, F}, 1}$
- $\tuple{\tuple{c, T}, 1}$
- $\tuple{\tuple{c, F}, 1}$

:::

::: exercise
Continuing the previous example, list all elements of $A \times B \times C$.
Does this set also contain 6 tuples?
Are they also pairs?
:::

::: solution
Yes, it also contains 6 tuples, but they are triples, not pairs.

- $\tuple{a, T, 1}$
- $\tuple{a, F, 1}$
- $\tuple{b, T, 1}$
- $\tuple{b, F, 1}$
- $\tuple{c, T, 1}$
- $\tuple{c, F, 1}$

:::

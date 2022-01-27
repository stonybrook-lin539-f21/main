**Prerequisite**

- Tuples (basics)

# Crossproduct

One often wants to define an entire set of tuples.
This can be done with set-builder notation.

::: example
Let $N$ be a set of names and $P$ a set of phone numbers.
Then we might define an address book as the set
$$
A \is \setof{ \tuple{n, p} \mid n \in N, p \in P, \text{ and } p  \text{ is } n \text{'s phone number}}
$$
:::

But when we want to allow all possible combinations, there is an easier option.
Consider the colored objects depicted below:

~~~ {.include-tikz size=mid}
shapes.tikz
~~~

We can represent each object as a pair $\tuple{s,c}$ where $s$ and $c$ are drawn from a set $S \is \setof{\text{square}, \text{circle}}$ of shapes and a set $C \is \setof{\text{blue}, \text{red}}$ of colors, respectively.
The figure above contains every possible combination of those shapes and colors.
We can still use set-builder notation in this case: $\setof{ \tuple{s,c} \mid s \in S, c \in C}$.

::: exercise
Why shouldn't we use a set $\setof{s,c}$ instead of the pair $\tuple{s,c}$?
What might go wrong in this case depending on our choice of $S$ and $C$?
:::

A more elegant alternative to set-builder notation, however, is the **crossproduct** or **Cartesian product**.

::: definition
For any two sets $S$ and $T$, their crossproduct $S \times C$ is defined as $\setof{ \tuple{s,c} \mid s \in S, c \in C}$.
In general, $A_1 \times A_2 \times \cdots \times A_n \is \setof{ \tuple{a_1, a_2, \ldots, a_n} \mid a_1 \in A_1, a_2 \in A_2, \ldots, a_n \in A_n}$.
:::

::: example
For $S \is \setof{\text{square}, \text{circle}}$ and $C \is \setof{\text{blue}, \text{red}}$, $S \times C$ contains the pairs 


- $\tuple{\text{square}, \text{blue}}$
- $\tuple{\text{circle}, \text{blue}}$
- $\tuple{\text{square}, \text{red}}$
- $\tuple{\text{circle}, \text{red}}$


This is different from $C \times S$, which contains


- $\tuple{\text{blue}, \text{square}}$
- $\tuple{\text{blue}, \text{circle}}$
- $\tuple{\text{red}, \text{square}}$
- $\tuple{\text{red}, \text{circle}}$

:::

::: exercise
Suppose $S$ consists of \emph{John}, \emph{Mary}, and \emph{the old man}, whereas $V$ contains only *slept* and *left*.
Compute $S \times V$.
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

::: exercise
In a certain sense, the crossproduct is the result of generalizing concatenation from tuples to sets of 1-tuples.
Explain why.
:::

::: exercise
If $A$ has $m$ members and $B$ has $n$ members, then the number of tuples in $A \times B$ is $m$ multiplied by $n$.
Explain why.
:::

::: remark
The name Cartesian product makes more sense if you consider the special case of $\mathbb{N} \times \mathbb{N}$.
Here $\mathbb{N} \is \setof{0, 1, 2, 3, \ldots}$ is the set of all natural numbers.
So $\mathbb{N} \times \mathbb{N}$ is the set of all possible pairs of natural numbers.
We can take these two components to represent $(x,y)$-coordinates in the upper right quadrant of a coordinate system.
Such a coordinate system is also called a **Cartesian plane**, and that is why the crossproduct is sometimes called the Cartesian product.
:::

Just like tuple concatenation, the crossproduct operation is not commutative.

::: example
Let $A \is \setof{a,b}$ and $B \is \setof{1}$.
Then $A \times B = \setof{ \tuple{a,1}, \tuple{b,1}}$ whereas $B \times A = \setof{ \tuple{1,a}, \tuple{1,b} }$.
:::

But whereas tuple concatenation is associative, the crossproduct operation is not.
Most of the time, $A \times B \times C$ and $A \times (B \times C)$ and $(A \times B) \times C$ yield different results.

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


## Recap

- The crossproduct (or Cartesian product) generalizes concatenation from tuples to sets:
  $$A_1 \times A_2 \times \cdots \times A_n \is \setof{ \tuple{a_1, a_2, \ldots, a_n} \mid a_1 \in A_1, a_2 \in A_2, \ldots, a_n \in A_n}$$
- The crossproduct operation is not commutative.
  Never confuse $A \times B$ and $B \times A$.
- The crossproduct operation is not associative.
  Never confuse $A \times B \times C$, $A \times (B \times C)$, and $(A \times B) \times C$.

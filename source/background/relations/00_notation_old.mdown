**Prerequisite**

- tuples (basics)

# Relations

Relations are similar to functions in that they establish connections between objects.
But whereas a function associates only one output with every input, a relation is more flexible and allows connections to arbitrarily many elements.

::: example
The question *Is $x$ a biological child of $y$* is a function because it maps any two $x$ and $y$ to either true or false, but never both.
But if we slightly change the question to just *Name a biological child of $y$*, we are no longer dealing with a function because multiple answers are possible if $y$ has more than one child.
Instead, we can talk about the *biological child* relation $R$ such that $x$ is related to $y$ via $R$ iff $x$ is a biological child of $y$.
:::

## Intuition

::: example
Suppose *John* has exactly two siblings, *Mary* and *Sue*.
Then the sibling relation establishes two connections for John: *John*-*Mary*, and *John*-*Sue*.
This is commonly encoded as tuples: $\tuple{\text{John}, \text{Mary}}$ and $\tuple{\text{John}, \text{Sue}}$.
For this particular family, the whole sibling relation can be represented as a set of pairs $\tuple{x,y}$ such that $x$ is the sibling of $y$:
$$
\setof{ \tuple{x,y} \mid x,y \in \setof{\text{John}, \text{Mary}, \text{Sue}}, \text{ and } x \neq y}
$$
:::

::: example
The **substring relation** $\sqsubseteq$ holds between two strings $u$ and $v$ iff $u$ is a substring of $v$.
That is to say, there are $w, w' \in \Sigma^*$ such that $w \stringcat u \stringcat w' = v$.
Note that for any given string $u$, there are infinitely many $v$ that $u$ is a substring of.
Even if the alphabet contains only $a$, the string $aa$ is a substring of $aaa$, $aaaa$, $aaaaa$, and so on, ad infinitum.
It is also a substring of itself (in this case, $w = w' = \emptystring$).
:::

::: example
Just like a function can take multiple arguments to return a single output, a relation can connect multiple elements.
In the real world, the "jointly conceived" relation would connect two individuals to their offspring.
So $\tuple{\text{John}, \text{Mary}, \text{Sue}}$ encodes that John and Mary are the biological parents of Sue (let's just hope that those are not the same people as in the first example).
:::

## Definition and notation

::: definition
A **relation** is a (possibly empty, possibly infinite) set of $n$-tuples.
:::

We will mostly be dealing with the special case of **binary relations**, where $n = 2$.
Given a binary relation $R$, $a \mathrel{R}$ and $\mathrel{R} b$ are sets of objects related to $a$ and $b$, respectively:
$$
a \mathrel{R} \is \setof{ b \mid \tuple{a,b} \in R}
$$
$$
\mathrel{R} b \is \setof{ a \mid \tuple{a,b} \in R}
$$

::: example
Suppose that the parent-of relation $P$ contains only the pairs
$\tuple{\text{John}, \text{Sue}}$
and
$\tuple{\text{Mary}, \text{Sue}}$.
Then $\text{John} \mathrel{P} = \setof{\text{Sue}}$ and $\mathrel{P} \text{Sue} = \setof{ \text{John}, \text{Mary}}$.
:::

::: exercise
Let $R$ be the relation that connects words to their parts of speech (N for nouns, V for verbs, A for adjectives, P for prepositions, D for determiners, and so on).
List the following for English:


- export $R$
- apple $R$
- $R$ P

:::

## Relations versus functions

Every function can be regarded as a relation.

::: example
Consider the function $f: \mathbb{N} \rightarrow \mathbb{N}$ with $x \mapsto 2x$.
It is identical to the relation $\setof{ \tuple{x, 2x} \mid x \in \mathbb{N}}$.
:::

The crucial difference is that functions are **right-unique relations**.
That is to say, it holds for every $a$ that $a \mathrel{R}$ is either empty or contains exactly one element.

::: exercise
For each one of the following, say whether it is a function or just a relation.


- the parent-of relation
- the parent-of relation in a world where the one-child policy is enforced globally
- the relation between a car's license plate and its owners
- the prefix relation, where $u$ is a prefix of $v$ iff there is some $w \in \Sigma^*$ such that $v = u \stringcat w$

:::

::: exercise
Is the following statement true or false?
Justify your answer.


Every relation $R$ can be regarded as a function that maps $x$ to $x \mathrel{R}$.
:::


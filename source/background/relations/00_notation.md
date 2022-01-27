**Prerequisite**

- functions (basics)

# Relations

Relations are similar to functions in that they establish connections between objects.
But whereas a function associates only one output with every input, a relation is more flexible and allows connections to arbitrarily many elements.

::: example
The question *Is $x$ a biological child of $y$* is a function because it maps any two $x$ and $y$ to either true or false, but never both.
But if we slightly change the question to just *Name a biological child of $y$*, we are no longer dealing with a function because multiple answers are possible if $y$ has more than one child.
Instead, we can talk about the *biological child* relation $R$ such that $x$ is related to $y$ via $R$ iff $x$ is a biological child of $y$.
:::


## Basic notation

Given some relation $R$, we write $x \mathrel{R} y$ to indicate that $R$ relates $x$ to $y$.
Note that $x \mathrel{R} y$ does not imply that $y \mathrel{R} x$ also holds, nor that it doesn't hold.

::: example
One relation you know very well is the "less than" relation $<$ over numbers.
When we write $5 < 7$, we are saying that the relation $<$ relates $5$ to $7$.
However, it is not the case that $7$ is related to $5$ via $<$, since $7 < 5$ does not hold.
:::

::: example
Suppose *John* has exactly two siblings, *Mary* and *Sue*.
Then the sibling relation establishes two connections for John: *John*-*Mary*, and *John*-*Sue*.
Using $S$ for the sibling relation, we have
$\text{John} \mathrel{S} \text{Mary}$
and
$\text{John} \mathrel{S} \text{Sue}$.

In contrast to $<$, the sibling relation is **symmetric**.
That is to say, if Mary is a sibling of John, then John is also a sibling of Mary.
Therefore we also have
$\text{Mary} \mathrel{S} \text{John}$
and
$\text{Sue} \mathrel{S} \text{John}$.

The relation is also **transitive**.
If John is a sibling of Mary, and Sue is a sibling of John, then Sue is a sibling of Mary.
So is also holds that $\text{Mary} \mathrel{S} \text{Sue}$, and via symmetry we also get $\text{Sue} \mathrel{S} \text{Mary}$.

Overall, we have $x \mathrel{S} y$ where $x, y \in \setof{\text{John}, \text{Mary}, \text{Sue}}$ and $x \neq y$.
:::

::: example
The **substring relation** $\sqsubseteq$ holds between two strings $u$ and $v$ iff $u$ is a substring of $v$.
That is to say, $u \subseteq v$ iff there are $w, w' \in \Sigma^*$ such that $w \stringcat u \stringcat w' = v$.
Note that for any given string $u$, there are infinitely many $v$ that $u$ is a substring of.
Even if the alphabet contains only $a$, the string $aa$ is a substring of $aaa$, $aaaa$, $aaaaa$, and so on, ad infinitum.
It is also a substring of itself (in this case, $w = w' = \emptystring$).
:::

::: example
Relations can be defined over more complex objects like sets.
An example of this is the subset relation $\subseteq$.
The set $\setof{1}$ is a subset of infinitely many other sets: $\setof{0,1}$, $\setof{1,2}$, $\setof{0,1,2}$, $\setof{1,3}$, and so on.
:::

::: example
Just like a function can take multiple arguments to return a single output, a relation can connect multiple elements.
In the real world, the "jointly conceived" relation $J$ would connect two individuals to their offspring.
So the expression
$$\text{John}, \text{Mary} \mathrel{R} \text{Sue}$$
encodes that John and Mary are the biological parents of Sue (let's just hope that those are not the same people as in the first example).
:::

::: example
Here is an example of a very abstract relation.
Consider the space of all possible functions from real numbers to real numbers --- that's a lot of functions.
Now let's define a boundedness relation $B$ which relates function $f$ to function $g$ iff $f(x) \leq g(x)$ for every natural number $x$.
Suppose, for instance, that $f(x) = x$ and $g(x) = x^2$.
Then $f \mathrel{B} g$, but not $g \mathrel{B} f$.

Many functions aren't related via $B$ at all.
One example of this is $f(x) = -x + 1$ and $g(x) = x^2$.
It is the case that $f(x) \leq g(x)$ for all $x \geq 1$, but $f(0) = 1 > 0 = g(0)$.
:::

We will mostly be dealing with the special case of **binary relations** where exactly one element is related to some other element.

::: example
Almost all relations above are binary relations.
The only exception is the "jointly conceived" relation $J$, which is a ternary relation as it relates three elements.
:::

Given a binary relation $R$, $a \mathrel{R}$ is the set of objects that $a$ is related to.
Similarly, $\mathrel{R} b$ is the set of objects that are related to $b$.
$$
a \mathrel{R} \is \setof{ b \mid a \mathrel{R} b}
$$
$$
\mathrel{R} b \is \setof{ a \mid a \mathrel{R} b}
$$

::: example
Suppose that the parent-of relation $P$ establishes the following relations between elements:
$\text{John} \mathrel{P} \text{Sue}$
and
$\text{Mary} \mathrel{P} \text{Sue}$.
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
It is identical to the relation $R$ with $x \mathrel{R} y$ iff $y = 2x$.
:::

The crucial difference between functions and relations is that functions are **right-unique relations**.
That's a fancy way of saying that a function cannot provide more than one output, whereas a relation can unless it is right-unique.
When we view a function $f$ as a relation $R$, then it must hold for every $a$ that $a \mathrel{R}$ is either empty or contains exactly one element.
Hence the term right-unique: if we look at the expression $a \mathrel{R} b$, $a$ is the left side and $b$ the right side.
If there cannot be more than one choice for $b$, then the right side of $a \mathrel{R} b$ is uniquely determined.

The bottom line: every function is a relation, but not every relation is a function.
If $a$ is related to two elements or more (i.e. $\card{a \mathrel{R}} \geq 2$), then $R$ cannot be a function.

::: exercise
For each one of the following, say whether it is a function or just a relation.

- the parent-of relation (e.g. $j \mathrel{P} m$ for "John is a parent of Mary")
- the parent-of relation in a world where the one-child policy is enforced globally
- the relation between a car's license plate and its owners
- the prefix relation, where $u$ is a prefix of $v$ iff there is some $w \in \Sigma^*$ such that $v = u \stringcat w$

:::

::: exercise
Is the following statement true or false?
Justify your answer.

Every relation $R$ can be regarded as a function that maps $x$ to $x \mathrel{R}$.
:::

## Recap

- Relations are a generalization of functions in that a single input can be related to many distinct outputs.
- Given some relation $R$, we write $x \mathrel{R} y$ to indicate that $R$ relates $x$ to $y$.
- We mostly focus on binary relations.
- For binary relations, we have the following notation:
$$
a \mathrel{R} \is \setof{ b \mid a \mathrel{R} b}
$$
$$
\mathrel{R} b \is \setof{ a \mid a \mathrel{R} b}
$$

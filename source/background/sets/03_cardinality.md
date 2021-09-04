**Prerequisites**

- sets (notation, operations)
- functions (basic notation, domain terminology)

# Cardinality

Sets can be compared based on how many elements they contain.

::: example
The set $A \is \setof{a,b,c}$ contains exactly as many elements as the set $X \is \setof{x,y,z}$, namely $3$.
Each set has fewer members than $A \cup X$, which contains $6$ elements, whereas $A \cap X$ has $0$ members.
:::

This is commonly called the **size** of a set, but the more accurate term is **cardinality**.
The cardinality of a set $A$ is denoted $\card{A}$.
We say that $\card{A} \leq B$ iff there is a function $f$ such that every element of $A$ is mapped to some element of $B$ and every element of $B$ has at most one element of $A$ mapped to it.

::: example
Suppose that $A \is \setof{a,b,c}$ and $D \is \setof{d,e,f,g}$.
Then $\card{A} \leq \card{D}$, as every element of $A$ can be mapped to some distinct element of $D$.
For instance, we could have a function with
$a \mapsto f$,
$b \mapsto d$,
$c \mapsto g$.

In the other direction, $\card{D} \not\leq \card{A}$.
No matter how one maps the elements of $D$ to members of $A$, at least two members of $D$ will have to be mapped to the same element in $A$.
:::

Clearly $\card{A} = \card{B}$ iff $\card{A} \leq \card{B}$ and $\card{B} \leq \card{A}$ are both true.
But there is a more direct definition:
$\card{A} = \card{B}$ iff there is a function $f$ such that $f$ maps every element of $A$ to some element of $B$ and every element of $B$ has exactly one element of $A$ mapped to it.
We also say that there is a **bijection** between $A$ and $B$, which is a technical term for a 1-to-1 correspondence between the elements of $A$ and $B$.

::: example
We already saw that $\card{A} = \card{X}$ in the previous example.
A possible choice of $f$ would be
$a \mapsto x$,
$b \mapsto y$,
$c \mapsto z$.
:::

::: example
The sets $A \is \setof{0,1,2}$ and $B \is \setof{2,3}$ obviously have distinct cardinality.
The set $A$ contains 3 elements, the set $B$ only 2.
But let us see how we get the same result via our mathematical definition.

Suppose we have some arbitrary function $f: A \rightarrow B$.
If $f$ is a bijection, then it must map every element of $A$ to some element of $B$.
But since there are three elements in $A$ and only two in $B$, some element of $B$ must be the output for at least two elements of $A$.
But then $f$ is not a bijection.

In the other direction, consider some arbitrary function $g: B \rightarrow A$.
Since a function maps each input to at most one output, the two elements of $B$ are mapped to at most two elements of $A$.
But $A$ has three elements, so one element of $A$ cannot be an output for any element of $B$.
Again we find that $g$ cannot be bijection.

This exhausts all cases we need to consider, and we may conclude that no function from $A$ to $B$, or the other way round, can be a bijection.
Hence $A$ and $B$ must have distinct cardinality.
:::

::: exercise
Show that
$\card{\setof{ 0 \leq n < 10 \mid n \text{ is odd}} = \card{\setof{ 0 \leq n < 10 \mid n \text{ is even}}}}$.
:::

For finite sets, our intuitive notion of size closely matches the technical term of cardinality.
However, size and cardinality diverge once we look at infinite sets.

::: example
Consider the set $\mathbb{N} \is \setof{0,1,2,\ldots}$ of all natural numbers and the set $\mathbb{N}_+ \is \setof{1,2,\ldots}$ of all positive natural numbers.
Intuitively, $\mathbb{N}$ is larger than $\mathbb{N}_+$ because it contains all members of $\mathbb{N}_+$ as well as 0, which is not in $\mathbb{N}_+$.
But the function $f: \mathbb{N} \rightarrow \mathbb{N}_+$ with $n \mapsto n+1$ is a bijection.
Hence $\card{\mathbb{N}} = \card{\mathbb{N}_+}$ even though intuitively the two sets have distinct size.
:::

::: exercise
Show that the set of natural numbers has the same cardinality as the set of all even natural numbers.
:::

In a later unit, we will see that our definition of cardinality entails that there are different "sizes" of infinity, and that we want one specific infinity size to talk about language.

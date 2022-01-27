# Lower bounds and upper bounds

::: exercise
Draw corresponding diagrams indicating the upper and lower bounds of

- $\setof{1,3}$
- $\emptyset$

:::

::: solution
fixme: typeset this
:::

::: exercise
Say whether the following is true or false, and justify your answer:
if $\tuple{S, \leq}$ is a poset, then it holds for all $x, y \in S$ that $y$ is both an upper and a lower bound for $x$ iff $x = y$.
:::

::: solution
This statement is true.
If $y$ is an upper bound for $x$, then $x \leq y$, and if $y$ is a lower bound for $x$, then $y \leq x$.
Since $\leq$ is a partial order, and thus antisymmetric, $x \leq y$ and $y \leq x$ jointly imply $x = y$.
:::

::: exercise
Given some arbitrary poset $\tuple{S, \leq}$, what are $\mathrm{lb}(\emptyset)$ and $\mathrm{ub}(\emptyset)$?
Justify your answer.
:::

::: solution
By definition, $\mathrm{lb}(A)$ contains every $x$ such that $x \leq y$ is true for all $y \in A$.
But if $A$ is empty, then this condition is trivially satisfied --- for any arbitrary $x$, there is no $y \in A$ such that $x \leq y$ is false.
Hence $\mathrm{lb}(\emptyset) = S$.
For the same reason, it is also the case that $\mathrm{ub}(\emptyset) = S$.
:::

::: exercise
Explain why the set of upper bounds of some element $x$ of a poset is identical to $\mathrm{ub}(\setof{x})$.
:::

::: solution
Given some element $x$ of some poset $\tuple{S, \leq}$, its set of upper bounds is defined as $\setof{y \in S \mid x \leq y}$.
And for every subset $A$ of $S$,
$\mathrm{ub}(A) \is \setof{ y \in S \mid z \leq y \text{ for all } z \in A}$.
If $A \is \setof{x}$, then this definition reduces to
$\mathrm{ub}(A) \is \setof{ y \in S \mid z \leq y \text{ for all } z \in \setof{x}}$,
which is equivalent to
$\mathrm{ub}(A) \is \setof{ y \in S \mid x \leq y}$.
But as we saw before, this is the set of upper bounds of $x$.
:::

::: example
One more example with the same poset.
The upper bounds of $\setof{2}$, $\setof{3}$, and $\setof{2,3}$ are $\setof{2,3}$ and $\setof{1,2,3}$, whereas their only lower bound is $\emptyset$.
We write this more succinctly as
$\mathrm{ub}(\setof{\setof{2}, \setof{3}, \setof{2,3}}) = \setof{\setof{2,3} \setof{1,2,3}}$ and 
$\mathrm{lb}(\setof{\setof{2}, \setof{3}, \setof{2,3}}) = \setof{\emptyset}$.
Once again we can also depict this in the graphical format: 

~~~ {.include-tikz size=mid}
lattice_123_bounds2-3-23.tikz
~~~
:::

::: solution
Given the poset in the previous example, compute all of the following:


- $\mathrm{ub}(\setof{\setof{1,2}, \setof{2,3}}) = \setof{ \setof{ 1,2,3 } }$
- $\mathrm{lb}(\setof{\setof{1,2}, \setof{2,3}}) = \setof{ \setof{2}, \emptyset }$
- $\mathrm{ub}(\setof{\emptyset}) = \setof{ \emptyset, \setof{1}, \setof{2}, \setof{3}, \setof{1,2}, \setof{1,3}, \setof{2,3}, \setof{1,2,3} }$
- $\mathrm{ub}(\emptyset) = \setof{ \emptyset, \setof{1}, \setof{2}, \setof{3}, \setof{1,2}, \setof{1,3}, \setof{2,3}, \setof{1,2,3} }$
- $\mathrm{lb}(\setof{\emptyset, \setof{1,2,3}}) = \setof{ \emptyset }$
- $\mathrm{lb}(\setof{\setof{1}, \setof{2,3}, \setof{1,2,3}}) = \setof{ \emptyset }$
- $\mathrm{ub}(\setof{\setof{1}, \setof{2}, \setof{3}}) = \setof{ \setof{1,2,3} }$

:::

::: exercise
Consider $\tuple{\setof{0,1,2,3,4}, \leq}$, the set of the first five natural numbers ordered in the usual fashion via $\leq$.
Using the pictorial format described above, indicate the lower and upper bounds for the following subsets:

- $\setof{2}$
- $\setof{1,4}$
- $\setof{2,3}$
- $\setof{0,3}$

:::

::: solution
fixme: typeset this
:::

::: exercise
Since $\mathrm{lb}$ and $\mathrm{ub}$ are functions from sets to sets, the output of one can be the input for the other.
Compute $\mathrm{lb}(\mathrm{ub}({\setof{0,3})})$ over $\setof{0,1,2,3,4}$ ordered by $\leq$.
By comparison, what is $\mathrm{ub}(\mathrm{lb}(\setof{0,3}))$?
:::

::: solution

- $\mathrm{lb}(\mathrm{ub}(\setof{0,3})) = \mathrm{lb}(\setof{3}) = \setof{3}$
- $\mathrm{ub}(\mathrm{lb}(\setof{0,3})) = \mathrm{ub}(\setof{0}) = \setof{0}$

:::

::: exercise
Now consider $\tuple{\mathbb{N}, \leq}$ instead, the set of all natural numbers ordered via $\leq$.
For each one of the following statements, say whether it is true or false and justify your answer.


- Any two natural numbers $x$ and $y$ have infinitely many upper bounds.
- Any two natural numbers $x$ and $y$ have infinitely many lower bounds.

:::

::: solution
The first statement is true, the second one is false.

For any two natural numbers $x$ and $y$ such that $x \leq y$, $\mathrm{ub}(\setof{x,y}) = \setof{ z \in \mathbb{N} \mid y \leq z}$.
But irrespective of how we choose $y$, there are infinitely many $z \in \mathbb{N}$ such that $z \geq y$.

With $x$ and $y$ as before, it also holds that $\mathrm{lb}(\setof{x,y}) = \setof{ z \in \mathbb{N} \mid z \leq x}$.
But for any $x \in \mathbb{N}$, there are exactly $x+1$ elements $z \in \mathbb{N}$ such that $z \leq x$.
Hence $\mathrm{lb}(\setof{x,y})$ is finite for any choice of $x$ and $y$.
:::

::: exercise
You might think that the poset in the previous example is somehow defective or pathological because no element is related to any element except itself.
But that's not really the issue, as is witnessed by the structure below.

~~~ {.include-tikz size=mid}
poset_nobounds.tikz
~~~

Find the smallest subset $S$ such that $\mathrm{ub}(S) = \emptyset$ and $\mathrm{lb}(S) = \emptyset$.
:::

::: solution
The smallest subset is $\setof{a,b,d,e}$.
This is because $\mathrm{lb}(\setof{a,b}) = \emptyset$, and if $\mathrm{lb}(A) = \emptyset$ for some subset $A$, then $\mathrm{lb}(B) = \emptyset$ for every $B \supseteq A$.
Similarly, $\mathrm{ub}(\setof{d,e}) = \emptyset$, and if $\mathrm{ub}(A) = \emptyset$ for some subset $A$, then $\mathrm{ub}(B) = \emptyset$ for every $B \supseteq A$.

Every proper subset of $\setof{a,b,d,e}$ has a non-empty set of upper bonds, a non-empty set of lower bounds, or both.
:::

::: exercise
Say whether the following is true or false, and justify your answer:

Given some poset $\tuple{S, \leq}$, it holds for every finite subset $\setof{s_1, \ldots, s_n}$ of $S$ that
$$\mathrm{ub}(\setof{s_1, \ldots, s_n}) = \mathrm{ub}(\setof{s_1}) \cap \mathrm{ub}(\setof{s_2} \cap \cdots \cap \mathrm{ub}(\setof{s_n})$$
:::

::: solution
This statement is true.
In order to show this, we use the fact that for any two sets $A$ and $B$, $A = B$ iff $A \subseteq B$ and $B \subseteq A$.

First, it must be the case that
$$\mathrm{ub}(\setof{s_1, \ldots, s_n}) \subseteq \mathrm{ub}(\setof{s_1}) \cap \mathrm{ub}(\setof{s_2} \cap \cdots \cap \mathrm{ub}(\setof{s_n})$$.
If $x \in \mathrm{ub}(\setof{s_1, \ldots, s_n})$, then $s_i \leq x$ for every $1 \leq i \leq n$.
But then it is also the case that $x \in \mathrm{ub}(\setof{s_i})$ for every $1 \leq i \leq n$, which in turn implies that $x$ belongs to the intersection of all $\mathrm{ub}(\setof{s_i})$.

It is also true that
$$\mathrm{ub}(\setof{s_1, \ldots, s_n}) \supseteq \mathrm{ub}(\setof{s_1}) \cap \mathrm{ub}(\setof{s_2} \cap \cdots \cap \mathrm{ub}(\setof{s_n})$$.
The intersection of all $\mathrm{ub}(\setof{s_i})$ contains $x$ iff $x$ is a member of each $\mathrm{ub}(\setof{s_i})$ ($1 \leq i \leq n$).
Hence $x \geq s_i$ for every $1 \leq i \leq n$.
But then, by definition, $x \in \mathrm{ub}(\setof{s_1, \ldots, s_n)}$.
:::

::: exercise
Say whether the following is true or false, and justify your answer:

Given some poset $\tuple{S, \leq}$, it holds for every finite subset $\setof{s_1, \ldots, s_n}$ of $S$ that
$$\mathrm{lb}(\setof{s_1, \ldots, s_n}) = \mathrm{lb}(\setof{s_1}) \cup \mathrm{lb}(\setof{s_2} \cup \cdots \cup \mathrm{lb}(\setof{s_n})$$
:::

::: solution
This statement is false, as can be shown with a single counterexample.
Consider the poset **2** of truth values, with carrier $S \is \setof{T, F}$ and $F \leq T$.
Then $\mathrm{lb}(\setof{T}) \cup \mathrm{lb}(\setof{F}) = \setof{T,F} \cup \setof{F} = \setof{T,F} \neq \setof{F} = \mathrm{lb}(\setof{T,F})$.
:::

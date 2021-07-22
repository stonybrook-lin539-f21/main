# Semigroups, monoids, and groups

Remember that a magma is a (total) algebra whose carrier set is closed under the algebra's operation $\oplus$.
By adding on additional properties that $\oplus$ must satisfy, one gets a hierarchy of increasingly specialized types of algebras:

| **Property**                             | **Algebra type** |
| :--                                      | :--              |
| $\oplus$ total                           | total algebra    |
| previous & closure under $\oplus$        | magma            |
| previous & associativity of $\oplus$     | semigroup        |
| previous & identity element for $\oplus$ | monoid           |
| previous & inverse for $\oplus$          | group            |
| previous & commutativity of $\oplus$     | Abelian group    |

## Semigroups

The next step up from a magma is a semigroup, which requires $\oplus$ to be associative.

::: definition
A (total) magma $\tuple{C, \oplus}$ is a **semigroup** iff $\oplus$ is associative.
:::

Remember that associativity means $a \oplus (b \oplus c) = (a \oplus b) \oplus c$.
So order of evaluation does not matter.
This is a tremendous advantage.
Associativity can greatly simplify proofs, and it also allows for faster computational implementations (see, for instance, the unit on matrix multiplication).

::: example
The magma $\tuple{\mathbb{N}, +}$ is a semigroup because addition is associative.
:::

::: example
The total algebra $\tuple{\mathbb{Z}, -}$ is the set of integers with subtraction.
This is a magma but not a semigroup because $5 - (3 - 2) = 4 \neq 0 = (5 - 3) - 2$.
:::

::: exercise
For each one of the following, say whether it is a semigroup.
Justify your answer.


- the interval $[0,1]$ of real numbers between and including $0$ and $1$, with multiplication
- for any given set $S$, $\wp(S)$ with set union (where $\wp(S)$ is the powerset of $S$)
- for any given set $s$, $\wp(S)$ with relative complement
- $\Sigma^*$ with an operation *splice* that maps two strings $u_1 u_2 \cdots u_m$ and $v_1 v_2 \cdots v_n$ ($m, n \geq 0$) to $u_1 v_1 u_2 v_2 \cdots u_x v_x$, where $x \is \min(m,n)$ (for instance, $abc$ spliced with $defghij$ is $adbecf$, and $abcdefg$ spliced with $i$ is $ai$).

:::

## Monoid

For computational linguistics, the most important kind of algebraic structure is the monoid.
A monoid is a semigroup with a unique **identity element** for $\oplus$.
An identity element is something that causes $\oplus$ not to change the value of the other argument.

::: example
Addition has $0$ as its identity element.
For instance, $5 + 0 = 5$, and similarly $0 + 5 = 5$.
So adding the identity element to some natural number $n$ just gives us $n$ again.


For multiplication, the identity element is $1$ as $5 \times 1 = 1 \times 5 = 5$.
:::

::: exercise
What is the identity element for set union?
Justify your answer.
:::

::: definition
A semigroup $\tuple{C, \oplus}$ is a **monoid** $\tuple{C, \oplus, e}$ iff there is a unique element $e \in C$ such that for all $a \in C$, $a \oplus e = e \oplus a = a$.
We say that $e$ is the **identity element** for $\oplus$, and that $\oplus$ **has an identity (element)**.
:::

::: example
We already know that addition has the identity element $0$, so it's not surprising that the semigroup $\tuple{\mathbb{N}, +}$ is also a monoid.
We can simply write $\tuple{\mathbb{N}, +, 0}$ to express this fact.
:::

::: example
The minimally different algebra $\tuple{\mathbb{N}^+, +}$ is a semigroup, but not a monoid.
That's because $\mathbb{N}^+ \is \setof{1,2,3,\ldots}$ is the set of positive natural numbers, which excludes $0$. 
Therefore, the algebra lacks the required identity element.
:::

::: exercise
For each one of the following semigroups, say whether it is a monoid.
Justify your answer.


- $\tuple{\wp(S), \cap}$ (where $S$ is some arbitrary set)
- $\Sigma^+$ with string concatenation
- the set of all strings of even length with string concatenation
- a semilattice

:::

A special case of the monoid is the **commutative monoid**, where $\oplus$ is also commutative.
This means that $a \oplus b = b \oplus a$.

::: example
The natural numbers with addition are a commutative monoid.
While $\Sigma^*$ with concatenation is a monoid (with identity element $\emptystring$), it is not a commutative monoid as $a \stringcat b = ab \neq ba = b \stringcat a$.
:::

::: exercise
Actually, there are special cases where $\tuple{\Sigma^*, \stringcat}$ is a commutative monoid.
Describe one of these special cases.
:::

## Group

Perhaps the most studied and best understood kind of algebraic object is the group.
A group is a monoid where every element also has an inverse.
An element and its inverse are like polar opposites that cancel each other out to yield the identity element.

::: definition
A monoid $\tuple{C, \oplus}$ is a **group** iff there for every $a \in C$ there is an element $\inv{a} \in C$ such that $a \oplus \inv{a} = e$.
We say that $\inv{a}$ is the **inverse** of $a$, and that $\oplus$ has an inverse for every element of the carrier $C$.
As $e$ is unique, we can add it directly to the specification: $\tuple{C, \oplus, e}$.
:::

::: example
The monoid $\tuple{\mathbb{N}, +, 0}$ is not a group.
Consider any arbitrary $n \in \mathbb{N}$.
There is no natural number $x$ such that $n + x = 0$.
:::

::: example
The monoid $\tuple{\mathbb{Z}, +, 0}$ is a group.
For every integer $n$, its inverse with respect to addition is $-n$.
For instance, $5 + (-5) = 5 - 5 = 0$, and $-3 + (- (- 3)) = -3 + 3 = 0$.
:::

While groups are mathematicians' darling, they show up much less in linguistics and are mostly listed here for the sake of completeness.
That said, there are some promising attempts to find group-like mechanisms in language, so a few years from now groups might be just as important as monoids.

::: exercise
For each one of the following monoids, say whether it is a group.
Justify your answer.


- $\tuple{\mathbb{N}, \times, 1}$
- $\tuple{\mathbb{Q}, \times, 1}$ (where $\mathbb{Q}$ is the set of rationals; e.g. $\frac{3}{2} \times \frac{-2}{2}$)
- $\Sigma^{\geq 3} \cup \setof{\emptystring}$ with concatenation and identity element $\emptystring$ ($\Sigma^{\geq 3}$ contains all $\Sigma$-strings whose length is at least $3$)
- $\wp(\Sigma^*)$ with union

:::

::: example
The monoid $\tuple{\Sigma^*, \stringcat, \emptystring}$ is not a group because there are no inverses.
No matter what one concatenates a string $u$ with, it won't reduce $u$ to $\emptystring$.
But if one really wants the monoid to be a group, one can stipulate the existence of such inverses.


For any string $u$ let $\overline{u}$ be such that $u \stringcat \overline{u} = \overline{u} \stringcat u = \emptystring$.
In cases where the two don't match, nothing happens: $u \stringcat \overline{v} = \overline{v} \stringcat u = u$ if $u \neq v$.
So $\String{abc} \stringcat \overline{\String{abc}} = \emptystring$, but $\String{abc} \stringcat \overline{\String{aac}} = abc$.
Intuitively, $\overline{\String{abc}}$ is an instruction to delete a string iff it is $\String{abc}$; basically the string equivalent of antimatter in physics.


Thanks to these "antistrings", $\tuple{\setof{u, \overline{u} \mid u \in \Sigma^*}, \stringcat, \emptystring}$ is a group.
:::

For some groups, $\oplus$ may also be commutative, so that $a \oplus b = b \oplus a$ for all $a$ and $b$.
An example of that is $\tuple{\mathbb{Z}, +}$.
Such a group is called **Abelian**, after the mathematician [Niels Henrik Abel](https://en.wikipedia.org/wiki/Niels_Henrik_Abel).

# Types of relations

Weak partial orders and total orders are just two particular types of relations.
There are several others.

## Preorder

The most basic order relation is the **preorder**, which is like a weak partial order but lacks antisymmetry.
So it is transitive and reflexive, but not necessarily anything beyond that.

::: definition
A relation $R \subseteq D \times D$ is a **preorder** iff it is reflexive and transitive. 
:::

If one takes a preorder and adds antisymmetry, one gets a weak partial order.
If one adds symmetry instead, one gets an **equivalence relation**.

~~~ {.include-tikz size=mid}
relation_types.tikz
~~~

## Equivalence relations

::: definition
A relation $R \subseteq D \times D$ is an **equivalence relation** iff it is reflexive, symmetric, and transitive.
:::

Intuitively, an equivalence relation does exactly what its name implies: it relates elements that are equivalent with respect to some property that the relation is sensitive to.

::: example
One equivalence relation that everybody is familiar with is the equality $=$ of numbers.
But it isn't a particularly insightful relation.
It is reflexive as $n = n$ for every number $n$.
It also satisfies symmetry and transitivity, but that's because $x = y$ iff $x$ and $y$ are the same number.
So symmetry holds because $x = y$ obviously implies $y = x$ if $x$ and $y$ are the same number.
For the same reason, transitivity must hold, too: $x = y$ and $y = z$ can be the case only if $x$, $y$, and $z$ are all the same number, in which case $x = z$ is of course true.
:::

::: example
A more interesting example is equivalence modulo $2$.
The modulo $n$ operation divdies a number by $n$ and returns the remainder.
For example, $5 \mod 2 = 1$, whereas $6 \mod 2 = 0$.

Suppose $x \equiv_2 y$ iff $x \mod 2 = y \mod 2$.
Then $\equiv_2$ is an equivalence relation.
First, it is clearly refleixve: $x \equiv_2 x$ iff $x \mod 2 = x \mod 2$, which always holds.
Next, symmetry is also satisfied: $x \equiv_2 y$ iff $x \mod 2 = y \mod 2$ iff $y \mod 2 = x \mod 2$ iff $y \equiv_2 x$.
:::

::: exercise
Explain why $\equiv_2$ is transitive.
:::

::: exercise
Let us define a person's *family pain* as the number of family members that they'd rather not be related to.
Given some domain $D$ of individuals, let $R \is \setof{ \tuple{d,e} \mid d \text{ and } e \text{ suffer the same familiy pain} }$.
Show that $R$ is an equivalence relation.
:::

::: exercise
The **equivalence kernel** of a function $f$ is an equivalence relation $\sim_f$ such that two elements are equivalent iff they are mapped to the same value by $f$.
Formally, $x \sim_f y$ iff $f(x) = f(y)$.
Explain why $\equiv_f$ is an equivalence relation no matter what function $f$ is.
:::

::: exercise
Suppose that two cities are *continent mates* iff they are connected by roads.
The continent mate relation contains all $\tuple{c,m}$ (and only those) such that $c$ and $m$ are continent mates.
Is the continent mate relation an equivalence relation?
Why (not)?
:::

::: exercise
Is the empty relation (i.e. $\emptyset$) an equivalence relation?
Justify your answer.
:::

## Equivalence classes and partitions

Given an equivalence relation $R \subseteq D \times D$ and element $x$, $[x]$ is the **equivalence class** of $x$.
It contains all elements that are equivalent to $x$ according to $R$.
Formaly, $[x] \is \setof{ y \mid x R y}$.
Keep in mind that $R$ is reflexive, so $x \in [x]$.

Also, symmetry and transitivity entail that $x \in [y]$ iff $y \in [x]$.
So it follows from $x \in [y]$ that $[x] = [y]$.
Hence it doesn't matter which member of an equivalence class one uses in its name, there is no difference between $[x]$ and $[y]$ if $x$ and $y$ belong go the same equivalence class.

::: example
Consider again the modulo 2 relation $\equiv_2$.
It gives rise to two equivalence classes.
The first ist $[0] \is \setof{0, 2, 4, 6, \ldots}$, which contains all even numbers, and the other is $[1] \is \setof{1, 3, 5, 7, \ldots}$, the set of odd numbers.
We could also refer to them as $[2]$ and $[3]$, respectively, or $[10]$ and $[7]$, it really does not matter.
:::

::: exercise
Intuitively, what equivalence classes does the continent mate relation yield?
:::

Note that equivalence classes never overlap, they are disjoint sets.
Given a set $S$ and an equivalence relation $R$, no member of $S$ can belong to more than one equivalence class.

::: exercise
Suppose that $x \in [y]$ and $x \in [z]$, but $[y] \neq [z]$.
Why is this impossible?
:::

In addition, an equivalence relation over a set $S$ is usually chosen in such a way that every element of $S$ belongs to an equivalence class.

::: exercise
In principle, one could combine the set $\setof{a,b,c}$ with the equivalence relation $R \is \setof{\tuple{a,a}, \tuple{a,b}, \tuple{b,a}, \tuple{b,b}}$.
But it is more natural to extend the relation to $R' \is \setof{\tuple{a,a}, \tuple{a,b}, \tuple{b,a}, \tuple{b,b}, \tuple{c,c}}$.
Intuitively, $R'$ is exactly like $R$ except that there is also an equivalence class for elements that $R$ is not defined for.
:::

Given these assumptions, every member of $S$ belongs to exactly one equivalence class.
The equivalence classes thus add an additional layer of structure to $S$.
They break it down into a collection of non-overlapping, non-empty subsets (the equivalence classes) that fully cover $S$.
This is also called a **partition** of $S$, and one says that $R$ partitions $S$.
Each equivalence class is also called a **cell** of the partition.

## Quotient structure

Given an equivalence relation $\sim$, $S/\sim \is \setof{ [x] \mid x \in S}$ is the partition $\sim$ induces on $S$.
This is also called a **quotient set** (yes, there's many different names for the same thing here).
Sometimes, $S$ may have some additional operation or relation defined on it.
It may be possible to lift this operation or relation from $S$ to its quotient set $S/\sim$.
In this case, one obtains a **quotient structure**.

::: example
Consider once more the \emph{modulo-2} equivalence relation $\equiv_2$.
Over the natural numbers, it induces a quotient set consisting of $[0]$ and $[1]$, the even and odd numbers, respectively.
Now suppose that we add addition as an operation to the natural numbers.
Then it holds that $(m + n) \mod 2 = ([m] + [n]) \mod 2$.
In other words, there are two different ways of computing the desired result.
The first option operates on $S$.
One adds the two numbers and then takes the sum modulo 2.
Alternatively, one can look at the quotient set.
Take the two equivalence classes, and take their sum by picking the smallest number from each equivalence class and adding them together.
Then apply modulo 2 as before.


Here's what this looks like with specific numbers.
Suppose you want to calculate $(10,222 + 13,728,529) \mod 2$.
You could add this up to $13,738,751$, divide by two, and get a remainder of $1$.
But you probably realized right away that the first number is even and the second one odd, so their sum will be odd, which means that division by 2 will leave a remainder of $1$.
In other words, you have computed the result with the quotient structure.
First you noted that $10,222 \in [0]$ and $13,728,529 \in [1]$.
As $[0] + [1] = 0 + 1 = 1$, you immediately get a remainder of $1$.
:::

Quotient structures are a very powerful concept, in particular when it comes to designing efficient algorithms.
A set may contain millions of elements, and the operations on the set may take a long time to compute on some of those elements.
But you might be able to build a much smaller quotient structure, and the operations may be faster over equivalence classes because you can pick very simple representatives of each class.
After all, $(3 + 5) \mod 7$ is a much easier way to calculate the output of $(7,003 + 14,726) \mod 7$.

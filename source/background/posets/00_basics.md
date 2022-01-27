**Prerequisites**

- tuples (basics)
- relations (basic orders)

# Posets

While sets are unstructured, they can be combined with an ordering relation to yield a structured object.
Usually, this will be a partial order.
A set with a partial order defined over it is a **partially ordered set** or simply **poset**.

## Definition

In mathematical terms, a poset is usually treated as a tuple $\tuple{S, R}$ that consists of the set $S$ and the order $R$ defined over its elements.
Don't attach too much significance to this, it is just a matter of notation and you wouldn't want to apply the usual tuple operations to these objects.
For instance, we wouldn't want to concatenate the posets $\tuple{S_1, R_1}$ and $\tuple{S_2, R_2}$ to get a 4-tuple $\tuple{S_1, R_1, S_2, R_2}$, that doesn't make much sense.

::: definition
A **partially ordered set**, or simple **poset**, is a pair $\tuple{S, R}$ such that $S$ is some set and $R$ is a partial order over $S$.
<!-- If $R$ is a weak/strict partial order, then $\tuple{S, R}$ is also called a weak/strict poset. -->
:::

Sometimes, $S$ is also called the **carrier** of the poset $\tuple{S, R}$.

::: example
The set of natural numbers is $\mathbb{N} \is \setof{0, 1, 2, 3, \ldots}$.
By itself, it has no internal order.
But of course we can order the natural numbers according to the familiar relation $\leq$, and then we get the poset $\tuple{\mathbb{N}, \leq}$.
The carrier of $\tuple{\mathbb{N}, \leq}$ is $\mathbb{N}$.
:::

::: example
We can take the set $H$ of all humans that ever lived or are currently alive.
We then order this set by the ancestor relation.
Since that is a partial order, the result is a poset.
<!-- If we treat every human as an ancestor of themselves, the ancestor relation is a weak partial order, so once again we get a weak poset. -->
<!-- If we use the more intuitive definition, then we get a strict poset. -->
:::

## Visualizing posets

Often it is very useful to visualize posets.
In this case, elements of the set are represented as nodes in a figure, and arrows between the nodes indicate that they are related via the order relation.
Here is what this looks like for the natural numbers ordered by $\leq$.

~~~ {.include-tikz size=mid}
natnum_lessthan_redundant.tikz
~~~

Since that is very convoluted, it is customary to omit arrows that can be inferred from the properties of the order.
First, one omits all arrows that can be inferred from transitivity.
That is to say, if there is an arrow from $x$ to $y$ and another arrow from $y$ to $z$, we do not need an arrow from $x$ to $z$.

~~~ {.include-tikz size=mid}
natnum_lessthan_loops.tikz
~~~

And if we know that the ordering relation $R$ is such that $x \mathrel{R} x$ holds for every $x$, then we do not need all the loops either.

~~~ {.include-tikz size=mid}
natnum_lessthan_simplified.tikz
~~~

**Caution:** due to these conventions, a depiction of $\tuple{\mathbb{N}, \leq}$ will look the same as one for $\tuple{\mathbb{N}, <}$, but those are different posets.

::: exercise
Take the set $\mathbb{Z} \is \setof{0, -1, 1, -2, 2, -3, 3, \ldots}$ of integers.
Let $x \prec y$ iff $x^2 \leq y^2$.
Sketch a figure of the poset $\tuple{\mathbb{Z}, \prec}$.
Avoid all arrows that can be inferred from the general properties of $\prec$.
:::

::: exercise
Let $S$ be the set of all substrings of the word *poset*.
Draw the strict poset $\tuple{S, \sqsubset}$, where $\sqsubset$ is the proper substring relation: $x \sqsubset y$ iff there is some $z \neq \emptystring$ such that $x \stringcat z = y$.


Now suppose that we used $\sqsubseteq$ instead: $x \sqsubseteq y$ iff there is some (possibly empty) $z$ such that $x \stringcat z = y$.
Do you have to change anything about your figure?
:::

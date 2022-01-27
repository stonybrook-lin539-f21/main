# Posets

::: exercise
Take the set $\mathbb{Z} \is \setof{0, -1, 1, -2, 2, -3, 3, \ldots}$ of integers.
Let $x \prec y$ iff $x^2 \leq y^2$.
Sketch a figure of the poset $\tuple{\mathbb{Z}, \prec}$.
Avoid all arrows that can be inferred from the general properties of $\prec$.
:::

::: solution
fixme: typeset this
:::

::: exercise
Let $S$ be the set of all substrings of the word *poset*.
Draw the strict poset $\tuple{S, \sqsubset}$, where $\sqsubset$ is the proper substring relation: $x \sqsubset y$ iff there is some $z \neq \emptystring$ such that $x \stringcat z = y$.

Now suppose that we used $\sqsubseteq$ instead: $x \sqsubseteq y$ iff there is some (possibly empty) $z$ such that $x \stringcat z = y$.
Do you have to change anything about your figure?
:::

::: solution
fixme: typeset this

No changes are needed because the only difference between the strict partial order $\sqsubset$ and the weak partial order $\sqsubseteq$ is reflexivity, which isn't usually indicated in such diagrams.
:::

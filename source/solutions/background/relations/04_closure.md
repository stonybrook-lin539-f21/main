# Taking the closure of a relation

Let $D$ be some fixed domain over which we define a relation $R \subseteq D \times D$.
The $P$-closure of $R$ is the smallest $R'$ such that $R \subseteq R' \subseteq D \times D$ and $R$ has property $P$.
For example, the reflexive, symmetric, transitive closure of $R$ is the smallest superset $R'$ that is reflexive, symmetric, and transitive.

::: example
Consider the relation $R \is \setof{ \tuple{1,2}, \tuple{2,3}, \tuple{3,4} }$.
We want to compute its transitive closure.
We first add $\tuple{1,3}$ and $\tuple{2,4}$, which we can construct from the existing pairs via transitivity.
But the result is still not transitive
The relation now contains both $\tuple{1,3}$ and $\tuple{3,4}$, so we also have to add $\tuple{1,4}$.
At this point, the relation is transitive, so we do not add any more edges.
:::

::: example
Consider the relation $R \is \setof{ \tuple{1,2}, \tuple{3,2} }$.
Its transitive closure is just $R$.
:::

::: example
Consider once more the relation $R \is \setof{ \tuple{1,2}, \tuple{3,2} }$.
Now we want to compute its symmetric, transitive closure.
As $R$ is not symmetric, we have to add additional pairs, in this case $\tuple{2,1}$ and $\tuple{2,3}$.
But $R' \is \setof{\tuple{1,2}, \tuple{2,1}, \tuple{2,3}, \tuple{3,2}}$ is not transitive.
In order to make $R'$ transitive, we have to add $\tuple{1,3}$ and $\tuple{3,1}$, but also $\tuple{1,1}$, $\tuple{2,2}$, and $\tuple{3,3}$.
The resulting $R'' \is \setof{1,2,3} \times \setof{1,2,3}$ is transitive and symmetric, and even reflexive.
:::

::: exercise
Calculate all of the following, assuming that the relation's domain is $D \is \setof{a,b,c,d}$:

- the reflexive closure of $\setof{\tuple{a,b}, \tuple{b,a}}$
- the transitive closure of $\setof{\tuple{a,b}, \tuple{b,a}}$
- the transitive closure of $\setof{\tuple{a,b}, \tuple{b,c}, \tuple{c,d}, \tuple{d,a}}$
- the reflexive, symmetric, transitive closure of $\setof{\tuple{a,b}, \tuple{a,c}, \tuple{d,c}}$
- the reflexive, symmetric, transitive closure of $\emptyset$

:::

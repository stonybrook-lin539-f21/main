# Union, intersection, and complement of sets

::: exercise
Compute the union of the following:

- $\setof{0,1} \cup \setof{2,3}$
- $\setof{0,1} \cup \setof{1,2,3}$
- $\setof{0,1} \cup \setof{0,1}$
- $\setof{0,1} \cup \emptyset$
- $\setof{1,2,3} \cup \setof{0,1}$

:::

::: solution

- $\setof{0,1} \cup \setof{2,3} = \setof{0,1,2,3}$
- $\setof{0,1} \cup \setof{1,2,3} = \setof{0,1,2,3}$
- $\setof{0,1} \cup \setof{0,1} = \setof{0,1}$
- $\setof{0,1} \cup \emptyset = \setof{0,1}$
- $\setof{1,2,3} \cup \setof{0,1} = \setof{0,1,2,3}$

:::

::: exercise
Compute the union of the following in a step-wise fashion:

- $\setof{0,1} \cup \setof{2,3} \cup \emptyset$
- $\setof{0,1} \cup \emptyset \cup \setof{2,3}$

:::

::: solution
This can be done in two different orders in each case, depending on whether one first takes the left union or the right union.
But only in the first example does this order difference lead to different intermediate steps:

- $\setof{0,1} \cup \setof{2,3} \cup \emptyset = \setof{0,1,2,3} \cup \emptyset = \setof{0,1,2,3}$
- $\setof{0,1} \cup \setof{2,3} \cup \emptyset = \setof{0,1} \cup \setof{2,3} = \setof{0,1,2,3}$
- $\setof{0,1} \cup \emptyset \cup \setof{2,3} = \setof{0,1} \cup \setof{2,3} = \setof{0,1,2,3}$

:::

::: exercise
Compute the intersection of the following:

- $\setof{0,1} \cap \setof{2,3} = \emptyset$
- $\setof{0,1} \cap \setof{1,2,3} = \setof{1}$
- $\setof{0,1} \cap \setof{0,1} = \setof{0,1}$
- $\setof{0,1} \cap \emptyset = \emptyset$
- $\setof{1,2,3} \cap \setof{0,1} = \setof{1}$

:::

::: exercise
Give a concrete example where $A - B = B - A$.
Then make a single change to $A$ such that $A - B \neq B - A$.
:::

::: solution
Assume $A \is \setof{a}$ and $A = B$.
In that case, $A - B = A - A = \emptyset = A - A = B - A$.
Then if we set $A \is \setof{a,b}$ and leave $B \is \setof{a}$, we have
$A - B = \setof{a,b} - \setof{b} = \setof{a} \neq \emptyset = \setof{a} - \setof{a,b} = B - A$.
:::

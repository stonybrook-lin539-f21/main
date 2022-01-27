# Comparing sets

::: exercise
Complete the table below.

| A             | B                 | $A \subseteq B$? | $A \supseteq B$? | 
| :--           | :--               | :--              | :--              | 
| $\setof{a,b}$ | $\setof{a,a,b,c}$ |                  |                  | 
| $\setof{a}$   | $\setof{b}$       |                  |                  | 
| $\setof{}$    | $\setof{a}$       |                  |                  | 
| $\setof{a,b}$ | $\setof{a,a,b,b}$ |                  |                  | 

:::

::: solution
Complete the table below.

| A             | B                 | $A \subseteq B$? | $A \supseteq B$? | 
| :--           | :--               | :--              | :--              | 
| $\setof{a,b}$ | $\setof{a,a,b,c}$ | Y                | N                | 
| $\setof{a}$   | $\setof{b}$       | N                | N                | 
| $\setof{}$    | $\setof{a}$       | Y                | N                | 
| $\setof{a,b}$ | $\setof{a,a,b,b}$ | Y                | Y                | 

:::

::: exercise
Say whether the following statement is true or false and justify your answer:
for any two sets $A$ and $B$, $A \subseteq B$ iff $A \cap B = A$.
:::

::: solution
This statement is correct.
We first show the right-to-left direction, then left-to-right.

If $A \cap B = A$, then every element of $A$ must also be an element of $B$, i.e. $A \subseteq B$.

In the other direction, if $A \subseteq B$, then every element of $A$ is an element of $B$.
Hence $A \cap B$ is a superset of $A$.
But as it is impossible for $A \cap B$ to a proper superset of $A$, it must be the case that $A \cap B = A$.
:::

::: exercise
Fill in $=$, $\subsetneq$, or $\supsetneq$ as appropriate.

- $\setof{a,b} \_ \setof{a}$
- $\setof{a,a,b,c} \_ \setof{b,b,a,c}$
- $\setof{1,2,3} \_ \setof{n + 5 \mid n \in \setof{-4, -3}}$
- $\emptyset \_ \setof{a}$
- $\emptyset \_ \setof{\emptyset}$

:::

::: solution

- $\setof{a,b} \supsetneq \setof{a}$
- $\setof{a,a,b,c} = \setof{b,b,a,c}$
- $\setof{1,2,3} \supsetneq \setof{n + 5 \mid n \in \setof{-4, -3}}$
- $\emptyset \subsetneq \setof{a}$
- $\emptyset \subsetneq \setof{\emptyset}$

:::

::: exercise
For each line in the table, say whether the sets are disjoint, incomparable, identical, or stand in a proper subset/superset relation.

| A               | B                                                 | Relation      |
| :--             | :--                                               | :--           |
| $\setof{2,5,8}$ | the set of all odd numbers                        | incomparable  |
| $\setof{a,b,c}$ | $\setof{a,b} \cup (\setof{a,c} - \setof{b,d})$    | identical     |
| $\emptyset$     | $\setof{a,b} \cap (\setof{a,c} - \setof{b,d})$    | proper subset |
| $\emptyset$     | $\setof{a,b} \cap (\setof{a,c} \cap \setof{b,d})$ | identical     |

:::

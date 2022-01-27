# Operations on multisets

## Standard set operations

::: exercise
Fill each gap with a matching multiset or operator.


- $\setof{a:3, b:2, c:1} \cup \setof{a:5, b:1, d:8} = \_$
- $\setof{c:17} \_ \setof{a:5, b:1, d:8} = \setof{c:17}$
- $\setof{a:3, b:3} \cup \_ = \setof{a:5, b:3, c:5, d:6}$
- $\_\ \_ \setof{a:5, b:1, d:8} = \setof{a:3, b:1}$

:::

::: solution

- $\setof{a:3, b:2, c:1} \cup \setof{a:5, b:1, d:8} = \setof{a:5, b:2, c:1, d:8}$
- $\setof{c:17} - \setof{a:5, b:1, d:8} = \setof{c:17}$
- $\setof{a:3, b:3} \cup \setof{a:5, b:2, c:5, d:6} = \setof{a:5, b:3, c:5, d:6}$ ($b$ could have any count less than or equal to $3$)
- $\setof{a:3, b:5, d:0} \cap \setof{a:5, b:1, d:8} = \setof{a:3, b:1}$ (there are infinitely many other solutions, some using intersection, some using relative complement)

:::

::: exercise
Calculate the final result of the equations below.
If the result cannot be uniquely determined without additional assumptions, explain why.

- $3 \multimult \big( (\setof{a:5, b:3}_M \multisum \setof{a:1, c:5, d:6}_M) - (\setof{a:5, b:3}_M \cap \setof{a:1, c:5, d:6}_M) \big )$
- $\setof{\text{John}, \text{John}} \multisum 3 \multimult \setof{\text{Mary}, \text{Mary}, \text{Mary}, \text{John}}_M$
- $\setof{a:5, c:1}_M \cup \setof{a:3, b:3, c:3, d:3}_M \multisum \setof{a:1}_M$

:::

::: solution

- $3 \multimult \big( (\setof{a:5, b:3}_M \multisum \setof{a:1, c:5, d:6}_M) - (\setof{a:5, b:3}_M \cap \setof{a:1, c:5, d:6}_M) \big ) =
3 \multimult \big( \setof{a:6, b:3, c:5, d:6} - (\setof{a:5, b:3}_M \cap \setof{a:1, c:5, d:6}_M) \big ) =
3 \multimult \big( \setof{a:6, b:3, c:5, d:6} - \setof{a:1, b:0, c:0, d:0} \big ) =
3 \multimult \setof{a:5, b:3, c:5, d:6} =
\setof{a:15, b:9, c:15, d:18}$

For the second example, we have to assume that $\setof{\text{John}, \text{John}}$ is a multiset even though it isn't marked as such.
Otherwise the multiset sum isn't defined.

- $\setof{\text{John}, \text{John}} \multisum 3 \multimult \setof{\text{Mary}, \text{Mary}, \text{Mary}, \text{John}}_M =
\setof{\text{John}: 2} \multisum 3 \multimult \setof{\text{Mary}: 3, \text{John}: 1} =
\setof{\text{John}: 2} \multisum \setof{\text{Mary}: 9, \text{John}: 3} =
\setof{\text{Mary}: 9, \text{John}: 5}$

The third equation has no unique solution because it is unclear in which order we should apply multiset union and multiset sum.
Each order yields a different result:

- $\setof{a:5, c:1}_M \cup (\setof{a:3, b:3, c:3, d:3}_M \multisum \setof{a:1}_M) =
\setof{a:5, c:1}_M \cup \setof{a:4, b:3, c:3, d:3}_M =
\setof{a:5, b:3, c:3, d:3}$

- $(\setof{a:5, c:1}_M \cup \setof{a:3, b:3, c:3, d:3}_M) \multisum \setof{a:1}_M =
\setof{a:5, b:3, c:3, d:3} \multisum \setof{a:1}_M =
\setof{a:6, b:3, c:3, d:3}$

:::

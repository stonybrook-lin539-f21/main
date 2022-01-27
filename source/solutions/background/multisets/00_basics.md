# Sets with counters: Multisets

::: exercise
Fill in the gaps with $=$ and $\neq$ as appropriate.


- $\setof{5, 5, 7, 8}_M \neq \setof{7, 5, 8, 7}_M$
- $\setof{5, 3, 4} = \setof{5,3,4,4,3,5,5,4,3}$ (careful, these are sets, not multisets)
- $\setof{\text{peanut butter}, \text{jelly}}_M = \setof{\text{peanut butter}, \text{jelly}}_M$
- $\setof{\text{John}, \text{John}, \text{John}}_M \neq \setof{\text{John}}_M$
- $\setof{a}_M \neq \setof{a,a}$ (the second is a set $\setof{a,a}$, which is equivalent to $\setof{a}$ because of idempotency, but a multiset is not the same as a set)

:::

::: exercise
Represent all the multisets in the exercise above with explicit counts.

- $\setof{5, 5, 7, 8}_M$: $\setof{5: 2, 7: 1, 8: 1}$
- $\setof{7, 5, 8, 7}_M$: $\setof{5:1, 7:2,  8:1}$
- $\setof{\text{peanut butter}, \text{jelly}}_M$: $\setof{\text{peanut butter}: 1, \text{jelly}: 1}$ 
- $\setof{\text{John}, \text{John}, \text{John}}_M$: $\setof{\text{John}: 3}$
- $\setof{\text{John}}_M$: $\setof{\text{John}: 1}$
- $\setof{a}_M$: $\setof{a: 1}$
:::

::: exercise
Write down the multiset defined by each set-builder expression.
These are not entirely straight-forward, and you'll have to make some educated guesses as to how to handle special cases.

- $\setof{n: 10 - n \mid 0 \leq n \leq 10} = \setof{0: 10, 1: 9, 2: 8, 3: 7, 4: 6, 5: 5, 6: 4, 7: 3, 8: 2, 9: 1, 10: 0}$
- $\setof{a: b, b: a \mid a,b \geq 0, a + b = 10} = \setof{0: 10, 1:9, 2:8, 3:7, 4:6, 5:5, 6:4, 7:3, 8:2, 9:1, 10:0}$

:::

# The Powerset

::: exercise
For each one of the following sets, compute its powerset.

1. $\setof{a,b}$
1. $\setof{a,b,c,d}$
1. $\setof{\setof{a}}$
1. $\emptyset$
1. $\setof{\emptyset}$
1. $\wp(\setof{\setof{a}})$
1. $\wp(\wp(\emptyset))$

:::

::: solution

1. $\setof{a,b} = \setof{\emptyset, \setof{a}, \setof{b}, \setof{a,b}}$
1. $\setof{a,b,c,d} = \{ \emptyset, \setof{a}, \setof{b}, \setof{c}, \setof{d}, \setof{a,b}, \setof{a,c}, \setof{a,d}, \setof{b,c}, \setof{b,d}, \setof{c,d}, \setof{a,b,c}, \setof{a,b,d}, \setof{a,c,d}, \setof{b,c,d}, \setof{a,b,c,d} \}$
1. $\setof{\setof{a}} = \setof{\emptyset, \setof{\setof{a}}}$
1. $\emptyset = \setof{\emptyset}$
1. $\setof{\emptyset} = \setof{\emptyset, \setof{\emptyset}}$
1. $\wp(\setof{\setof{a}}) = \setof{\emptyset, \setof{\emptyset}, \setof{\setof{\setof{a}}}, \setof{\emptyset, \setof{\setof{a}}}}$
1. $\wp(\wp(\emptyset)) = \setof{\emptyset, \setof{\emptyset}, \setof{\setof{\emptyset}}, \setof{\emptyset, \setof{\emptyset}}}$

:::

::: exercise
For each set $A$ in the previous exercise, verify that $\card{\wp(A)} = 2^{\card{A}}$.
:::

::: solution

1. Yes, $2^2 = 4$
1. Yes, $2^4 = 16$
1. Yes, $2^1 = 2$
1. Yes, $2^0 = 1$
1. Yes, $2^1 = 2$
1. Yes, $2^{2^1} = 4$
1. Yes, $2^{2^{2^0}} = 4$

:::

# Picking maxima and minima

Four commonly encountered functions are $\max$, $\min$, $\mathrm{argmax}$, and $\mathrm{argmin}$.
Each one is fairly intuitive.

## $\max$ and $\min$

The $\max$ function returns the largest element of a set.

::: example
Let $S \is \setof{-5, 7, 23}$.
Then $\max(S) = \max(\setof{-5, 7, 23}) = 23$.
Some authors just write $\max(-5, 7, 23)$ instead of $\max(\setof{-5, 7, 23})$.
:::

In most cases, $\max$ is used with numbers.
But the function can be generalized to any structure that is a linear order.

::: example
Consider **2**, the lattice with $F < T$.
Then $\max(\setof{F, T}) = T$.
:::

Note that the order must be a linear order.
With weak partial orders that aren't also linear orders, $\max$ may not be defined for all cases.

::: example
Consider a case hierarchy with
$\text{Nom} \leq \text{Acc}$
and
$\text{Nom} \leq \text{Gen}$, but Acc and Gen are unordered with respect to each other.
Then $\max(\setof{\text{Acc}, \text{Gen}})$ is undefined.
:::

The opposite of $\max$ is $\min$.
It returns the smallest member of a set.

::: example
While $\max(\setof{-5, 7, 23} = 23$, $\min(\setof{-5, 7, 23} = -5$.
And assuming $F < T$, $\min(\setof{T, F}) = F$.
:::

## argmax/argmin

will be added at a later point

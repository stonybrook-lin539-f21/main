# Morphological paradigms

::: exercise
What patterns do the two pictures below represent?

~~~ {.include-tikz size=mid}
123_AAB.tikz
~~~

~~~ {.include-tikz size=mid}
123_ABB.tikz
~~~
:::

::: solution
AAB and ABB, respectively.
:::

::: exercise
Define
$f_{AAA}$,
$f_{ABB}$,
$f_{ABC}$,
and
$f_{ABA}$.
:::

::: solution
1. $f_{AAA}$: $x \mapsto A$ for every $x \in \setof{1,2,3}$
1. $f_{ABB}$: $1 \mapsto A$, $2 \mapsto B$, $3 \mapsto B$
1. $f_{ABC}$: $1 \mapsto A$, $2 \mapsto B$, $3 \mapsto C$
1. $f_{ABA}$: $1 \mapsto A$, $2 \mapsto B$, $3 \mapsto A$
:::

::: exercise
Show that $f_{ABA}$ is not monotonically decreasing.
:::

::: solution
We have to show that there are $x$ and $y$ such that $x \leq y$ holds but $f(x) \geq f(y)$ does not hold.
This is the case for $x = 1$ and $y = 2$:
$1 \leq 2$, yet $f(1) = A \leq B = f(2)$.
:::

::: exercise
Show that monotonicity also explains the absence of adjectival gradation paradigms like
*good*-*better*-*goodest*
if one assumes the hierarchy $\text{positive} < \text{comparative} < \text{superlative}$.
Explain why this is an intuitively plausible hierarchy.
:::

::: solution
In the pattern *good*-*better*-*goodest*, the positive and superlative are A-forms, whereas the comparative is a B-form.
Hence we have $f(\text{good}) = f(\text{goodest}) \neq f(\text{better})$.
Suppose $f(\text{better}) > f(\text{good})$.
Then $f$ is not monotonically increasing because we have $\text{better} < \text{goodest}$ yet $f(\text{better}) > f(\text{goodest})$.
If, on the other hand, $f(\text{better}) < f(\text{goodest})$, then we have $\text{good} < \text{better}$ yet $f(\text{good}) > f(\text{better})$, which again shows that $f$ is not monotonic increasing.
The same way, $f$ can be shown not be monotonically decreasing, either.

The hierarchy is intuitively plausible because it orders the three forms by their meaning.
For example, a *tall* man is not as tall as a *taller* man, and nobody is taller than the *tallest* man.
:::

::: exercise
As was briefly mentioned earlier, no language seems to allow AAB as an adjectival gradation pattern.
Is this predicted by monotonicity?
If not, is this an undergeneration or an overgeneration problem?
:::

::: solution
This is not predicted because the AAB pattern is monotonically increasing.
This is an overgeneration problem because our formalism predicts that AAB should exist in some language, yet we do not find it in any language.
:::

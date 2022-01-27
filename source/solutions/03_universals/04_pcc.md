# Person Case Constraints

::: exercise
Can you think of other clitics in English?
Exemplify their use with specific sentences.
:::

::: solution
English also has *'im* for *him and *'em* for *them*.
However, *'im* is rarely used in writing.

- I told'im so.
- I told'em so.

One could argue that *y'* in *y'all* is a cliticized version of *you all*, but this is better understood as a single pronoun *you-all* where the first vowel is reduced for phonological reasons.
:::

::: exercise
Add the corresponding table for the M-PCC.
:::

::: solution

The M-PCC states that if IO is 2 or 3, then DO is not 1.
Hence the first column must be N, everything else is Y.

$\downarrow$IO/DO$\rightarrow$ | 1 | 2 | 3
--: | :-: | :-: | :-:
1   | -   | Y   | Y
2   | N   | -   | Y
3   | N   | Y   | -

:::

::: exercise
Translate between IO/DO notation and pairs.

- 2IO, 1DO
- $\tuple{1,2}$
- $\tuple{3,3}$
- 2DO, 1IO

:::

::: solution
Each pair is of the form $\tuple{\text{IO}, \text{DO}}$.
Hence we have:

- $\tuple{2, 1}$
- 1IO, 2DO
- 3IO, 3DO
- $\tuple{1, 2}$

:::

::: exercise
Fill each gap with $<$, $>$, or $=$ as appropriate.
If none of the three fit, leave the gap empty.


- $\tuple{3,3} \_ \tuple{2,2}$
- $\tuple{2,3} \_ \tuple{2,2}$
- $\tuple{3,2} \_ \tuple{2,2}$
- $\tuple{2,2} \_ \tuple{2,2}$
- $\tuple{1,2} \_ \tuple{3,1}$

:::

::: solution
We have $1 < 2 < 3$ for each component of the pair.
Hence:

- $\tuple{3,3} > \tuple{2,2}$ because $3 > 2$ and $3 > 2$
- $\tuple{2,3} > \tuple{2,2}$ because $2 = 2$ and $3 > 2$
- $\tuple{3,2} > \tuple{2,2}$ because $3 > 2$ and $2 = 2$
- $\tuple{2,2} = \tuple{2,2}$ because $2 = 2$ and $2 = 2$
- $\tuple{1,2} \_ \tuple{3,1}$ because $1 < 3$ and $2 > 1$

:::

::: exercise
Write down the 6 values of $f$ for the W-PCC.
:::

::: solution

- $f(\tuple{1, 2}) = T$
- $f(\tuple{1, 3}) = T$
- $f(\tuple{2, 1}) = T$
- $f(\tuple{2, 3}) = T$
- $f(\tuple{3, 1}) = T$
- $f(\tuple{3, 2}) = F$

:::

::: exercise
Pick two pairs $x$ and $y$ and use them to show that the U-PCC is not a monotonically increasing map.

*Hint:* What's the main difference between the W-PCC and the U-PCC?
:::

::: solution
We have $\tuple{2, 3} < \tuple{2, 1}$, yet $f(\tuple{2,3}) = T > F = f(\tuple{2, 1})$.
:::

::: exercise
Continuing the previous exercise, show that the U-PCC isn't a monotonically decreasing map either.
:::

::: solution
We have $\tuple{3, 2} < \tuple{1, 2}$, yet $f(\tuple{3,2}) = F < T = f(\tuple{1, 2})$.
:::

::: exercise
Fill each gap with $\triangleleft$, $\triangleright$, or $=$ as appropriate.
If none of the three fit, leave the gap empty.


- $\tuple{3,3} \_ \tuple{2,2}$
- $\tuple{2,3} \_ \tuple{2,2}$
- $\tuple{3,2} \_ \tuple{2,2}$
- $\tuple{2,2} \_ \tuple{2,2}$
- $\tuple{1,2} \_ \tuple{3,1}$

:::

::: solution
We now have $1 < 2 < 3$ in the first component and $3 \prec 2 \prec 1$ in the second component.

- $\tuple{3,3} \_ \tuple{2,2}$ because $3 > 2$ and $3 \prec 2$
- $\tuple{2,3} \triangleleft \tuple{2,2}$ because $2 = 2$ and $3 \prec 2$
- $\tuple{3,2} \triangleright \tuple{2,2}$ because $3 > 2$ and $2 = 2$
- $\tuple{2,2} = \tuple{2,2}$ because $2=2$ and $2=2$
- $\tuple{1,2} \triangleleft \tuple{3,1}$ because $1 < 3$ and $2 \prec 1$

:::

::: exercise
This exercise is only for those who have already delved deep into the background sections:
Explain why $\triangleleft$ is a weak partial order.

*Hint*: Remember the three properties that each weak partial order must satisfy, and explain for each one why it holds.
:::

::: solution
tbd
:::

::: exercise
Redraw the figures above with arrows pointing towards T and F as we did earlier on in this unit.
Confirm for yourself that this is indeed a monotonically increasing map.
:::

::: solution
fixme: typeset this even though it's a pain
:::

::: exercise
Draw the corresponding pictures (with boxes instead of arrows) for the S(trong)-PCC and the M(e first)-PCC.
:::

::: solution
fixme: typeset this even though it's a pain
:::

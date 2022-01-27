# Functions: Basic notation

::: exercise
Let $f$ be a function that takes as its input a number $n$ and returns $n+1$ on a weekday and $n+2$ on the weekend.

- Is $f$ a function?
- What if $f$ instead takes two arguments: a number $n$, and the name of the day of the week.

:::

::: solution
If $f$ takes only a number as its input, then it is not a function because it can produce distinct outputs for one and the same input.
However, if $f$ takes both the number $n$ and the day of the week as an argument, then it is a function because each combination of a number and day of the week has a unique output:

- $f(\text{Monday}, n) = n+1$
- $f(\text{Tuesday}, n) = n+1$
- $f(\text{Wednesday}, n) = n+1$
- $f(\text{Thursday}, n) = n+1$
- $f(\text{Friday}, n) = n+1$
- $f(\text{Saturday}, n) = n+2$
- $f(\text{Sunday}, n) = n+2$
:::

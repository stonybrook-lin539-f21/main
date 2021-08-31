# Factorial

Given a natural number $n \geq 1$, its **factorial** $n!$ is defined in a recursive fashion:

- $1! = 1$, and
- $n! = n \cdot (n - 1)!$.

::: example
The factorial of $5$ is $120$ because


- $5! = 5 \cdot 4!$
- $4! = 4 \cdot 3!$
- $3! = 3 \cdot 2!$
- $2! = 2 \cdot 1!$
- $1! = 1$


So $5!$ reduces to $5 \cdot 4 \cdot 3 \cdot 2 \cdot 1$
:::

The factorial often appears in combinatorial problems.
For instance, if you have $n$ distinct elements, then they can be arranged in $n!$ ways.

::: example
There are $3! = 6$ ways to order $a$, $b$, and $c$:


- $abc$
- $acb$
- $bac$
- $bca$
- $cab$
- $cba$

:::

The factorial function grows very fast, even faster than an exponential function.

| $n$ | $2^n$ | $n!$ |
| --: | --:   | --:  |
| 1   | 2     | 1    |
| 2   | 4     | 2    |
| 3   | 8     | 6    |
| 4   | 16    | 24   |
| 5   | 32    | 120  |
| 6   | 64    | 720  |

Even a very fast growing exponential like $10,000^n$ will eventually grow more slowly than the factorial, even though it grows more rapidly for small values of $n$ (e.g. $10,000^{10} = 10^{4^{10}} = 10^{40}$ is much larger than $10! = 3,628,800$).

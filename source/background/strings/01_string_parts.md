# Parts of strings

## Substrings

A **substring** is a continuous part of a string.

::: example
The string $\String{abcd}$ has 11 substrings:

- $\emptystring$
- $\String{a}$
- $\String{b}$
- $\String{c}$
- $\String{d}$
- $\String{ab}$
- $\String{bc}$
- $\String{cd}$
- $\String{abc}$
- $\String{bcd}$
- $\String{abcd}$

:::

Note that

1. the empty string is a substring of every string, and
2. every string is a substring of itself.

A substring $u$ of $v$ is **proper** iff $u \neq v$.

::: example
All the strings listed above are proper substrings of $\String{abcd}$, except $\String{abcd}$ itself.
:::

::: exercise
For each one of the gaps below, enter $\sqsubseteq$, $\sqsubsetneq$, or $\not\sqsubseteq$ depending on whether the first string is a substring of the second string, a proper substring, or neither:


- $\String{a} \_ \String{aaaa}$
- $\String{a} \_ \String{b}$
- $\emptystring \_ \String{b}$
- $\emptystring \_ \emptystring$
- $\String{aa} \_ \String{abbbca}$
- $\String{bc} \_ \String{abbbca}$
- $\String{cb} \_ \String{abbbca}$

:::

## Subsequence

A **subsequence** is a discontinuous part of a string that preserves the order between the symbols.

::: example
The string $\String{abcd}$ has subsequences:


- $\emptystring$
- $\String{a}$
- $\String{b}$
- $\String{c}$
- $\String{d}$
- $\String{ab}$
- $\String{ac}$
- $\String{ad}$
- $\String{bc}$
- $\String{bd}$
- $\String{cd}$
- $\String{abc}$
- $\String{abd}$
- $\String{bcd}$
- $\String{abcd}$


Note that $\String{ca}$ is not a subsequence of $\String{abcd}$, but it is a subsequence of $\String{abcda}$.
:::

Just like substrings, a subsequence $u$ of $v$ is proper iff $u \neq v$.

::: exercise
For each one of the gaps below, enter $\sqsubseteq$, $\sqsubsetneq$, or $\not\sqsubseteq$ depending on whether the first string is a subsequence of the second string, a proper subsequence, or neither:


- $\String{a} \_ \String{aaaa}$
- $\String{a} \_ \String{b}$
- $\emptystring \_ \String{b}$
- $\emptystring \_ \emptystring$
- $\String{aa} \_ \String{abbbca}$
- $\String{bc} \_ \String{abbbca}$
- $\String{cb} \_ \String{abbbca}$

:::

::: exercise
Say whether the following is True or False:
Every substring of some string $s$ is also a subsequence of $s$, but not the other way round.
Justify your answer.
:::

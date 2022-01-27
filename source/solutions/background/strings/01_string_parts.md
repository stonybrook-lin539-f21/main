# Parts of strings

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

::: solution

- $\String{a} \sqsubsetneq \String{aaaa}$
- $\String{a} \not\sqsubseteq \String{b}$
- $\emptystring \sqsubsetneq \String{b}$
- $\emptystring \sqsubseteq \emptystring$
- $\String{aa} \not\sqsubseteq \String{abbbca}$
- $\String{bc} \sqsubsetneq \String{abbbca}$
- $\String{cb} \not\sqsubseteq \String{abbbca}$

:::

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

::: solution

- $\String{a} \sqsubsetneq \String{aaaa}$
- $\String{a} \not\sqsubseteq \String{b}$
- $\emptystring \sqsubsetneq \String{b}$
- $\emptystring \sqsubseteq \emptystring$
- $\String{aa} \sqsubsetneq \String{abbbca}$
- $\String{bc} \sqsubsetneq \String{abbbca}$
- $\String{cb} \not\sqsubseteq \String{abbbca}$

:::

::: exercise
Say whether the following is True or False:
Every substring of some string $s$ is also a subsequence of $s$, but not the other way round.
Justify your answer.
:::

::: solution
This is correct.
A substring is a subsequence where all symbols happen to be adjacent.
For example, $\String{ab}$ is both a substring and a subsequence of $\String{abc}$.

On the other hand, not every subsequence is a substring.
For example, $\String{ac}$ is a subsequence of $\String{abc}$ but not a substring.
:::

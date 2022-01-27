# Strings: Basic notation

::: exercise
Fill in $=$ or $\neq$ as appropriate for each pair of strings below.

- $\mathit{abba}$ \_ $\mathit{ABBA}$
- $10$ \_ $5 + 5$
- $\setof{m,a,d} \_ \setof{d,a,m}$

Caution: $\{$ and $\}$ can be symbols just like $m$, $a$, or $d$.
:::

::: solution
- $\mathit{abba} \neq \mathit{ABBA}$
- $10 \neq 5 + 5$ (because those are strings, not numerical expressions)
- $\setof{m,a,d} \neq \setof{d,a,m}$ (because those are strings, not sets)
:::

::: exercise
For each one of the following, say whether it is a valid alphabet.
Justify your answer.

- $\setof{a}$
- $\setof{0,1}$
- the set of all English words that are spelled with at most 5 characters
- all natural numbers less than 1000
- the nucleobases of DNA: adenine, cytosine, guanine, thymine 

:::

::: solution

- $\setof{a}$: Yes, this is a finite set of symbols.
- $\setof{0,1}$: Yes, this is a finite set of symbols.
- the set of all English words that are spelled with at most 5 characters: Yes, because there are only finitely many words that can be spelled using at most 5 characters.
- all natural numbers less than 1000: Yes, because there are only finitely many of those.
- the nucleobases of DNA: adenine, cytosine, guanine, thymine: Yes, because this is a finite set. 

:::

::: exercise
Which one of the following are members of $\setof{a,b}^4$, i.e. $\Sigma^4$ where $\Sigma$ contains $a$, $b$, and nothing else?

- $\mathit{aaab}$
- $\mathit{aba}$
- $\mathit{aaaaa}$
- $\mathit{b}$
- $\mathit{abca}$

:::

::: solution

- $\mathit{aaab} \in \setof{a,b}^4$
- $\mathit{aba} \notin \setof{a,b}^4$ because its length is $3$, not $4$
- $\mathit{aaaaa} \notin \setof{a,b}^4$ because its length is $5$
- $\mathit{b} \notin \setof{a,b}^4$ because its length is $1$
- $\mathit{abca} \notin \setof{a,b}^4$ because $c$ is not part of the alphabet

:::

::: exercise
List all members of $\setof{k,o,z}^2$.
:::

::: solution

1. $\String{kk}$
1. $\String{ko}$
1. $\String{kz}$
1. $\String{ok}$
1. $\String{oo}$
1. $\String{oz}$
1. $\String{zk}$
1. $\String{zo}$
1. $\String{zz}$

:::

::: exercise
Write each one of the following in a more compact fashion using exponents.

- ABBA
- loool
- aardvark

:::

::: solution

- ABBA: AB$^2$A
- loool: lo$^3$l
- aardvark: a$^2$rdvark

:::

::: exercise
Enumerate the five shortest members of $\setof{a}^*$.
:::

::: solution

1. $\emptystring$
1. $\String{a}$
1. $\String{aa}$
1. $\String{aaa}$
1. $\String{aaaa}$

:::

::: exercise
Give an example of distinct $u$ and $v$ such that $u \stringcat v = v \stringcat u$ and neither $u$ nor $v$ is the empty string.

::: solution
The easiest solution is $u = v = a$, so that $a \stringcat a = a \stringcat a = aa$.
A more elaborate example is $u = \String{ab}$ and $v = \String{abab}$, where $\String{ab} \stringcat \String{abab} = \String{abab} \stringcat \String{ab}$.
:::

::: exercise
Is the following true or false?
If $u \neq v$, then $u \stringcat v \neq v \stringcat u$?
:::

::: solution
No, see the example above with $u = \String{ab}$ and $v = \String{abab}$.
:::

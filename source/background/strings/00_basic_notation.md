**Prerequisites**

- sets (basic notation)

# Strings: Basic notation

Strings play a very prominent role in computational linguistics.
A string is a sequence of symbols, like *nfm*, *wendigo*, or *105§/*.
In contrast to sets, strings are ordered and can contain duplicates.

::: example
The sets $\setof{m,a,d}$, $\setof{d,a,m}$, and $\setof{a,d,a,m}$  are equivalent, but for strings $\mathit{mad} \neq \mathit{dam} \neq \mathit{adam}$.
:::

::: exercise
Fill in $=$ or $\neq$ as appropriate for each pair of strings below.

- $\mathit{abba}$ \_ $\mathit{ABBA}$
- $10$ \_ $5 + 5$
- $\setof{m,a,d} \_ \setof{d,a,m}$

Caution: $\{$ and $\}$ can be symbols just like $m$, $a$, or $d$.
:::

## Alphabet

When talking about strings, one usually fixes a finite set of symbols over which the strings are built.
This is called an **alphabet**.
Alphabets are often given labels like $\Sigma$ or $\Omega$.
A string over alphabet $\Sigma$ is also called a $\Sigma$-string.

::: example
The set of Latin characters (A-Z, a-z) is an alphabet that's familiar to all of you.
Strings over it include:


- string
- alphabet
- aaaaaaa
- c

:::

::: example
The set of Arabic digits is an alphabet with symbols 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9.
Every natural number (0, 1, 2, ...), when represented in decimal as usual, is a string over this alphabet.
But not every string over this alphabet is a number of the decimal system.
For instance, 000134095 is not a valid number, although 134095 is.
:::

::: example
The set $\mathbb{N}$ of all natural numbers is not a valid alphabet because it isn't finite.
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

## String length

The length of a $\Sigma$-string $s$ is indicated by $\length{s}$.
For instance,
$\length{\text{ant}} = 3$,
$\length{0770001} = 7$,
and $\length{\text{a}} = 1$.
The set of all strings over $\Sigma$ whose length is exactly $n$ is denoted by $\Sigma^n$.

::: example
Let $\Sigma \is \setof{a,b}$.
Then $\Sigma^3$ contains all of the following strings, and only those:


- $\mathit{aaa}$
- $\mathit{aab}$
- $\mathit{aba}$
- $\mathit{abb}$
- $\mathit{baa}$
- $\mathit{bab}$
- $\mathit{bba}$
- $\mathit{bbb}$

:::

The size of $\Sigma^n$ is always fixed.
If $\Sigma$ has $m$ members, then $\Sigma^n$ contains $m^n$ strings.

::: example
In the previous example, $\Sigma$ contains two symbols, so $\Sigma^n$ should consist of $2^3 = 8$ distinct strings.
That's exactly what we found.
:::

::: exercise
Which one of the following are members of $\setof{a,b}^4$, i.e. $\Sigma^4$ where $\Sigma$ contains $a$, $b$, and nothing else?

- $\mathit{aaab}$
- $\mathit{aba}$
- $\mathit{aaaaa}$
- $\mathit{b}$
- $\mathit{abca}$

:::

::: exercise
List all members of $\setof{k,o,z}^2$.
:::

Very often expressions like $a^n$ are used as a shorthand for $\setof{a}^n$.

::: example
The expression $\mathit{b a^5 c^3 d}$ is a shorthand for $\mathit{baaaaacccd}$.
:::

::: exercise
Write each one of the following in a more compact fashion using exponents.

- ABBA
- loool
- aardvark

:::

## Infinite string sets over $\Sigma$

Since alphabets must be finite, $\Sigma^n$ is necessarily finite for any alphabet $\Sigma$ and $n \geq 0$.
But the set of all strings over $\Sigma$ is infinite.

::: example
Let $\Sigma \is \setof{a}$.
Then $a$ is a string over $\Sigma$, and so are $\mathit{aa}$, $\mathit{aaa}$, $\mathit{aaaa}$, and so on.
This enumeration continues indefinitely, so there must be infinitely many distinct strings over $\Sigma$.
:::

Two infinite string sets are commonly defined over $\Sigma$.
They are $\Sigma^*$ and $\Sigma^+$, respectively.
The former contains all strings over $\Sigma$, whereas the latter contains all strings whose length is at least $1$.
The only difference between the two is that $\Sigma^*$ also contains the **empty string** $\emptystring$.
The empty string is the string counterpart of the number 0: it represents nothing.
In fact, $\emptystring$ is the only string whose length is 0.

::: example
Let $\Sigma = \setof{a,b}$.
Then $\Sigma^*$ contains

- $\emptystring$,
- $\mathit{a}$,
- $\mathit{b}$,
- $\mathit{aa}$,
- $\mathit{ab}$,
- $\mathit{ba}$,
- $\mathit{bb}$,
- $\mathit{aaa}$,
- $\mathit{aab}$,
- $\mathit{aba}$,
- $\mathit{abb}$,
- and so on.

All these strings are also members of $\Sigma^+$, except $\emptystring$.
:::

$\Sigma^*$ is also called the **Kleene closure**, named after [Stephen C. Kleene](https://en.wikipedia.org/wiki/Stephen_Cole_Kleene).

Here's a little bit of background to make it easier for you to remember the difference between $\Sigma^*$ and $\Sigma^+$.
As you might know from search engines, the Kleene star `*` is sometimes used as a wildcard that matches everything.
So $\Sigma^*$ can be translated as "every string built over $\Sigma$".
On the other hand $\Sigma^+$ only contains those strings whose length is at least 1, or in other words, whose length is positive.
And $+$ is a common abbreviation for positive (just think of batteries).

::: exercise
Enumerate the five shortest members of $\setof{a}^*$.
:::

## Concatenation

Given two $\Sigma$-strings $u$ and $v$, their **concatenation** $u \stringcat v$ is the result of "glueing" the left end of $v$ to the right end of $u$.

::: example
Here are a few examples of concatenation:

- $\mathit{math} \stringcat \mathit{ematics} = \mathit{mathematics}$,
- $2000 \stringcat 18 = 200018$,
- $\text{Thomas} \stringcat \text{Graf} = \text{ThomasGraf}$.

:::

Just like addition, concatenation is **associative**.
This means that if we carry out multiple concatenations, it does not matter which concatenation step we resolve first: $u \stringcat (v \stringcat w) = (u \stringcat v) \stringcat w = u \stringcat v \stringcat w$.

::: example
It does not matter in which order we combine *is* with *concatenation* and *associative* below:

- $(\emph{concatenation} \stringcat \emph{is}) \stringcat \emph{associative} = \emph{concatenation is associvative}$
- $\emph{concatenation} \stringcat (\emph{is} \stringcat \emph{associative}) = \emph{concatenation is associvative}$

:::

Even though concatenation is associative, it is not **commutative**.
That is to say, $u \stringcat v$ and $v \stringcat u$ are not necessarily the same.

::: example
Let $u \is \text{house}$ and $v \is \text{boat}$.
Then $u \stringcat v$ is *houseboat*, whereas $v \stringcat u$ is *boathouse*.
Those are not the same strings (and they also happen to mean completely different things).
:::

Note the special behavior of the empty string: $u \stringcat \emptystring = \emptystring \stringcat u = u$. 
This makes sense because adding nothing to $u$ does not change $u$, just like adding 0 to a number does not change that number.

Sometimes concatenation is not explicitly indicated, so that instead of $u \stringcat v$ one may simply write $\mathit{uv}$.

::: exercise
Give an example of distinct $u$ and $v$ such that $u \stringcat v = v \stringcat u$ and neither $u$ nor $v$ is the empty string.
:::

::: exercise
Is the following true or false?
If $u \neq v$, then $u \stringcat v \neq v \stringcat u$?
:::

## Recap

- A string is a sequence of symbols drawn from some alphabet.
- A $\Sigma$-string is a string over alphabet $\Sigma$.
- The length of string $s$ is denoted by $\length{s}$.
- The empty string $\emptystring$ is the unique string of length $0$.
- $\Sigma^n$ is the set of all $\Sigma$-strings $s$ such that $\length{s} = n$.
- $a^n$ is a shorthand for $\setof{a}^n$.
- The Kleene closure $\Sigma^*$ is the set of all $\Sigma$-strings (including $\emptystring$).
- The positive closure $\Sigma^+$ contains all $\Sigma$-strings except $\emptystring$.
- Concatenation of strings $u$ and $v$ is denoted by $u \stringcat v$.

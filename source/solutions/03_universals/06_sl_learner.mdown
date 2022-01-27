# The lattice space of $n$-gram grammars

::: exercise
As a reminder for yourself, write down an SL grammar for an attested linguistic phenomenon.
A simple option is word-final devoicing or intervocalic voicing, but feel free to mix it up a bit.
:::

::: solution
Here is a grammar for vowel harmony in a language with CV and CVC syllables and no transparent vowels.
Suppose there are two class of vowels, light (L) and dark (D), such that a word may only contain light vowels or only dark vowels.
As usual, C is a shorthand for consonants.
The following mixed negative 4-gram grammar correctly enforces vowel harmony in this language, assuming that L, D, and C are compiled out into the specific sounds of this language:

$$
^-G \is \setof{ \String{LCD}, \String{DCL}, \String{LCCD}, \String{DCCL} }
$$
:::

::: exercise
Suppose that you have the SL-$3$ language $(\String{aba})^+$, which contains $\String{aba}$, $\String{abaaba}$, $\String{abaabaaba}$, and so on.
Write down the positive trigram grammar for this language.
Then write down a single example from which one can immediately infer the whole grammar.
:::

::: solution
The positive trigram grammar is

$$
^+G \is \setof{
{{{L}}}{{{L}}}a,
{{{L}}}ab,
aba,
baa,
aab,
ba{{{R}}},
a{{{R}}}
}
$$

The grammar can be learned just from $\String{abaaba}$.
Quite generally, any string will do that is of the form $(\String{aba})^n$ for $n \geq 2$.
:::

::: exercise
Suppose $G_1 \is \setof{{{{L}}}{{{R}}}, {{{L}}}a, aa}$ and $G_2 \is \setof{a{{{R}}}}$.
Compute $G_{1 \wedge 2}$ and $G_{1 \vee 2}$.
:::

::: solution
$$
G_{1 \wedge 2} \is \emptyset
$$

$$
G_{1 \vee 2} \is \setof{ {{{L}}} {{{R}}}, {{{L}}}a, aa, a{{{R}}} }
$$
:::

::: exercise
Suppose that the lattice of grammars is as depicted above.
Assume furthermore that the currently conjectured grammar is $\setof{{{{L}}}{{{R}}}}$.
The next example contains the bigrams ${{{L}}}a$ and $a{{{R}}}$.
Verify via calculation that
$\setof{{{{L}}}{{{R}}}} \cup \setof{{{{L}}}a, a{{{R}}}} = \setof{{{{L}}}{{{R}}}} \vee \setof{{{{L}}}a, a{{{R}}}}$.
:::

::: solution
The upper bounds of
$\setof{{{{L}}}{{{{R}}}}$
and
$\setof{{{{L}}}a, a{{{R}}}}$
in the lattice
are
$\setof{{{{L}}}{{{R}}}, {{{L}}}a, a{{{R}}}}$
and
$\setof{{{{L}}}{{{R}}}, {{{L}}}a, a{{{R}}}, aa}$.
Among those two bounds, the least upper bound is
$\setof{{{{L}}}{{{R}}}, {{{L}}}a, a{{{R}}}}$.
This is identical to
$\setof{{{{L}}}{{{{R}}}} \cup \setof{{{{L}}}a, a{{{R}}}}$.
:::

::: exercise
Suppose that all members of $\mathcal{G}$ are negative grammars.
Draw the corresponding lattice of languages, and connect each grammar to its language with a colored line.
:::

::: solution
fixme: typeset this
:::

::: exercise
What is the relation between negative grammars and their languages?
Is it still monotonic?
If so, is it the same kind of monotonicity?
:::

::: solution
Now the function from grammars to their languages is monotonically decreasing instead of monotonically increasing.
This is unsurprising:
Recall that given a positive $n$-gram grammar $G$, its equivalent negative grammar is $\Sigma_E^n - G$.
Given two positive $n$-gram grammars $G_1$ and $G_2$ such that $G_1 \subseteq G_2$, it must the case that $\Sigma_E^n - G_1 \supseteq \Sigma_E^n - G_2$.
Hence if we wanted to ensure that the function stays monotonically increasing, we would have to order negative grammars by $\supseteq$ instead of $\subseteq$.
:::

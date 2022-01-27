# The problem of overgeneration

::: exercise
Write a negative grammar for intervocalic devoicing, assuming that the alphabet consists only of
*a*,
*i*,
*u*,
*s*,
*z*,
*f*,
and
*v*.
:::

::: solution
$^-G \is \setof{ \mathrm{V}[-voice]\mathrm{V} \mid \mathrm{V} \in \setof{\text{a, i, u}}, \mathrm[-voice] \in \setof{\text{s,f}}}$

Compiled out this set contains the following forbidden trigrams:

- asa
- asi
- asu
- afa
- afi
- afu
- isa
- isi
- isu
- ifa
- ifi
- ifu
- usa
- usi
- usu
- ufa
- ufi
- ufu

A bigram grammar won't do because the illicit *fufuf* only contains bigrams that also occur in the licit *fuvuf*.
:::

::: exercise
Assuming the same alphabet as before,
write an $n$-gram grammar (it may be positive or negative) that requires every word to consist of exactly 5 symbols.
This will be a large grammar.
But keep in mind that $n$-gram grammars are just sets, and there's various way to compactly define large sets.
:::

::: solution
$$
^+G \is
\setof{ {{{L}}} x_1 x_2 x_3 x_4 x_5 \mid x_i \in \Sigma \cup \setof{{{{L}}}}, 1 \leq i \leq 5}
\cup
\setof{ x_0 x_1 x_2 x_3 x_4 {{{R}}} \mid x_i \in \Sigma \cup \setof{{{{R}}}}, 0 \leq i \leq 4}
$$

This positive grammar contains, among others:

- ${{{L}}} {{{L}}} {{{L}}} {{{L}}} {{{L}}} a$
- ${{{L}}} {{{L}}} {{{L}}} {{{L}}} a i$
- ${{{L}}} {{{L}}} {{{L}}} a i u$
- ${{{L}}} {{{L}}} a i u s$
- ${{{L}}} a i u s z$
- $a i u s z {{{R}}}$
- $i u s z {{{R}}} {{{R}}}$
- $u s z {{{R}}} {{{R}}} {{{R}}}$
- $s z {{{R}}} {{{R}}} {{{R}}} {{{R}}}$
- $z {{{R}}} {{{R}}} {{{R}}} {{{R}}} {{{R}}}$

With those 6-grams, we can built the string $aiusz$.
Note that the grammar also contains useless 6-grams like ${{{L}}} a {{{L}}} u i {{{L}}}$.
But it does not contain, say, ${{{L}}} {{{R}}} {{{L}}} a i u$ or ${{{R}}} a {{{R}}} u i s$.
:::

::: exercise
Assuming the same alphabet as before,
write an $n$-gram grammar (it may be positive or negative) that requires every word to start with
*a*
and end with
*f*.
:::

::: solution
$^-G \is
\setof{ {{{L}}} x \mid x \neq \mathrm{a} }
\cup
\setof{ x {{{R}}} \mid x \neq \mathrm{f} }$

Alternatively, we could have defined a positive grammar over our alphabet $\Sigma$:
$^+G \is
\setof{ {{{L}}} \mathrm{a} }
\cup
\setof{ xy \mid x, y \in \Sigma}
\cup
\setof{ \mathrm{f} {{{R}}} }$

Note that the positive grammar has a size of $\card{\Sigma}^2 + 2$,
whereas the negative grammar has a size of $2 \times (\card{\Sigma}-1)$.
As $\Sigma$ grows in size, the negative grammar will be much more compact than the positive one.
:::

::: exercise
Assuming the same alphabet as before,
write an $n$-gram grammar (it may be positive or negative) for "penultimate *f*":
if a word has at least two symbols, then the last but one symbol must be *f* and no other position may be *f*.
:::

::: solution
$^-G \is
\setof{ xy{{{R}}} \mid x \neq \mathrm{f}, y \in \Sigma}
\cup
\setof{ x\mathrm{f}{{{R}}} \mid x \in \Sigma}
\cup
\setof{ \mathrm{f}yz \mid y,z \in \Sigma}$
:::

::: exercise
Suppose that English only contains the words
*the*,
*old*,
*man*,
*woman*,
*sleep*,
*sleeps*,
*snore*,
and
*snores*.
Assume furthermore that the English subject verb agreement system works as follows:
if the subject does not contain an adjective (like *old*),
then use the inflected verb form; otherwise, use the base form.
So we would get *The old man snore* but *The man snores*.
Write an $n$-gram grammar that captures this unnatural condition.
:::

::: solution
Let $^+G$ be the positive grammar that contains only the following trigrams:

- {{{L}}} {{{L}}} the,
- {{{L}}} the old,
- {{{L}}} the man, 
- {{{L}}} the woman, 
- the old man,
- the old woman,
- the old woman,
- the man snores,
- the woman snores,
- the man sleeps,
- the woman sleeps,
- old man snore,
- old woman snore,
- old man sleep,
- old woman sleep,
- man sleeps {{{R}}}
- man sleep {{{R}}}
- woman sleeps {{{R}}}
- woman sleep {{{R}}}
- man snores {{{R}}}
- man snore {{{R}}}
- woman snores {{{R}}}
- woman snore {{{R}}}
- sleeps {{{R}}} {{{R}}}
- sleep {{{R}}} {{{R}}}
- snores {{{R}}} {{{R}}}
- snore {{{R}}} {{{R}}}
:::

::: exercise
No known language enforces any of the following conditions:

1. The further to the right a syllable occurs in a word, the more consonants it must have.
1. Any sequence of sounds is a possible word as long as it contains at least as many vowels as consonants.
1. When we sort the words of a language by their length, we get the **Fibonacci series**: 1, 1, 2, 3, 5, 8, 13, ...
1. The first word in a sentence must rhyme with the last word in a sentence.
1. Every sentence must have an odd number of words.
1. To negate a sentence, utter it backwards.
1. Adjectives that start with a vowel go before the noun, adjectives that start with a consonant go after the noun.
1. Relative clauses follow the noun they modify if it is the subject, but otherwise precede the noun.

Apparently languages can only enforce constraints of a specific kind, and the examples above do not fit the bill.

For each constraint above, give a concrete example from English that violates it.
:::

::: solution
1. screen.ing
1. bnauili
1. trivially disproved by any word of length 4, for instance *mama*
1. Consider the sentence: "This is false."
1. Consider the sentence: "This is also false."
1. "True not is this" is not the negation of "This is not true". And "Am I as bored as you are?" is not a negation of "Are you as bored as I am?".
1. Consider the phrase: "The false, untrue claim".
1. Consider the sentence: "Anybody who knows a bit of English can disprove this claim, which is false."
:::

::: exercise
Can you think of a constraint that you are fairly certain does not arise in any natural language?

*Hint:* Mathematical concepts like prime numbers are very fruitful for this.
:::

::: solution
There's many options.
Here's a few examples of increasing complexity:

1. A sentence must have at most five or at least thirteen words.
1. If a sentence contains any reflexives (*himself*, *herself*, *itself*), it contains at least two reflexives.
1. A **happy number** is a number such that the sum of the squares of its digits eventually reaches 1. For example, 19 is a happy number because $1^2 + 9^2 = 82$, and $8^2 + 2^2 = 68$, and $6^2 + 8^2 = 100$, and $1^2 + 0^2 + 0^2 = 1$. Imagine any constraint that requires something in language to be a happy number, and you have a constraint that never occurs in a natural language.
:::

::: exercise
Can any of the constraints listed above be enforced by an $n$-gram grammar?
If so, explain how.
:::

::: solution
A simple version of the adjective ordering constraint can be enforced by a bigram grammar.
Let N stand for any noun, V for any adjective that starts with a vowel, and C for any adjective that starts with a consonant.
The string language $\mathrm{V}^*\mathrm{N}\mathrm{C}^*$ is SL-2.
The corresponding positive grammar contains:

- {{{L}}}V
- {{{L}}}N
- VV
- VN
- N{{{R}}}
- NC
- CC
- C{{{R}}}

But if we want to do this for a full language that works like English except that the order of adjectives varies as described, this account fails.
Consider a sentence like *John fed pigeons poison*.
We can adjectives, e.g. *John fed [ugly pigeons nasty] [old poison stale]*.
But since we have *nasty old* in this sentence, we must allow CV as a bigram.
Once we do that, we can also generate *John fed [ugly pigeons nasty old]*, which should be illicit.
:::

::: exercise
You might think the previous example is contrived because there's no utility to those new classes.
So let's consider a case where utility doesn't even factor into things.
Below is a chart showing some made-up English words and what kind of objects this word can refer to.
For example, the first row tells us that blue circles and blue squares are *blip*, whereas red circles and red squares are not *blip*.
Try to infer the meaning of those words from those examples.

~~~ {.include-tikz}
nonceterms_bluered.tikz
~~~

Now consider this expanded chart which also contains information about brown objects.
Is your original hypothesis still correct?
Can you make more or less sense of the words now?

~~~ {.include-tikz}
nonceterms_full.tikz
~~~

Once you're done pondering those questions, go to the end of the unit for a definition of each word.
Do they strike you as particularly natural?
If not, what is it about them that makes them weird?
:::

::: exercise
In general, monomorphemic words (i.e. words that aren't built from smaller parts like *un*) do not have a meaning that involves negation or disjunction.
For example, *unred* or *non-red* are somewhat acceptable ways of talking about things that aren't red, but we can't replaced *non-red* with the monomorphemic *blip*.
:::

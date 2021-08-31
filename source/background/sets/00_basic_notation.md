# Sets: The basics

Sets are the fundamental building block of modern mathematics.
Intuitively, a set is a collection of objects, but with two important twists:

1. Sets are unordered.
1. Sets contain no duplicates.

::: example
Suppose you want to keep a record of which words occur in a text.
You aren't interested in how often a given word occurred, just whether it occurs at all.
Nor do you care in which order the words occurred in the text.
So you are actually interested in the *set* of words that occur in the text.
:::

::: jupyterpython
# Converting a text to the set of words
import re

def text_to_set(text):
    return set(re.findall(r"\w+", text.lower()))

# change the string below as you see fit
text = "If police police police, then police police police."
print("The original text is:")
print(text)
print("The set of words is:")
print(text_to_set(text))
:::

Each property is explained in detail below, but let's first put some helpful notation in place.

## List notation

Sets are often written as lists with curly braces around them.
So $\setof{a, b, c, d}$ denotes the set containing $a$, $b$, $c$, $d$.
Here $a$, $b$, $c$, $d$ are some arbitrary objects.
This is known as **list notation**.
More complex sets are defined with [**set-builder notation**, which will be covered in a later unit](./fixme).

::: example
Consider the string *If John slept, then Mary left*.
Its set of words (ignoring sentence-initial capitalization) is
$\setof{
\text{if},
\text{John},
\text{left},
\text{Mary},
\text{slept},
\text{then}
}$.
:::

::: exercise
Write the following as a set:

- the first names of your three favorite actors/actresses,
- the colors of the rainbow,
- all prime numbers between 1 and 10 (remember, 1 is not a prime number!)

:::

## Elements and set membership

The objects contained in a set are called its **elements** or **members**.
One writes $e \in S$ to indicate that $e$ is an element of $S$.
The opposite is denoted $e \notin S$: $e$ is not an element of $S$.
The symbol $\in$ thus indicates **set membership**.

::: example
Let $W$ be the set of words in the string *If John slept, then Mary left*.
Then it holds that $\emph{left} \in W$ and $\emph{right} \notin W$.
But it is not the case that $\emph{then} \notin W$ or $\emph{awake} \in W$.
:::

Sometimes $\ni$ is used as the mirror image of $\in$.
For example, $a \in S$ could also be written as $S \ni a$.

::: example
Continuing the previous example, it is true that $\emph{left} \in W \ni \emph{then}$.
That is to say, both $\emph{left} \in W$ and $\emph{then} \in W$ are true.
:::

::: exercise
Put $\in$, $\ni$, $\notin$, $\not\ni$ in the gaps below as appropriate:

- $5 \_ \setof{1,2,4,5,8}$
- $6 \_ \setof{1,2,4,5,8}$
- $\setof{5} \_ \setof{1,2,4,5,8}$
- $5 \_ \setof{1,2,4,5,8} \_ 6$

:::

## Lack of order

Even though we may write sets in a linear fashion as lists, they have no internal order.
The set $\setof{a,b}$ could also be written as $\setof{b,a}$.
So we have $\setof{a,b} = \setof{b,a}$, and
$\setof{a,b,c} =
 \setof{a,c,b} =
 \setof{b,a,c} =
 \setof{b,c,a} =
 \setof{c,a,b} =
 \setof{c,b,a}$.

::: example
Consider the strings
*If John slept, then Mary left* and
*If Mary left, then John slept*.
While they are clearly distinct sentences, their sets of words are identical.
:::

::: jupyterpython
import re

def text_to_set(text):
    return set(re.findall(r"\w+", text.lower()))

text1 = "If John slept, then Mary left."
text2 = "If Mary left, then John slept."

set1, set2 = text_to_set(text1), text_to_set(text2)
print("Are the sets identical?")
print("Yes") if set1 == set2 else print("No")
:::

::: exercise
For each one of the following, fill the gap with $=$ or $\neq$ as appropriate:

- $\setof{a,b} \_ \setof{a,b}$
- $\setof{b,a} \_ \setof{a,b}$
- $\setof{b,a,c,d} \_ \setof{e,a,b,d}$

:::

## Lack of duplicates/Idempotency

Sets are **idempotent**, which means that duplicates are ignored.
So $\setof{a,b} = \setof{a,a,b} = \setof{a,b,b,a,b,a,b,a,a}$.
It also holds that $\setof{a} = \setof{a,a} = \setof{a,a,a}$, and so on.

::: jupyterpython
import re

def text_to_set(text):
    return set(re.findall(r"\w+", text.lower()))

text1 = "If John slept, then Mary left."
text2 = "If Mary left, then John slept."

set1, set2 = text_to_set(text1), text_to_set(text2)
print("Are the sets identical?")
print(set1 == set2)
:::

::: example
Linguists distinguish between **word types** and **word tokens**.
The sentence *dogs love dogs* contain two tokens of the type *dogs*, and one token of the type *love*.
The sentences *dogs love* and *dogs love dogs* are different with respect to word tokens, but identical with respect to word types.
So if you care about word types rather than word tokens, you're dealing with a set because the only thing that matters is which words the text contains, not how many tokens of each word.
:::

::: example
Consider the sentence *If police police police, then police police police*.
Its set of words (ignoring capitalization) is 
$\setof{
\text{if},
\text{police},
\text{then}
}$.
:::

::: exercise
For each one of the following, fill the gap with $=$ or $\neq$ as appropriate:

- $\setof{a,b} \_ \setof{a,a,b,b}$
- $\setof{b,a} \_ \setof{a,b,a}$
- $\setof{c,b,a,a,d,c} \_ \setof{a,a,b,d,c,c,c}$
- $\setof{a} \_ \setof{a,a,a,a,a,a,c,a,a,a,a,a,a}$

:::

::: exercise
The sentence *If police police police, then police police police* actually uses two different word types.
It just just so happens that both are pronounced and spelled *police*.
But one is the noun *police*, the other one the verb *police*.
So we might want to annotate the string as follows:
*If police[N] police[V] police[N], then police[N] police[V] police[N]*.
Assume that words are annotated with their part of speech in this fashion.
Then what would be the corresponding set of words?
:::

## Recap

- Sets are collections of arbitrary objects.
- Sets are unordered and idempotent (= duplicates are ignored).
- Sets can be defined with list notation, e.g. $\setof{a, b}$.
- The objects contained in a set are called its *elements* or *members*.
- The symbols $\in$ and $\notin$ are used to indicate membership and non-membership, respectively.
- Occasionally, $\ni$ is used as the mirror image of $\in$.

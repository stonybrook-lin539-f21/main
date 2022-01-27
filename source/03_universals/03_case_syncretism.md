**Prerequisites**

- relations (notation, basic orders)

# Monotonicity in case syncretism

Monotonicity also seems to play a role in a phenomenon called **case syncretism**.
As you probably know, some languages have specific endings that go on nouns to indicate their case.
A subject might usually be nominative case, whereas an object could be accusative or dative, and a possessor might have genitive case.
Case syncretism refers to the phenomenon that a word ends up using identical forms for distinct cases.
Once again not every logically conceivable system is actually attested.
Languages seem to be very finicky in what kinds of case syncretism they allow, and we would like to know why that is so.


## A primer on case syncretism

We still see small reflexes of case syncretism in English, where the personal pronouns have different forms:

| **Word**                      | **Subject** | **Object** | **Possessor** |
| :--                           | :-:         | :-:        | :-:           |
| 3rd person singular masculine | he          | him        | his           |
| 3rd person singular feminine  | she         | her        | her           |
| 3rd person singular neuter    | it          | it         | its           |

The table above is called a **morphological paradigm**, where **morphology** means that we are talking about the form of words, and a **paradigm** is a collection of cells that specify the relation between the forms of a word and their function.
In the case at hand, those functions are subject, object, and possessor.
As you can see, *her* is the form for both the object and the possessor, and *it* is the form for both the subject and the object.
When multiple cells of a paradigm look the same, this is called **syncretism**.

The case system of English is so impoverished by now that it isn't very interesting to look at.
But many languages have a much richer case morphology, and case syncretism is a common occurrence in those languages.
This is shown below for Latin *rex* 'king', where nominative and accusative are syncretic in the plural, as are dative and ablative.

| **Case** | **Singular** | **Plural** |
| --:      | :--          | :--        |
| Nom      | rex          | reg-es     |
| Gen      | reg-is       | reg-um     |
| Dat      | reg-i        | reg-ibus   |
| Acc      | reg-em       | reg-es     |
| Abl      | reg-e        | reg-ibus   |

And Icelandic has paradigms like the one for *mamma* 'mum' below, where almost every form is syncretic with some other form.

| **Case** | **Singular** | **Plural** |
| --:      | :--          | :--        |
| Nom      | mamma        | mömm-ur    |
| Gen      | mömm-u       | mamm-a     |
| Dat      | mömm-u       | mömm-um    |
| Acc      | mömm-u       | mömm-ur    |

As with person pronoun paradigms and adjectival gradation, some conceivable case syncretisms never show up in any language. 
For instance, there is no language with the following variant of the plural case paradigm for 'rex':

| **Case** | **Plural** |
| --:      | :--        |
| Nom      | reg-ibus   |
| Gen      | reg-um     |
| Dat      | reg-ibus   |
| Acc      | reg-es     |
| Abl      | reg-ibus   |

Why is this impossible?
It can't be just because three cases are syncretic, because we've seen that this is fine in Icelandic.
So why does no language like to have a case paradigm of this form?
Again we are forced to explain some typological gaps, and again monotonicity provides an answer.

::: exercise
Pick one of the languages below and write down a case paradigm for a specific word of that language.
Highlight the cells that are syncretic (if any).

- Ancient Greek
- Basque
- Finnish
- German
- Hungarian
- Icelandic
- Japanese
- Korean
- Old English
- Old Norse
- Russian
- Sanskrit
- Tamil

Unless you're a native speaker of one of those languages, you will have to do some research to find out how their case system works.
Try your local library, or an online resource like Wikipedia.
:::


## Genitive, dative and accusative

Case systems can be very complex and convoluted, so we will only focus on a few simple problems here.
First of all, we will only consider syncretism within a single column of the case paradigm.
That is to say, we do not worry how singular forms can be syncretic with plural forms, we're only interested in syncretism among case forms in the singular and syncretism among case forms in the plural.
Second, we won't consider each individual case that has been proposed for some language, because there's tons of them: ablative, locative, elative, instrumental, benefactive, and much more.
Instead, we will subsume them all under *other* and use **Blake's case hierarchy** as our starting point.
Slightly truncated, it postulates that
$$\text{Nom} <
\text{Acc} <
\text{Gen} <
\text{Dat} <
\text{others}$$
The $^*$ABA generalization, which we encountered with adjectival gradation and person pronoun paradigms, can be extended to this hierarchy.
In this broader form, it states that two cases $x$ and $z$ cannot have the same form in a paradigm unless every case $y$ that occurs between them in the hierarchy also has this form in the paradigm.

::: example
The paradigm for Latin *rex* displays syncretism of nominative and accusative to the exclusion of genitive, dative, and ablative.
But since these cases do not occur between nominative and accusative in Blake's case hierarchy, this obeys the $^*$ABA generalization.
:::

::: exercise
The paradigm for *rex* also has syncretism of dative and ablative in the plural.
Can a monotonic function produce this pattern from Blake's case hierarchy?
Justify your answer.
:::

There is a problem with the monotonicity account, though.
In many Germanic languages, dative and accusative are syncretic to the exclusion of genitive.

::: example
In German, it is very common for nominative, dative and accusative to take the base form, whereas genitive receives a special affix.
So *Papa* 'dad' could be nominative, dative, or accusative, whereas the genitive must be *Papas*.
German is not an ideal example, though, as the genitive is becoming increasingly unproductive.
Moreover, the dative allows for a special suffix *-e* for nouns that end in a consonant, so that *Mann* can be either *Mann* or *Manne* (although the latter sounds very archaic).
Nonetheless, it is conceivable that the dative of *Papa* is underlyingly *Papae*, with the final vowel subsequently deleted by some phonological process.
:::

::: example
A better example comes from the Icelandic word for *father*.
The nominative is *faðir*, its dative and accusative are *föður*, yet the genitive is *föðurs*.
And in contrast to German, there's no wiggle room here: these are the endings, and there aren't any colloquial variations.
So accusative and dative are indeed the only syncretic cases, and crucially the genitive case does not participate in this syncretism.
:::

If we combine the $^*$ABA generalization with Blake's hierarchy in its current form, then we cannot produce syncretism of accusative and dative to the exclusion of genitive.
Either the $^*$ABA generalization is too restrictive, or Blake's hierarchy is wrong.
We could of course try to change the hierarchy, but the easy options do not work.

::: exercise
Explain why the following hierarchy is empirically inadequate:
$\text{Nom} <
\text{Gen} <
\text{Acc} <
\text{Dat} <
\text{others}$.
:::

::: exercise
Icelandic also has some nouns where nominative and genitive are syncretic to the exclusion of dative and accusative.
Which variants of Blake's hierarchy does this rule out?
:::


## Partial orders to the rescue

It seems that no matter how we order the cases, at least one attested syncretism will violate the $^*$ABA generalization.
But perhaps we are accidentally limiting ourselves.
First of all, remember that the $^*$ABA generalization is just a linguistic counterpart to the mathematical notion of monotonicity.
Perhaps monotonicity provides a way out?

::: exercise
Pick one of the problematic syncretisms pointed out above and explain why it is also problematic if we replace the $^*$ABA generalization with the requirement that the mapping from the Blake hierarchy to surface forms must be a monotonic function.
:::

Well, monotonicity by itself doesn't really help.
But it opens up a path toward a new solution.
So far, we have implicitly assumed that linguistic hierarchies must be **trichotomous**: for any given $x$ and $y$, it holds that $x < y$, or $y < x$, or $x = y$.

::: example
If we order the natural numbers by $<$, the result is a trichotomous order.
No matter which two numbers $m$ and $n$ we pick, we either have $m < n$, $n < m$, or $m = n$.

Now suppose that we take the set of all humans that have ever lived and order them by the ancestor relation $A$ such that $x \mathrel{A} y$ iff $x$ is an ancestor of $y$.
The resulting order is not trichotomous because there are at least two distinct human beings such that neither one is the other's ancestor.
:::

Trichotomy is a natural starting point for linguistic hierarchies, but it isn't a necessary one.
In contrast to the $^*$ABA generalization, monotonicity is also a meaningful concept if we consider **partial orders**.
In a partial order, some elements may be unordered with respect to each other.
This allows us to make a small but important modification to Blake's hierarchy.

~~~ {.include-tikz size=mid}
blake_partialorder.tikz
~~~

This graph encodes the following orderings of cases:

1. $\text{Nom} < \text{Acc}$,
1. $\text{Nom} < \text{Gen}$,
1. $\text{Acc} < \text{Dat}$,
1. $\text{Gen} < \text{Dat}$,
1. $\text{Dat} < \text{others}$,
1. all the orders that follow from this (e.g. $\text{Nom} < \text{Dat}$).

Notice how genitive and accusative are now unordered with respect to each other.
Monotonicity is a restriction on what a function may map $x$ and $y$ to if $x$ and $y$ are ordered with respect to each other.
But monotonicity has nothing to say for cases where no such ordering holds.
If there is no order between $x$ and $y$, then it does not matter whether $f(x) \leq f(y)$ or the other way round.
Without an ordering between accusative and genitive, it becomes possible for accusative and dative to be syncretic to the exclusion of genitive.

::: example
Suppose that accusative and dative are both mapped to the same exponent, which is different to the realization of genitive: $f(\text{Acc}) = f(\text{Dat}) \neq f(\text{Gen})$.
We will show that this is compatible with the assumption of a monotonically increasing (or decreasing) function.

First, the revised case hierarchy above establishes that $\text{Acc} < \text{Dat}$.
If $f$ is monotonically increasing, then $\text{Acc} < \text{Dat}$ entails $f(\text{Acc}) \leq f(\text{Dat})$.
By our initial assumption, $f(\text{Acc}) = f(\text{Dat})$, which confirms $f(\text{Acc}) \leq f(\text{Dat})$.
Our revised case hierarchy also postulates that $\text{Gen} < \text{Dat}$, so it must be the case that $f(\text{Gen}) \leq f(\text{Dat})$.
Whether this holds depends on how one orders the surface forms, but it is always possible to pick an ordering that satisfies $f(\text{Gen}) \leq f(\text{Dat})$.
Finally, $\text{Acc}$ and $\text{Gen}$ are unordered with respect to each other, and consequently the relative order of $f(\text{Acc})$ and $f(\text{Gen})$ is irrelevant for monotonicity.
:::

::: exercise
For each one of the following syncretisms, state whether it can be realized by a monotonic mapping assuming the modified Blake hierarchy (if necessary, you may assume a different linear order of output forms for each syncretism).
Justify your answer.


- Syncretism of nominative and genitive to the exclusion of accusative
- Syncretism of nominative and dative to the exclusion of accusative
- Syncretism of nominative, accusative, and dative to the exclusion of genitive
- Syncretism of nominative, accusative, and genitive to the exclusion of dative
- Syncretism of accusative and genitive to the exclusion of nominative and dative

:::

It seems, then, that monotonicity does a lot of work even in the richer domain of case syncretisms.
The crucial step is to move from a total order to a partial order.

## Recap

- Linguists often assume that hierarchies are **trichotomous**: all elements of the hierarchy must be ordered with respect to each other.
- If we drop the trichotomy requirement, linguistic hierarchies can be partial orders.
- In contrast to linguistic proposals like the No-Crossing-Branches constraint or the $^*$ABA generalization, monotonicity isn't limited to trichotomous orders.
  It works just as well for partial orders.
- This makes it possible to explain many highly distinct linguistic phenomena in terms of monotonicity.

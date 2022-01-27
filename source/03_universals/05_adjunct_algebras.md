**Prerequisites**

- posets (basics, semilattices)

# Explaining a syntactic universal: the Adjunct Island Constraint

The Person Case Constraint in the previous unit was an instance of monotonicity regulating the shape of sentences, i.e. the **syntax** of a language.
It probably won't surprise you to hear that there is more to syntax than just the Person Case Constraint.
After all, the study of syntax has been around since at least the late 50s, and who would want to spend over 60 years studying just one phenomenon?
Syntax is a smorgasbord of intriguing, somewhat odd phenomena.
One of them is the **Adjunct Island Constraint**, or simply **AIC**.
The AIC is a condition that holds in every natural language we currently know.
It seems to be a universal law of natural language.
So what it is about?
It is about a peculiar contrast, illustrated below for English.

(@) John asserted [that Mary wants to watch which movie]? (good)
(@) Which movie did John assert [that Mary wants to watch]? (good)
(@) John cried [because Mary wants to watch which movie]? (good)
(@) \*Which movie did John cry [because Mary wants to watch]? (bad)

The last sentence is not okay in English, which --- following linguists' convention --- we indicate with an asterisk.
But why isn't this sentence okay.
It has all the needed words, and its meaning is perfectly clear.
Why isn't that okay?
The culprit is the AIC, or, as we will see in this unit, monotonicity all over again.
But in order to get to that point, we first have to put in place some linguistic basics.
If you're already familiar with the AIC, skip ahead to the section on adjunct extensions.


## Linguistic background

### Arguments versus adjuncts

The AIC builds on the long-standing distinction in linguistics between **arguments** and **adjuncts**, and it states that the latter **block movement**.
Well that's quite a mouthful, so let's take it step by step, starting with the split between arguments and adjuncts.

An argument is a phrase that is introduced and required by some other word in the sentence.
For example, in *Yesterday, John devoured twelve pounds of pasta*, both *John* and *twelve pounds of pasta* are arguments of the verb *devour*.
Neither one can be easily removed --- *Yesterday, devoured twelve pounds of pasta* is not well-formed, and neither is *Yesterday, John devoured*.
So the arguments of the verb are a necessary part of the sentence.
We cannot freely throw in additional arguments, either: *Yesterday, John devoured Mary twelve pounds of pasta the whole bowl* is not a good sentence of English.

Adjuncts, on the other hand, are much less tightly controlled than arguments.
They can be removed and added without problem.
The adverb *yesterday* in *Yesterday, John devoured twelve pounds of pasta* is an adjunct, and indeed it can be removed without reducing the well-formedess of the string.
We can also add additional adjuncts, e.g. the adverb *quickly* or the adjective *delicious*.

(@) Yesterday, John quickly devoured twelve pounds of pasta.
(@) Yesterday, John devoured twelve pounds of delicious pasta. 
(@) Yesterday, John quickly devoured twelve pounds of delicious pasta.

Metaphorically speaking, arguments are the essential parts that make up the basic structure of the sentence, like a sentence skeleton.
Adjuncts are the nice but ultimately optional embellishments that we hang from the bones of this skeleton.
That isn't to say that adjuncts are useless --- they often provide useful or even essential information, like *yesterday* in the examples above.
But in contrast to arguments, adjuncts aren't needed for a sentence to be well-formed.


### Movement

When you compare specific sentences of a language, it often looks like a part of the sentence has been moved around.
For instance, in the sentences below it looks like *this car* has moved from its position next to the verb to the beginning of the sentence.

(@) Mary really likes this car.
(@) This car, Mary really likes.

Linguists call this phenomenon **movement** or **displacement**.
Apparently the structure of sentences isn't fully rigid, parts can be shifted around.
Sometimes they move to the left, like in the example above, and sometimes to the right, as in the example below.

(@) The museum displayed a very old mosaic, which dates back all the way to 200BC and allegedly depicts an Etruscan goddess, at its most recent exhibition.
(@) The museum displayed at its most recent exhibition a very old mosaic, which dates back all the way to 200BC and allegedly depicts an Etruscan goddess.

But movement isn't all willy-nilly, there are some restrictions.
For instance, we can't move around the verb in the example below.

(@) The museum closed its exhibition early.
(@) \*Closed, the museum its exhibition early.

This shows that movement, just like most other aspects of language, is subject to an elaborate system of rules and laws.
The AIC is one of those laws.


### The AIC

Let's go back to our initial examples.
The first one contains the clause *that Mary wants to watch which movie*, repeated here:

(@base) John asserted [that Mary wants to watch which movie]?

This clause is an argument of the verb *asserted* (removing the argument leaves us with the rather odd *John asserted*).
In the sentence in (@base), we can move *which movie* all the way to the left.
As a peculiarity of English, this also requires a form of *do* to appear after *which movie* (in many other languages this doesn't happen).

(@good) Which movie did John assert [that Mary wants to watch]?

Now let's contrast this against the other two example sentences.

(@) John cried [because Mary wants to watch which movie]?
(@bad) \*Which movie did John cry [because Mary wants to watch]?

As you can see, *which movie* in (@bad) no longer gets to move to the left edge of the sentence as it did in (@good).
So apparently some law of movement has been violated.
And that law is the AIC.
You see, there is a crucial difference between (@good) and (@bad): a clause that starts with *because* is an adjunct, not an argument.
We can completely remove it from a well-formed sentence and the result is still well-formed.

(@) John cried.

Since the *because*-clause is an adjunct, the AIC does not allow anything to be moved out of it.
When *which movie* tries to sneak all the way to the left edge of the sentence, it is in violation of the AIC. 
As a result, the sentence is ill-formed.

This is the standard linguistic story, and it is supported by tons of evidence.
The AIC seems to be active in every natural language that's currently known to linguists.
But why should the world be this way?
The AIC looks like a pretty arbitrary law, yet it is enforced so stringently.
Why would languages limit movement out of adjuncts but not out of arguments?
Why isn't there a single language that bucks the trend and forbids movement out of arguments instead of adjuncts?
Clearly this isn't some conspiracy where all languages congregated in a smoky backroom and decided that those free-spirited adjuncts need to be taken down a notch.

No, the answer is much simpler.
It's just good ol' monotonicity again.


## Adjunct extensions

If monotonicity is involved in the AIC, then there must also be some underlying order over some set.
Remember, monotonicity states that $x \leq y$ implies $f(x) \leq f(y)$ --- if there is no order $\leq$ to begin with, then monotonicity is vacuous.
We can get such an order directly from the notion of adjuncts.

Given two sentences $s$ and $t$, we can order them with respect to each other based on various criteria.
For instance, we could say $s \leq_l t$ iff the length of $s$ does not exceed the length of $t$.
Or we could say $s \leq_s t$ iff $s$ contains at most as many slurs as $t$.

::: exercise
Neither $\leq_l$ nor $\leq_s$ are weak partial orders.
Remember that a relation is a weak partial order iff it is transitive, antisymmetric, and reflexive.
Which of these properties do not hold of $\leq_l$ or $\leq_s$?
Justify your answer.
:::

Neither $\leq_l$ nor $\leq_s$ are of any use for our problem, though; we need something a bit more sophisticated.
Instead, we will establish an order $\leq_A$ between sentences based on whether one can be obtained from the other by adding 0 or more adjuncts.
In other words, $x \leq_A y$ iff we can turn $x$ into $y$ by adding 0 or more adjuncts.
We say that $y$ is an **adjunct extension** of $x$ iff $x \leq_A y$.

::: example
Among the adjunct extensions of *John devoured twelve pounds of pasta*, we find, among many others:


- *John quickly devoured twelve pounds of pasta.*
- *John devoured twelve delicious pounds of pasta.*
- *John devoured twelve pounds of pasta yesterday.*
- *John quickly devoured twelve delicious pounds of pasta.*
- *John quickly devoured twelve pounds of pasta yesterday.*
- *John devoured twelve delicious pounds of pasta yesterday.*
- *John quickly devoured twelve delicious pounds of pasta yesterday.*


Note that *John devoured twelve pounds of pasta* is an adjunct extension of itself.
By putting parentheses around optional parts, we can represent all of this more succinctly as


- *John devoured twelve pounds of pasta* $\leq_A$ *John (quickly) devoured twelve (delicious) pounds of pasta (yesterday)*


Besides that, all of the following also hold.


- *John quickly devoured twelve pounds of pasta* $\leq_A$ *John quickly devoured twelve (delicious) pounds of pasta (yesterday)*
- *John devoured twelve pounds of pasta yesterday* $\leq_A$ *John (quickly) devoured twelve (delicious) pounds of pasta yesterday*

:::

::: exercise
Fill the gaps with $\leq_A$ or $\geq_A$ as appropriate.
If neither $\leq_A$ nor $\geq_A$ hold, leave the gap empty.

- John slept \_ John definitely slept yesterday
- The old man snored \_ The man snored
- John likes Mary \_ Mary really likes John
- John ate pasta \_ John ate pasta
- John ate pasta \_ John ate

:::

::: exercise
Show that $\leq_A$ is a weak partial order.
That is to say, it is a binary relation that is transitive, antisymmetric, and reflexive.
:::

As we will see next, $\leq_A$ interacts with well-formedness in a particular way.
Understanding this interaction will allow us to derive the AIC from monotonicity.


## The adjunct extension semilattice

Let $L$ be the set of all sentences that can be built using only English words.
Note that these sentences do not have to be well-formed, so $L$ contains both *Mary drives a fancy car* and *car Mary a fancy fancy drive because aardvark this seventeen allegedly*.
The point of $L$ is that we want to have a collection of all the sentences that English could in principle have if there were absolutely no restrictions on what a natural language may look like.

Assuming that we have some way of identifying adjuncts, we can order the sentences in $L$ according to the adjunct extension relation $\leq_A$.
Now pick some sentence $s \in L$.
We will write $A_L(s)$ to denote the set of sentences in $L$ that are adjunct extensions of $s$.
$$A_L(s) \is \setof{ t \mid t \in L \text{ and } s \leq_A t}$$

::: example
Let $s$ be the sentence
*John really likes Mary*.
Then $A_L(s)$ contains infinitely many sentences, including


- John really likes Mary.
- John really, really likes Mary.
- John really likes Mary because she looks like Sue.
- and so on


But it also includes infinitely many sentences that wouldn't actually be good English sentences, e.g. *John because yesterday she looks like Sue adores really Mary really red*.
:::

::: exercise
Suppose that $s$ is *The old men quickly manned the boat*.
Write down five members of $A_L(s)$.
:::

When we order $L$ with the partial order $\leq_A$, we turn it into a partially ordered set, i.e. a **poset**.
We can do the same thing with $A_L(s)$.

::: example
Let's consider a small fragment of $A_L(\mathit{John\ snored})$.
It contains


- John snored.
- John snored yesterday.
- John really snored.
- John really snored yesterday.
- Allegedly, John really snored yesterday.
- John really, really snored yesterday.
- John really, really, really snored yesterday.


When we order these sentences by $\leq_A$, we get the structure depicted below.

~~~ {.include-tikz size=mid}
adjunctextension.tikz
~~~

We could've also drawn it upside-down with *John snored* at the top, this does not make a difference.
:::

::: exercise
Continuing the previous exercise, draw the corresponding figure for your fragment of $A_L(s)$.
:::

When we order $A_L(s)$ with $\leq_A$, we don't just get any poset, we get a particular type of poset that's a **semilattice**.
More precisely, it is a **meet semilattice**.
Nice, another fancy term for your vocabulary, but this one sounds a lot scarier than it actually is.
You can check out the backgrounds section for all the math, but for our purposes a visual example suffices.

::: example
Consider once more the fragment from the previous example, sorted by $\leq_A$.
Pick two elements $x$ and $y$, for instance *Allegedly, John really snored yesterday* and *John really, really, really snored yesterday*.
Put your fingers on those sentences.
Now move your fingers downward, tracing a path towards the bottom element *John snored*.
The **meet** $x \wedge y$ is the earliest point where your fingers can meet.
In the case at hand, that's *John really snored yesterday*.

The meet of *John really, really, really snored yesterday* and *John really, really snored yesterday* is just *John really, really snored yesterday*.
After all, the earliest point your fingers can meet is if you move the higher one down by one step while keeping the lower where it is.
:::

A poset is a meet semilattice iff it holds for all elements $x$ and $y$ that they have a unique meet.
This is the case for $A_L(s)$ no matter what sentence we pick for $s$.
But there are posets that do not meet this condition.

::: example
Consider the structure below.
Even though it is a poset, it is not a meet semilattice because $a$ and $b$ have no meet.

~~~ {.include-tikz size=mid}
poset_nomeet.tikz
~~~
:::

::: example
The structure below is also a poset that fails to be a meet semilattice.

~~~ {.include-tikz size=mid}
poset_nouniquemeet.tikz
~~~

In this case, the problem is that there is no unique meet for $a$ and $b$. 
Both $c$ and $d$ are viable choices, which violates the requirement that the meet must be unique.
:::

::: exercise
Suppose we take the set of natural numbers and order it by $\leq$ in the usual way, yielding a single line of numbers.
Is this a meet semilattice?
Justify your answer.
:::

::: example
Finally, the structure below isn't a meet semilattice either.
Even though it consists of two parts, each one of which forms a semilattice, there's many pairs of elements that do not have meet, e.g. $c$ and $x$.
As one missing meet is enough to prevent a poset from being a semilattice, this shows that the structure isn't as semilattice.

~~~ {.include-tikz size=mid}
poset_union.tikz
~~~

:::

The structure in the last example is exactly what we find with the poset $L$ ordered by $\leq_A$.
Each sentence $s$ that does not contain any adjuncts is the bottom element of a meet semilattice that consists of $s$ and all its adjunct extensions.
But $L$, even though it is a collection of such meet semilattices, is not itself a meet semilattice because adjunct extensions of distinct sentences simply have no meet.
Their semilattices are like little islands with no land connection between them.
The poset $L$ ordered by $\leq_A$ is the archipelago that consists of all these islands.

~~~ {.include-tikz size=large}
aic_semilattices.tikz
~~~


## Optionality and well-formedness entailments

All the math so far has served the purpose of identifying relations between possible sentences.
We collect all logically conceivable sentences, including ill-formed ones, and say that if $t$ can be obtained from $s$ by adding finitely many adjuncts, then $t$ is an adjunct extension of $s$.
This turns a language from a simple set of sentences into a poset whose structure encodes how strings are related with respect to adjuncts.

Now remember from earlier on that adjuncts have a crucial property: they are optional.
That is to say, if a sentence containing an adjunct is grammatical, it should still be grammatical after removal of the adjunct.

::: example
The sentence
*Yesterday John definitely snored loudly*
is well-formed, and so is every sentence that it is an adjunct extension of:


- Yesterday John definitely snored loudly
- Yesterday John definitely snored
- Yesterday John snored loudly
- John definitely snored loudly
- Yesterday John snored
- John definitely snored
- John snored loudly
- John snored

:::

In the other direction, adding an adjunct cannot make an ill-formed sentence grammatical.

::: example
The sentence
*John meet*
is ill-formed,
and so are
*John meet yesterday*,
*John definitely meet*,
*John really, really meet*,
and all other adjunct extensions of the sentence.
:::

If we take optionality in this sense as an intrinsic property of adjuncts, then we can use the structure of $L$ under $\leq_A$ to infer the well-formedness of one string from another.
In particular, the following two laws follow from optionality:

1. If $s$ is well-formed, then so is every string that $s$ is an adjunct extension of.
1. If $s$ is ill-formed, then so is every adjunct extension of $s$.

In other words, well-formedness travels downward in each meet semilattice $A_L(s)$, and ill-formedness travels upward.

::: exercise
Explain why these entailments follow from the optionality of adjuncts.
:::


## Monotonicity derives the AIC

Alright, so we've covered a lot of linguistics ground, with arguments, adjuncts, and movement, and we've covered a lot of math ground, with meet semilattices.
But I promised you an explanation of the AIC, and in particular I promised you an explanation in terms of monotonicity.
Nothing said so far has anything to do with monotonicity.
But the connection is easily made.
Here's another way of saying that grammaticality travels downward and ungrammaticality travels upward: the mapping from $L$ ordered by $\leq_A$ into the poset $\mathbf{2}$ of truth values must be --- you guessed it --- monotonic!

Consider any function $f$ from $L$ to $\mathbf{2}$, the structure of truth values $T$ and $F$.
Usually the order on $\mathbf{2}$ states $F \leq_2 T$, but we will switch it to $T \leq_2 F$ (this is innocuous, it only means that the relevant mapping will be monotonically increasing instead of monotonically decreasing).
If $f(s) = T$, then $s$ is well-formed, otherwise it is ill-formed.

::: exercise
Explain why a monotonically increasing function from $L$ to $\mathbf{2}$ with $F \leq_2 T$ must be monotonically decreasing if we do exactly one of the following:

- switch the order to $T \leq_2 F$,
- switch the order $\leq_A$ in $L$.

:::

Now consider two strings $s$ and $t$ such that $s \leq_A t$.
Suppose $f(t) = T$.
Since grammaticality travels downward, this entails $f(s) = T$.
But we get the very same inference from monotonicity:

1. If $s \leq_A t$, then $f(s) \leq_2 f(t)$.
1. We know that $f(t) = T$, and therefore $f(s) \leq_2 T$.
1. But $T \leq_2 F$, so $f(s) \leq_2$ implies $f(s) = T$.

Now let us look at the other case.
Suppose $f(s) = F$.
Then $f(t) = F$ because ungrammaticality travels upward.
Once again monotonicity gives us the same inference:

1. If $s \leq_A t$, then $f(s) \leq_2 f(t)$.
1. We know that $f(s) = F$, and therefore $F \leq_2 f(t)$.
1. But $T \leq_2 F$, so $F \leq_2 f(t)$ implies $f(t) = F$.

And this is the key to the AIC.
To recap, here's what we've done so far:

1. We have adopted the linguistic distinction between arguments and adjuncts.
1. We have ordered the set of all conceivable (but not necessarily well-formed sentences) by the adjunct extension.
   This gives us a poset that is a collection of meet semilattices.
1. Because adjuncts are optional, grammaticality travels downwards in this poset, whereas ungrammaticality travels upward.
1. We have shown that the way grammaticality and ungrammaticality travel through the structure is once again an instance of monotonicity.

At this point, we have actually derived the AIC from monotonicity.
You might not see it clearly yet, but think about it.
Consider once more the contrast this unit started out with (I know, that was ages ago).

(@) John asserted [that Mary wants to watch which movie]? (good)
(@) Which movie did John assert [that Mary wants to watch]? (good)
(@) John cried [because Mary wants to watch which movie]? (good)
(@bad2) \*Which movie did John cry [because Mary wants to watch]? (bad)

We have to explain why (@bad2) is bad.
But we already have!
The sentence in (@bad2) contains a *because*-clause, which is an adjunct.
This means that (@bad2) is an adjunct extension of *which movie did John cry*.
That's not a grammatical sentence of English.
But if *which movie did John cry* is ungrammatical, then by monotonicity this must also be true for all its adjunct extensions, including (@bad2).
So there you have it, the explanation of the AIC: it's not that movement out of an adjunct isn't allowed, but rather the optionality of adjuncts creates monotonic entailment relations that simply make it impossible for such a sentence to be allowed.

## Recap

- Languages do not need to be flat, unstructured sets, we can define orders over the sentences they contain.
- One particular order is the adjunction extension order $\leq_A$: $s \leq_A t$ iff $t$ can be built by adding 0 or more adjuncts to $s$.
- A language with this order is a partially ordered set, or **poset**.
- More specifically, it is a collection of **meet semilattices**.
- Because of the optionality of adjuncts, we get specific entailments over each one of these semilattices:

    - ungrammaticality travels upward: if $s$ is ill-formed, then so is every adjunction extension $t$ of $s$ (adjuncts cannot repair ill-formed sentences);
    - grammaticality travels downward: if $t$ is well-formed, then so is every sentence $s$ that $t$ is an adjunct extension of (adjuncts aren't needed for well-formedness).

- But this is the same as saying that the mapping from $L$ to $\mathbf{2}$, the poset of truth values, must be monotonic.

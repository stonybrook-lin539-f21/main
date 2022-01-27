**Prerequisites**

- sets (notation, operations, cardinality)

# Comparing sets

Two sets can stand in several distinct relations to each other:

1. subset
1. superset
1. identity
1. proper subset
1. proper superset
1. disjoint
1. incomparable


## Subset and superset

Given two sets $A$ and $B$, $A$ is a **subset** of $B$ iff every element of $A$ is also an element of $B$.
In this case, one writes $A \subseteq B$.
For example, $\setof{a,b} \subseteq \setof{a,b,c,d}$.
Alternatively, one also says in this case that $B$ is a **superset** of $A$ (written $B \supseteq A$).

::: example
A transitive verb is a verb that occurs with a subject and an object: *devour*, *contradict*, *wager*, *flummox*, and many more.
Not all verbs are transitive, e.g. *sleep* or *give*. 
Suppose $T$ is the set of all English transitive verbs, whereas $V$ is the set of all English verbs.
Since every transitive verb is a verb, but no the other way round, we have $T \subseteq V$.
:::

By the definition of subset, every set $S$ is a subset of itself.
The reasoning is simple.
If $S \subseteq S$, then every member of $S$ must be a member of $S$, which is obviously true (how could it be otherwise?).

In addition, the empty set is a subset of every set, including itself.
This is because the empty set contains no elements at all, so it trivially holds that every member of the empty set is a member of every set.

::: exercise
Complete the table below.

| A             | B                 | $A \subseteq B$? | $A \supseteq B$? | 
| :--           | :--               | :--              | :--              | 
| $\setof{a,b}$ | $\setof{a,a,b,c}$ |                  |                  | 
| $\setof{a}$   | $\setof{b}$       |                  |                  | 
| $\setof{}$    | $\setof{a}$       |                  |                  | 
| $\setof{a,b}$ | $\setof{a,a,b,b}$ |                  |                  | 

:::


::: jupyterpython
def set_print(some_set):
    return '{' + ', '.join(sorted(list(some_set))) + '}'

# adapt the sets as necessary
set1 = set(['a', 'b'])
set2 = set(['a', 'a', 'b', 'c'])

if set1.issubset(set2):
    print(set_print(set1), "is a subset of", set_print(set2))
else:
    print(set_print(set1), "is not a subset of", set_print(set2))
:::

::: exercise
Say whether the following statement is true or false and justify your answer:
for any two sets $A$ and $B$, $A \subseteq B$ iff $A \cap B = A$.
:::

## Identity

Two sets are *identical* iff each one is a subset of the other.
In formal terms, $A = B$ iff both $A \subseteq B$ and $B \subseteq A$ hold.
The reason for this is again simple:

1.  If two sets $A$ and $B$ are identical, then they must contain exactly the same elements.
    But then every member of $A$ is a member of $B$, which implies $A \subseteq B$.
    And it's also the case that every member of $B$ is a member of $A$, so that we have $B \subseteq A$, too.

1.  In the other direction, if $A \subseteq B$ and $B \subseteq A$, then every member of $A$ is a member of $B$, and every member of $B$ is a member of $A$.
    But that can only happen if the sets are identical.


## Proper subset and superset

We call $A$ a **proper subset** of $B$ ($A \subsetneq B$) iff $A$ is a subset of $B$ but $A$ and $B$ are not identical.
In other words, every element of $A$ is a member of $B$, but not every element of $B$ is a member of $A$.
We also say that $B$ is a **proper superset** of $A$ ($B \supsetneq A$).

::: example
Given our previous discussion, the set $T$ of transitive verbs is proper subset of the set $V$ of verbs because it is a subset but not every verb is a transitive verb.
In other words, $T \subseteq V$ yet $T \neq V$.
Hence $T \subsetneq V$.
:::

::: exercise
Fill in $=$, $\subsetneq$, or $\supsetneq$ as appropriate.


- $\setof{a,b} \_ \setof{a}$
- $\setof{a,a,b,c} \_ \setof{b,b,a,c}$
- $\setof{1,2,3} \_ \setof{n + 5 \mid n \in \setof{-4, -3}}$
- $\emptyset \_ \setof{a}$
- $\emptyset \_ \setof{\emptyset}$

:::

## Disjoint and incomparable sets

If there are two sets $A$ and $B$ such that neither $A \subseteq B$ nor $B \subseteq A$, then there can be only two scenarios.
One option is that $A$ and $B$ are **disjoint**, which means that there is no $x$ such that both $x \in A$ and $x \in B$ --- the two sets have absolutely no overlap.
In mathematical terms, $A \cap B = \emptyset$.
Alternatively, $A$ and $B$ might be **incomparable**.
In this case the two sets have a limited overlap such that there is at least one $x$ with both $x \in A$ and $x \in B$, but there are also $a \in A$ and $b \in B$ such that $a \notin B$ and $b \notin A$.

::: example
The set of English prepositions (*on*, *to*, *at*, ...) and the set of English determiners (*a*, *the*, *this*, ...) have not a single word in common and thus are disjoint.
The set of English verbs and the set of English nouns, on the other hand, are incomparable.
Many words like *water*, *cut*, *fall*, *love*, *try*, *judge*, *beat*, or *cross* can be used as nouns or verbs, but many other words are used only as nouns (*tree*, *waterfall*, *idea*, *Ferrari*) or only as verbs (*write*, *convince*, *admonish*).
:::

Remember that it is possible for both $A \subseteq B$ and $B \subseteq A$ to be true --- in this case, $A = B$.
But there can be no $A$ and $B$ such that $A \subsetneq B$ and $B \subsetneq A$.

::: exercise
For each line in the table, say whether the sets are disjoint, incomparable, identical, or stand in a proper subset/superset relation.

| A               | B                                                 | 
| :--             | :--                                               | 
| $\setof{2,5,8}$ | the set of all odd numbers                        | 
| $\setof{a,b,c}$ | $\setof{a,b} \cup (\setof{a,c} - \setof{b,d})$    | 
| $\emptyset$     | $\setof{a,b} \cap (\setof{a,c} - \setof{b,d})$    | 
| $\emptyset$     | $\setof{a,b} \cap (\setof{a,c} \cap \setof{b,d})$ | 
   
:::

## Remarks on notation

### Similarity to $\leq$ and $\geq$

Students sometimes confuse the symbols $\subseteq$ and $\supseteq$.
To avoid that, just keep in mind that these symbols are modeled after $\leq$ and $\geq$ for numbers.
Just like $x \leq y$ means that $x$ is at most as large as $y$, $x \subseteq y$ tells us that $x$ contains at most all the elements of $y$, and nothing else.

### A note on $\subset$

You may occasionally come across the symbol $\subset$ in other math texts.
Some authors use $\subset$ instead of $\subseteq$, while others use it for $\subsetneq$.
As you might imagine, this can be very confusing for the reader, so it's best to avoid $\subset$ and use $\subseteq$ and $\subsetneq$ instead.

### And then there's $\not\subseteq$

Sometimes we might just want to say that $A$ is not a subset of $B$.
We could paraphrase this, as in "it is not the case that $A \subseteq B$".
But mathematicians like to use symbols for common phrases, so there's a dedicated symbol for this: $\not\subseteq$.
Careful, do not confuse $\not\subseteq$ with $\subsetneq$.

Here's an overview of all the relevant notation:

| **Formula**         | **means...**                                                                 |
| :-:                 | :--                                                                          |
| $A \subseteq B$     | $A$ is a subset of $B$ (holds even if $A = B$)                               |
| $A \subsetneq B$    | $A$ is a proper subset of $B$ ($A \subseteq B$ and $A \neq B$)               |
| $A \not\subseteq B$ | $A$ is not a subset of $B$ ($A \ni a \notin B$ for some $a$) |

As you might have expected, there's corresponding counterparts for superset: $\supseteq$, $\supsetneq$, $\not\supseteq$.
But there is no standardized symbol for sets being incomparable, although some authors like to use $\sim$ for this purpose.

## Recap

::: definition
Let $A$ and $B$ be arbitrary sets.
Then $A$ is a **subset** of $B$ ($A \subseteq B$) iff every member of $A$ is a member of $B$.
In this case, $B$ is a **superset** of $A$ ($B \supseteq A$).
:::

::: definition
For $A$ and $B$ arbitrary sets, $A$ is a **proper subset** of $B$ ($A \subsetneq B$) iff $A \subseteq B$ and there is a $b \in B$ such that $b \notin A$.
Similarly, $B$ is a **proper superset** of $A$ ($B \supsetneq A$).
:::

::: definition
Let $A$ and $B$ be arbitrary sets.
Then $A$ and $B$ are:


- **identical** iff $A \subseteq B$ and $B \subseteq A$ both hold,
- **disjoint** iff $A \cap B = \emptyset$,
- **incomparable** iff $A \not\subseteq B$ and $B \not\subseteq A$ and $A \cap B \neq \emptyset$.

:::

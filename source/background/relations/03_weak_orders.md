# Weak order relations

Once you have a firm understanding of strict orders, weak orders are very simple: a weak order is a strict order that is reflexive instead of irreflexive.
That is to say, every element is related to itself.
In the figurative format we have used, this means that every node also has a loop back to itself (although this loop is usually not drawn if it's already known that we're dealing with a weak order).
The typical example of a weak order is $\leq$ over natural numbers, which only differs from $<$ in that $x \leq x$ while $x \not< x$.
This small difference to strict orders is pretty much all there is to weak orders, but this minor change requires a few changes in our definitions.

## Weak orders

The definition of weak orders replaces the irreflexivity property of strict orders with a reflexivity requirement.
Since reflexive relations cannot be asymmetric, asymmetry is weakened to **antisymmetry**.

::: definition
A **weak partial order** is a binary relation $R$ that is


- **transitive**: for all $x, y, z$, $x \mathrel{R} y$ and $y \mathrel{R} z$ jointly imply $x \mathrel{R} z$, and
- **reflexive**: it holds for every $x$ that $x \mathrel{R} x$, and
- **antisymmetry**: for all $x$ and $y$, if $x \mathrel{R} y$ and $y \mathrel{R} x$, then $x = y$.

:::

Just like strict total orders are strict partial orders that are semi-connex, weak total orders are weak partial orders that are **connex**.

::: definition
A **weak total order** is a weak partial order that is **connex**: for all $x$ and $y$, it holds that $x \mathrel{R} y$ or $y \mathrel{R} x$.
:::

## Reflexivity

Reflexivity is a very simple property: a relation is reflexive iff every element is related to itself.

::: definition
Let $R$ be a binary relation over $D$.
Then $R$ is **reflexive** iff it holds for all $x \in D$ that $x \mathrel{R} x$.
:::

If there is at least one element that is not related to itself, the relation is not reflexive.
However, that does not imply that the relation is irreflexive, as that is only the case if not a single element is related to itself.
In cases where some but not all elements are related to themselves, the relation is **non-reflexive**.

::: example
The "same height" relation is reflexive as everything has the same height as itself.
There simply cannot be any object $x$ such that $x$ does not have the same height as $x$.
:::

::: example
Suppose that John voted for Mary, and Mary voted for herself.
We can represent this as a relation $R$ such that
$\text{John} \mathrel{R} \text{Mary}$
and
$\text{Mary} \mathrel{R} \text{Mary}$.
This relation is not reflexive because $\text{John} \not\mathrel{R} \text{John}$.
But it isn't irreflexive either because $\text{Mary} \mathrel{R} \text{Mary}$.
Hence it is non-reflexive.
:::

::: example
Here's a surprising one: there is a relation that is both reflexive and irreflexive.
It's the **empty relation** $R$, whose domain is the empty set $\emptyset$.
In this case, there is no $x \in D$ such that $x \mathrel{R} x$, which means that $R$ is irreflexive.
But there's also no $x \in D$ such that $x \not\mathrel{R} x$, which is the same as saying that $x \mathrel{R} x$ holds for every $x \in D$ (there simply happen to be no $x$ in $D$).
Consequently, $R$ is also reflexive.
:::

::: exercise
There is no relation that is reflexive, and irreflexive, and non-reflexive.
Explain why!
:::

::: exercise
For each one of the following relations, say whether it is reflexive, irreflexive, or non-reflexive.
Justify your answers!
If you have to make additional assumptions, explain what they are. 


- the "younger than" relation
- the "sums to 10" relation ($x \mathrel{R} y$ iff $x + y = 10$)
- the "at least as rich as" relation
- the "voted for the same candidate" relation
- the "parent-of" relation over humans in a world with time travelling
- the "reverse" relation over words ($x \mathrel{R} y$ iff $x$ is $y$ read backwards; e.g. *deer* and *reed*)

:::

::: exercise
Say whether the following claim is true or false, and justify your answer: If there are $x$ and $y$ in the domain $D$ of $R$ such that $x \mathrel{R} y$, then it is impossible for $R$ to be reflexive and asymmetric.
:::

Reflexivity is the crucial difference between weak and strict orders.
The former are reflexive, the latter irreflexive.
All other differences are just a consequence of trying to accommodate this split between reflexivity and irreflexivity:

- Antisymmetry is a weakened version of asymmetry that allows for reflexivity.
- Semiconnexity is a weakened version of connexity that allows for irreflexivity.

## Antisymmetry

A relation is antisymmetric if it ensures as much asymmetry as possible without losing reflexivity.

::: definition
Let $R$ be a relation over $D$.
Then $R$ is **antisymmetric** iff $x \mathrel{R} y$ and $y \mathrel{R} x$ jointly imply $x = y$ for all $x, y \in D$.
:::

::: example
The familiar relation $\leq$ over natural numbers is antisymmetric since $x \leq y$ and $y \leq x$ cannot both be true unless $x = y$.
:::

::: example
The sibling-of relation is not antisymmetric.
That John is a sibling of Mary and Mary is a sibling of John does not entail that John and Mary are the same person.
:::

Here's a slightly confusing point.
Since antisymmetry is a weakened version of asymmetry, every asymmetric relation is also antisymmetric.

::: example
The relation $<$ is antisymmetric.
The only way for antisymmetry to fail would be if there were $x$ and $y$ such that $x \neq y$ yet $x < y$ and $y < x$.
But clearly there can be no natural numbers such that $x < y$ and $y < x$.
So antisymmetry is satisfied by virtue of $<$ being asymmetric.
:::

::: exercise
Show that every relation that is both irreflexive and antisymmetric is asymmetric.
:::

Keep in mind that antisymmetry is not the opposite of asymmetry.
That would be **symmetry**.

::: definition
Let $R$ be a binary relation over $D$.
Then $R$ is **symmetric** iff it holds for all $x$ and $y$ in $D$ that $x \mathrel{R} y$ implies $y \mathrel{R} x$.
:::

::: example
Consider the "difference is 10" relation over integers, where $x \mathrel{R} y$ iff $|x - y| = 10$ ($|n|$ is the value of $n$, e.g. $|5| = 5$ and $|-5| = 5$).
This relation is symmetric.
It is always the case that $|x - y| = |y - x|$, for instance $|15 - 5| = |5 - 15| = 10$.
So if $|x - y| = 10$, then $|y - x| = 10$.
Hence $x \mathrel{R} y$ implies $y \mathrel{R} x$, exactly as required by symmetry.


You might object that there are many choices for $x$ and $y$ whose difference isn't $10$, for example $|5 - 2| = 3$.
But that's immaterial for symmetry.
Symmetry has nothing to say about relations between arbitrary elements, it only tells us that if $x$ is related to $y$, then $y$ is related to $x$.
If $x$ isn't related to $y$ to begin with, then symmetry simply doesn't care.
:::

::: exercise
Say whether the following claim is true or false, and justify your answer: If there are $x$ and $y$ in the domain $D$ of $R$ such that $x \mathrel{R} y$, then it is impossible for $R$ to be transitive, symmetric, and irreflexive.
:::

If a relation is neither symmetric, nor asymmetric, nor antisymmetric, then it is **non-symmetric**.

::: example
Consider the relation $R$ such that $x \mathrel{R} y$ iff $x \leq y$ or $|x| = |y|$.
This relation is not symmetric.
For instance, $2 \leq 3$ entails that $2 \mathrel{R} 3$ holds, yet we do not have $3 \mathrel{R} 2$ because neither $3 \leq 2$ nor $|3| = |2|$ are true.
It is not asymmetric because it is reflexive: $x \mathrel{R} x$ always holds because $x \leq x$.
Yet it is not antisymmetric either.
This is witnessed by $-2 \mathrel{R} 2$ and $2 \mathrel{R} -2$ (because $|-2| = |2|$) even though $-2 \neq 2$.
With all symmetry options exhausted, this only leaves us to conclude that $R$ is non-symmetric.
:::

::: example
The empty relation is symmetric, asymmetric, and antisymmetric.
That's because its domain is the empty set. 
If there are no $x$ and $y$ such that $x \mathrel{R} y$, then it is impossible to violate symmetry, asymmetry, or antisymmetry.
Hence, all three variations of symmetry hold simultaneously.
However, this also means that the empty relation is not non-symmetric.
:::

::: exercise
For each one of the following relations, say whether it is symmetric, asymmetric, antisymmetric, or non-symmetric.
Be as specific as possible: don't just say "antisymmetric" if the relation is also asymmetric, in that case you should answer "asymmetric".
Take care to justify your answers, and if you have to make additional assumptions, explain what they are. 

- the "younger than" relation
- the "sums to 10" relation ($x \mathrel{R} y$ iff $x + y = 10$)
- the "at least as rich as" relation
- the "voted for the same candidate" relation
- the "parent-of" relation over humans in a world with time travelling
- the "reverse" relation over words ($x \mathrel{R} y$ iff $x$ is $y$ read backwards; e.g. *deer* and *reed*)
- the lexicographic order of words in a dictionary

:::


## Connexity

A relation is **connex** iff it is reflexive and semi-connex.
Remember that a relation is semi-connex iff $x \mathrel{R} y$ or $y \mathrel{R} x$ hold if $x$ and $y$ are distinct elements.
But if a relation is reflexive, then $x \mathrel{R} y$ is necessarily the case whenever $x = y$.
So we can just drop the requirement that $x$ and $y$ are distinct and stipulate that $x \mathrel{R} y$ or $y \mathrel{R} x$ holds no matter whether $x = y$ or $x \neq y$.

::: definition
A relation $R$ over set $D$ is **connex** iff $x \mathrel{R} y$ or $y \mathrel{R} x$ holds for all $x, y \in D$.
:::

::: exercise
Indicate in the table below which properties hold of the relations.

| **Relation**                  | **transitive** | **reflexive** | **anti-symmetric** | **connex** |
| :--                           | :--            | :--           | :--               | :--         |
| substring                     |                |               |                   |             |
| $\subsetneq$                  |                |               |                   |             |
| $\subseteq$                   |                |               |                   |             |
| alphabetical order            |                |               |                   |             |
| taller than                   |                |               |                   |             |

:::


## Overview of strict and partial orders

With all those different notions of reflexivity, symmetry, and connexity, it is easy to get confused about the various types of orders.
But they are all very similar, in fact.
The key difference between weak and strict orders is whether the relation is reflexive or irreflexive.
The key difference between partial and total orders is whether semi-connexity holds.

Here is a tabular overview based on the definitions in this and the preceding unit.
The use of ~ indicates that the property may or may not be satisfied

| **Property**                      | **Weak partial** | **Strict partial** | **Weak total** | **Strict total** |
| :--                               | :--              | :--                | :--            | :--              |
| transitive                        | Y                | Y                  | Y              | Y                |
| reflexive                         | Y                | N                  | Y              | N                |
| irreflexive                       | N                | Y                  | N              | Y                |
| asymmetric                        | N                | Y                  | N              | Y                |
| antisymmetric                     | Y                | Y                  | Y              | Y                |
| semi-connex                       | ~                | ~                  | Y              | Y                |
| connex                            | ~                | ~                  | Y              | N                |

For the sake of completeness, let's include all the other properties of relations we discussed in this unit.

| **Property**                      | **Weak partial** | **Strict partial** | **Weak total** | **Strict total** |
| :--                               | :--              | :--                | :--            | :--              |
| transitive                        | Y                | Y                  | Y              | Y                |
| reflexive                         | Y                | N                  | Y              | N                |
| irreflexive                       | N                | Y                  | N              | Y                |
| non-reflexive                     | N                | N                  | N              | N                |
| symmetric                         | N                | N                  | N              | N                |
| asymmetric                        | N                | Y                  | N              | Y                |
| antisymmetric                     | Y                | Y                  | Y              | Y                |
| non- symmetric                    | N                | N                  | N              | N                |
| semi-connex                       | ~                | ~                  | Y              | Y                |
| connex                            | ~                | ~                  | Y              | N                |

Some of these properties, like symmetry, aren't useful for separating the four types of orders, but will allow us later on to distinguish them from equivalence relations or preorders.

Still, the tables above can be simplified quite a bit:

1.  Remember that every asymmetric relation is also antisymmetric.
    And every irreflexive, antisymmetric relation is asymmetric.
    For the purposes of distinguishing weak and strict partial orders, we don't really need to list asymmetry.
    It's enough to know that both are antisymmetric relations that are either reflexive or irreflexive.

1.  Similarly, every connex relation is semiconnex.
    And if a relation is reflexive and semi-connex, then it is connex.
    So we don't need to list connexity either.
    All we need to say is that partial orders are reflexive and semi-connex whereas strict orders are irreflexive and semi-connex.
    
Hence, we can make do with a much shorter table.

| **Property**                  | **Weak partial** | **Strict partial** | **Weak total** | **Strict total** |
| :--                           | :--              | :--                | :--            | :--              |
| transitive                    | Y                | Y                  | Y              | Y                |
| antisymmetric                 | Y                | Y                  | Y              | Y                |
| reflexive                     | Y                | N                  | Y              | N                |
| irreflexive                   | N                | Y                  | N              | Y                |
| semi-connex                   | ~                | ~                  | Y              | Y                |

All four types of orders now share the common core of being transitive and antisymmetric (which separates them from other order relations).
Reflexivity determines if the order is weak or strict.
Semi-connexity determines if the order is partial or total.

::: definition
A binary relation $R$ over domain $D$ is


- a **weak partial order** iff it is transitive, antisymmetric, and reflexive
- a **strict partial order** iff it is transitive, antisymmetric, and irreflexive
- a **weak total order** iff it is transitive, antisymmetric, semi-connex, and reflexive
- a **strict total order** iff it is transitive, antisymmetric, semi-connex, and irreflexive

:::

::: exercise
Indicate for each relation in the table below what kind of order it represents.
Some relations fit multiple types, and some none.
:::

| **Relation**                  |  **weak partial** | **strict partial** | **weak total** | **weak strict** |
| :--                           |  :--              | :--                | :--            | :--             |
| substring                     |                   |                    |                |                 |
| $\subsetneq$                  |                   |                    |                |                 |
| alphabetical order            |                   |                    |                |                 |
| ordering all humans by height |                   |                    |                |                 |
| "sums to 10" relation         |                   |                    |                |                 |
| parent-of relation            |                   |                    |                |                 |
| "voted for same candidate"    |                   |                    |                |                 |

::: exercise
Give a real-world example of a weak partial order that is not a total order.
:::

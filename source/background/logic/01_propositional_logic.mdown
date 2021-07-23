# Propositional logic

Propositional logic formalizes the entailments that arise when propositions are built up from smaller propositions.

## Intuition

We are given a non-empty set of **proposition symbols** $p$, $q$, $r$, and so on.
This set might be infinite.
We also have an **assignment** that tells us for proposition symbol whether it is true (1) or false (0).

We can combine propositions with four operators:

| **Operator**      | **Meaning**    |
| :-:               | :--            |
| $\wedge$          | and            |
| $\vee$            | or             |
| $\rightarrow$     | if-then        |
| $\leftrightarrow$ | if and only if |

::: example
Let $p$ and $q$ be short for *Sue smokes* and *John likes fish*, respectively.
Here are some of the combinations that are possible this way:


- $p \wedge q$: *Sue smokes and John likes fish.*
- $p \vee q$: *Sue smokes or John likes fish.*
- $p \rightarrow q$: *If Sue smokes then John likes fish.*
- $p \leftrightarrow q$: *Sue smokes if and only if John likes fish.*

:::

In addition, we can use the negation operator $\neg$ to switch the truth value of a proposition symbol to its opposite.

::: example
Suppose that $p$ corresponds to the proposition *Sue smokes*.
Then $\neg p$ is equivalent to *It is not the case that Sue smokes*.
If $p$ is true, $\neg p$ is false, and the other way round.
:::


## Formal definition

Every logic is defined in terms of two components.
Its **syntax** describes the shape of the logical expressions, whereas the **semantics** specifies how these expressions are to be interpreted.
For propositional logic, the syntactic component revolves around combining propositional symbols via the propositional operators, whereas the semantics describes how one determines whether these expressions are true or false.

::: definition
Let $P$ be some non-empty set of **propositional symbols**.
The set $L$ of propositional **sentences** or **formulae** contains all of the following, and only those:


- $p$ for every $p \in P$
- $(\neg \phi)$ if $\phi \in L$
- $(\phi \wedge \psi)$ if $\phi, \psi \in L$
- $(\phi \vee \psi)$ if $\phi, \psi \in L$
- $(\phi \rightarrow \psi)$ if $\phi, \psi \in L$
- $(\phi \leftrightarrow \psi)$ if $\phi, \psi \in L$


Given an **assignment function** $g: P \rightarrow \setof{0,1}$, the truth value of a propositional formula with respect to $g$ is computed as follows:


- $g(\neg p) = 1 - g(p)$
- $g(\phi \wedge \psi) = \min(g(\phi), g(\psi))$
- $g(\phi \vee \psi) = \max(g(\phi), g(\psi))$
- $g(\phi \rightarrow \psi) = \max(g(\neg \phi) g(\psi))$
- $g(\phi \leftrightarrow \psi) = \min(g(\phi), g(\psi))$

:::

::: exercise
For each one of the following, say whether it is a valid propositional formula according to the definition above.
If so, compute its truth value in a step-by-step fashion, assuming $g(p) = 1$ and $g(q) = 0$.


- $(p \wedge q)$
- $((p \wedge q) \vee (\neg p))$
- $p$
- $(p \neg \rightarrow q)$
- $(\neg ((\neg p) \rightarrow (\neg (\neg q))))$

:::

::: exercise
The definition above defines formulas in terms of strings.
However, sometimes it is more insightful to define them as trees.
The formula $(p \wedge (\neg q))$ corresponds to the tree below.

~~~ {.include-tikz size=mid}
formula1.forest
~~~

A longer formula such as
$(\neg (\neg (\neg ((p \rightarrow q) \rightarrow (\neg ( (\neg p) \vee (\neg q)))))))$
yields a correspondingly larger tree.

~~~ {.include-tikz size=mid}
formula2.forest
~~~

Draw the corresponding tree for each one of the formulas below:


- $(\neg p)$
- $(p \rightarrow ((q \rightarrow r) \wedge (\neg r)))$
- p

:::

::: exercise
Define a context-free grammar that generates all trees of all well-formed propositional formulas, and only those.
You may assume that the set of propositional symbols is finite.
:::


## Bracketing conventions

The formal definition of propositional formulas rigorously places brackets to avoid any potential ambiguities.

::: example
The formula $p \wedge q \vee r$ is ambiguous.
It could either mean $((p \wedge q) \vee r)$, or $p \wedge (q \vee r)$.
:::

::: exercise
Give an assignment of truth values to $p$, $q$, and $r$ such that $((p \wedge q) \vee r)$ and $p \wedge (q \vee r)$ receive different truth values.
:::

But excessive bracketing is very inconvenient and hard to read.
The need for brackets can be reduced via an operator hierarchy:

1. $\neg$
1. $\wedge$ and $\vee$
1. $\rightarrow$
1. $\leftrightarrow$

Operators that are higher in this hierarchy are stronger binders than operators in lower levels.

::: example
Consider the formula $\neg p \rightarrow q \wedge \neg v$, where many brackets have been omitted.
According to the operator hierarchy above, this is equivalent to $((\neg p) \rightarrow (q \wedge (\neg v)))$.
The negation operator is highest in the hierarchy, so it gets to combine first.
This yields $(\neg p) \rightarrow q \wedge (\neg v)$.
Next we bracket all instances of $\wedge$ and $\vee$, resulting in $(\neg p) \rightarrow (q \wedge (\neg v))$.
Finally, we bracket $\rightarrow$ to arrive at the final $((\neg p) \rightarrow (q \wedge (\neg v)))$.
:::

::: exercise
For each one of the following formulas, remove all brackets that are redundant given the operator hierarchy above.


- $((\neg p) \rightarrow (\neg q))$
- $((p \wedge q) \leftrightarrow (\neg (q \vee r)))$
- $((\neg p) \rightarrow ((q \wedge r) \rightarrow s))$
- $(p \wedge (q \wedge r))$
- $(\neg (p \leftrightarrow (p \wedge q)))$

:::

## Truth tables

The semantic definition in terms of arithmetic over $0$ and $1$ is succinct, but not particularly intuitive.
A much more user-friendly format is provided by truth tables.
Each operator corresponds to a specific truth table, and each row in the truth table shows the value returned by the operator depending on the truth values of its arguments.

| $p$ | $\neg p$ |
| :-: | :-:      |
| 0   | 1        |
| 1   | 0        |


| $p$ | $q$ | $p \wedge q$ |
| :-: | :-: | :-:          |
| 0   | 0   | 0            |
| 0   | 1   | 0            |
| 1   | 0   | 0            |
| 1   | 1   | 1            |


| $p$ | $q$ | $p \vee q$   |
| :-: | :-: | :-:          |
| 0   | 0   | 0            |
| 0   | 1   | 1            |
| 1   | 0   | 1            |
| 1   | 1   | 1            |


| $p$ | $q$ | $p \rightarrow q$ |
| :-: | :-: | :-:               |
| 0   | 0   | 1                 |
| 0   | 1   | 1                 |
| 1   | 0   | 0                 |
| 1   | 1   | 1                 |


| $p$ | $q$ | $p \leftrightarrow q$ |
| :-: | :-: | :-:                   |
| 0   | 0   | 1                     |
| 0   | 1   | 0                     |
| 1   | 0   | 0                     |
| 1   | 1   | 1                     |

Truth tables not only provide an easier format for mastering the propositional operators, they also act as a simple way for calculating the truth value of a formula.
The table contains one row for every possible assignment of truth values to propositional symbols.
Then one proceeds row by row, adding in the values of the operators based on what other values have already been filled in.

::: example
Consider the fairly complex formula $p \rightarrow (q \wedge r \rightarrow (\neg q \rightarrow p \wedge \neg q))$.
Is is true or false?
It certainly is hard to tell at first glance, and translating to English doesn't help much (in fact, it makes things worse):
*If $p$ then it also holds that if both $q$ and $r$ then if not $q$ then $p$ and not $q$*.
Um, come again?

To quickly get the answer, we construct a truth table. 
We start out by instantiating all possible combinations of truth tables for the propositional symbols.
We also split the formula over multiple columns, one for each propositional symbol or logical operator.

| $p$ | $q$ | $r$ | $p$ | $\rightarrow$ | $(q$ | $\wedge$ | $r$ | $\rightarrow$ | $(\neg$ | $q$ | $\rightarrow$ | $p$ | $\wedge$ | $\neg$ | $q))$ |
| :-: | :-: | :-: | :-: | :-:           | :-:  | :-:      | :-: | :-:           | :-:     | :-: | :-:           | :-: | :-:      | :-:    | :-:   |
|  0  |  0  |  0  |     |               |      |          |     |               |         |     |               |     |          |        |       |
|  0  |  0  |  1  |     |               |      |          |     |               |         |     |               |     |          |        |       |
|  0  |  1  |  0  |     |               |      |          |     |               |         |     |               |     |          |        |       |
|  0  |  1  |  1  |     |               |      |          |     |               |         |     |               |     |          |        |       |
|  1  |  0  |  0  |     |               |      |          |     |               |         |     |               |     |          |        |       |
|  1  |  0  |  1  |     |               |      |          |     |               |         |     |               |     |          |        |       |
|  1  |  1  |  0  |     |               |      |          |     |               |         |     |               |     |          |        |       |
|  1  |  1  |  1  |     |               |      |          |     |               |         |     |               |     |          |        |       |

Next we fill in the columns of the formula whose truth value depends only on the propositional symbols.
That's the propositional symbols themselves, and a any operators that only depend on those propositional symbols

| $p$ | $q$ | $r$ | $p$ | $\rightarrow$ | $(q$ | $\wedge$ | $r$ | $\rightarrow$ | $(\neg$ | $q$ | $\rightarrow$ | $p$ | $\wedge$ | $\neg$ | $q))$ |
| :-: | :-: | :-: | :-: | :-:           | :-:  | :-:      | :-: | :-:           | :-:     | :-: | :-:           | :-: | :-:      | :-:    | :-:   |
|  0  |  0  |  0  |  0  |               |  0   |    0     |  0  |               |     1   |  0  |               |  0  |          |   1    |  0    |
|  0  |  0  |  1  |  0  |               |  0   |    0     |  1  |               |     1   |  0  |               |  0  |          |   1    |  0    |
|  0  |  1  |  0  |  0  |               |  1   |    0     |  0  |               |     0   |  1  |               |  0  |          |   0    |  1    |
|  0  |  1  |  1  |  0  |               |  1   |    1     |  1  |               |     0   |  1  |               |  0  |          |   0    |  1    |
|  1  |  0  |  0  |  1  |               |  0   |    0     |  0  |               |     1   |  0  |               |  1  |          |   1    |  0    |
|  1  |  0  |  1  |  1  |               |  0   |    0     |  1  |               |     1   |  0  |               |  1  |          |   1    |  0    |
|  1  |  1  |  0  |  1  |               |  1   |    0     |  0  |               |     0   |  1  |               |  1  |          |   0    |  1    |
|  1  |  1  |  1  |  1  |               |  1   |    1     |  1  |               |     0   |  1  |               |  1  |          |   0    |  1    |

Next we fill in the columns for operators whose arguments have had their columns filled in during the previous step.
The only option is the rightmost $\wedge$, everything else still is waiting for at least one column to be filled in.

| $p$ | $q$ | $r$ | $p$ | $\rightarrow$ | $(q$ | $\wedge$ | $r$ | $\rightarrow$ | $(\neg$ | $q$ | $\rightarrow$ | $p$ | $\wedge$ | $\neg$ | $q))$ |
| :-: | :-: | :-: | :-: | :-:           | :-:  | :-:      | :-: | :-:           | :-:     | :-: | :-:           | :-: | :-:      | :-:    | :-:   |
|  0  |  0  |  0  |  0  |               |  0   |    0     |  0  |               |     1   |  0  |               |  0  |     0    |   1    |  0    |
|  0  |  0  |  1  |  0  |               |  0   |    0     |  1  |               |     1   |  0  |               |  0  |     0    |   1    |  0    |
|  0  |  1  |  0  |  0  |               |  1   |    0     |  0  |               |     0   |  1  |               |  0  |     0    |   0    |  1    |
|  0  |  1  |  1  |  0  |               |  1   |    1     |  1  |               |     0   |  1  |               |  0  |     0    |   0    |  1    |
|  1  |  0  |  0  |  1  |               |  0   |    0     |  0  |               |     1   |  0  |               |  1  |     1    |   1    |  0    |
|  1  |  0  |  1  |  1  |               |  0   |    0     |  1  |               |     1   |  0  |               |  1  |     1    |   1    |  0    |
|  1  |  1  |  0  |  1  |               |  1   |    0     |  0  |               |     0   |  1  |               |  1  |     0    |   0    |  1    |
|  1  |  1  |  1  |  1  |               |  1   |    1     |  1  |               |     0   |  1  |               |  1  |     0    |   0    |  1    |

We then continue like this in a step-wise fashion, paying close attention to each operator's scope in order to determine which column should be filled in next.

| $p$ | $q$ | $r$ | $p$ | $\rightarrow$ | $(q$ | $\wedge$ | $r$ | $\rightarrow$ | $(\neg$ | $q$ | $\rightarrow$ | $p$ | $\wedge$ | $\neg$ | $q))$ |
| :-: | :-: | :-: | :-: | :-:           | :-:  | :-:      | :-: | :-:           | :-:     | :-: | :-:           | :-: | :-:      | :-:    | :-:   |
|  0  |  0  |  0  |  0  |               |  0   |    0     |  0  |               |     1   |  0  |     0         |  0  |     0    |   1    |  0    |
|  0  |  0  |  1  |  0  |               |  0   |    0     |  1  |               |     1   |  0  |     0         |  0  |     0    |   1    |  0    |
|  0  |  1  |  0  |  0  |               |  1   |    0     |  0  |               |     0   |  1  |     1         |  0  |     0    |   0    |  1    |
|  0  |  1  |  1  |  0  |               |  1   |    1     |  1  |               |     0   |  1  |     1         |  0  |     0    |   0    |  1    |
|  1  |  0  |  0  |  1  |               |  0   |    0     |  0  |               |     1   |  0  |     1         |  1  |     1    |   1    |  0    |
|  1  |  0  |  1  |  1  |               |  0   |    0     |  1  |               |     1   |  0  |     1         |  1  |     1    |   1    |  0    |
|  1  |  1  |  0  |  1  |               |  1   |    0     |  0  |               |     0   |  1  |     1         |  1  |     0    |   0    |  1    |
|  1  |  1  |  1  |  1  |               |  1   |    1     |  1  |               |     0   |  1  |     1         |  1  |     0    |   0    |  1    |

| $p$ | $q$ | $r$ | $p$ | $\rightarrow$ | $(q$ | $\wedge$ | $r$ | $\rightarrow$ | $(\neg$ | $q$ | $\rightarrow$ | $p$ | $\wedge$ | $\neg$ | $q))$ |
| :-: | :-: | :-: | :-: | :-:           | :-:  | :-:      | :-: | :-:           | :-:     | :-: | :-:           | :-: | :-:      | :-:    | :-:   |
|  0  |  0  |  0  |  0  |               |  0   |    0     |  0  |      1        |     1   |  0  |     0         |  0  |     0    |   1    |  0    |
|  0  |  0  |  1  |  0  |               |  0   |    0     |  1  |      1        |     1   |  0  |     0         |  0  |     0    |   1    |  0    |
|  0  |  1  |  0  |  0  |               |  1   |    0     |  0  |      1        |     0   |  1  |     1         |  0  |     0    |   0    |  1    |
|  0  |  1  |  1  |  0  |               |  1   |    1     |  1  |      0        |     0   |  1  |     1         |  0  |     0    |   0    |  1    |
|  1  |  0  |  0  |  1  |               |  0   |    0     |  0  |      1        |     1   |  0  |     1         |  1  |     1    |   1    |  0    |
|  1  |  0  |  1  |  1  |               |  0   |    0     |  1  |      1        |     1   |  0  |     1         |  1  |     1    |   1    |  0    |
|  1  |  1  |  0  |  1  |               |  1   |    0     |  0  |      1        |     0   |  1  |     1         |  1  |     0    |   0    |  1    |
|  1  |  1  |  1  |  1  |               |  1   |    1     |  1  |      1        |     0   |  1  |     1         |  1  |     0    |   0    |  1    |

| $p$ | $q$ | $r$ | $p$ | $\rightarrow$ | $(q$ | $\wedge$ | $r$ | $\rightarrow$ | $(\neg$ | $q$ | $\rightarrow$ | $p$ | $\wedge$ | $\neg$ | $q))$ |
| :-: | :-: | :-: | :-: | :-:           | :-:  | :-:      | :-: | :-:           | :-:     | :-: | :-:           | :-: | :-:      | :-:    | :-:   |
|  0  |  0  |  0  |  0  |      1        |  0   |    0     |  0  |      1        |     1   |  0  |     0         |  0  |     0    |   1    |  0    |
|  0  |  0  |  1  |  0  |      1        |  0   |    0     |  1  |      1        |     1   |  0  |     0         |  0  |     0    |   1    |  0    |
|  0  |  1  |  0  |  0  |      1        |  1   |    0     |  0  |      1        |     0   |  1  |     1         |  0  |     0    |   0    |  1    |
|  0  |  1  |  1  |  0  |      1        |  1   |    1     |  1  |      0        |     0   |  1  |     1         |  0  |     0    |   0    |  1    |
|  1  |  0  |  0  |  1  |      1        |  0   |    0     |  0  |      1        |     1   |  0  |     1         |  1  |     1    |   1    |  0    |
|  1  |  0  |  1  |  1  |      1        |  0   |    0     |  1  |      1        |     1   |  0  |     1         |  1  |     1    |   1    |  0    |
|  1  |  1  |  0  |  1  |      1        |  1   |    0     |  0  |      1        |     0   |  1  |     1         |  1  |     0    |   0    |  1    |
|  1  |  1  |  1  |  1  |      1        |  1   |    1     |  1  |      1        |     0   |  1  |     1         |  1  |     0    |   0    |  1    |

The last column to be filled in shows the truth value for the whole formula.
As you can see, this formula is always true, irrespective of the specific assignment. 
Such a formula is called a **tautology**.
:::

::: exercise
The **Quine dagger** has the following truth table.

| $p$ | $q$ | $p \downarrow   q$   |
| :-: | :-: | :-:                  |
| 0   | 0   | 1                    |
| 0   | 1   | 0                    |
| 1   | 0   | 0                    |
| 1   | 1   | 0                    |

How could you express $p \downarrow q$ with the standard operators?
Can you think of an English construction that corresponds to the Quine dagger?
:::

::: exercise
A set of operators is **(functionally) complete** iff $\neg$, $\wedge$, $\vee$, $\rightarrow$, and $\leftrightarrow$ can all be described in terms of the set's operators.
Show that $\setof{\neg, \wedge}$ is functionally complete in this sense by defining $\vee$, $\rightarrow$, and $\leftrightarrow$ in terms of $\neg$ and $\wedge$.
:::


## Two unintuitive aspects of $\vee$ and $\rightarrow$

For the most part, the propositional operators are very similar to their natural language counterparts.
There are two common stumble blocks, though, which pertain to the logical *or*-operator $\vee$ and the implication operator $\rightarrow$.
Logical or corresponds to what is called **inclusive or** in linguistics, in contrast to **exclusive or**.
Inclusive or is true whenever at least one of the arguments is true, whereas exclusive or holds only if exactly one of the arguments is true.

::: exercise
Exclusive or is known as XOR in computer science, and often occurs together with NAND, which is a negated $\wedge$ (the NAND operator is also known as the **Sheffer stroke** $\downarrow$).

| $p$ | $q$ | $p \mathrm{XOR} q$   |
| :-: | :-: | :-:                  |
| 0   | 0   | 0                    |
| 0   | 1   | 1                    |
| 1   | 0   | 1                    |
| 1   | 1   | 0                    |

| $p$ | $q$ | $p \mathrm{NAND} q$  |
| :-: | :-: | :-:                  |
| 0   | 0   | 1                    |
| 0   | 1   | 1                    |
| 1   | 0   | 1                    |
| 1   | 1   | 0                    |


The two are very important for transistor design, because $\neg$, $\wedge$, $\vee$, $\rightarrow$, and $\leftrightarrow$ can all be expressed in terms of these two operators.
So logical circuitry can be built entirely with XOR and NAND circuits, which keeps production costs low.


Express each one of the standard five operators as a combination of XOR and NAND (you may use each one multiple times, if necessary).
:::

With implication, the unintuitive part is that $p \rightarrow q$ is true whenever $p$ is false.
This is known as **ex falso quodlibet** --- from a falsehood we may infer whatever we want.
Natural language implication does not work like this.
Suppose a roober says *If you don't give me your money I'll shoot you*.
If the roober is a logician, he might take your money and shoot you, pointing out that he didn't say anything about what happens when you do give him your money.
That's how logical implication works, but it's not how if-then works in natural languages.
So always keep in mind:

- $\vee$ is inclusive, not exclusive
- $p \rightarrow q$ cannot be false if $p$ is false

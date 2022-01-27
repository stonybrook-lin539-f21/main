# Explaining a syntactic universal: the Adjunct Island Constraint

::: exercise
Neither $\leq_l$ nor $\leq_s$ are weak partial orders.
Remember that a relation is a weak partial order iff it is transitive, antisymmetric, and reflexive.
Which of these properties do not hold of $\leq_l$ or $\leq_s$?
Justify your answer.
:::

::: solution
Both $\leq_l$ and $\leq_s$ are transitive and reflexive (which makes them preorders):

- Transitivity of $\leq_l$: If the length of $s$ does not exceed the length of $t$, and the length of $t$ does not exceed the length of $u$, then the length of $s$ does not exceed the length of $u$.
- Reflexivity of $\leq_l$: The length of $s$ does not exceed the length of $s$.
- Transitivity of $\leq_s$: If the slur count of $s$ does not exceed the slur count of $t$, and the slur count of $t$ does not exceed the slur count of $u$, then the slur count of $s$ does not exceed the slur count of $u$.
- Reflexivity of $\leq_l$: The slur count of $s$ does not exceed the slur count of $s$.

But neither $\leq_l$ nor $\leq_s$ is antisymmetric.

- Lack of antisymmetry for $\leq_l$: If $s$ and $t$ are distinct strings of the same length, then we have $s \leq_l t$ and $t \leq_l s$ even though $s \neq t$.
- Lack of antisymmetry for $\leq_s$: If $s$ and $t$ contain the same number of slurs, then we have $s \leq_s t$ and $t \leq_s s$ even though $s \neq t$.

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

::: solution

- John slept $\leq_A$ John definitely slept yesterday
- The old man snored $\geq_A$ The man snored
- John likes Mary \_ Mary really likes John
- John ate pasta $\leq_A$ John ate pasta ($\geq_A$ would also work)
- John ate pasta \_ John ate (*pasta* is not an adjunct)

:::

::: exercise
Show that $\leq_A$ is a weak partial order.
That is to say, it is a binary relation that is transitive, antisymmetric, and reflexive.
:::

::: solution
- **Transitivity**:
  If $x \leq_A y$ and $y \leq_A z$, then $y$ can be obtained from $x$ by adding adjuncts $a_1, \ldots, a_m$ ($m \geq 0$), and $z$ can be obtained from $y$ by adding adjuncts $b_1, \ldots, b_n$ ($n \geq 0$).
  Hence $z$ can be obtained by adding adjuncts $a_1, \ldots, a_m, b_1, \ldots, b_n$, and thus $x \leq_A z$.

- **Reflexivity**:
  Every $x$ can be obtained from itself by adding 0 adjuncts, hence $x \leq_A x$ for all $x$.

- **Antisymmetry**:
  Suppose $x \leq_A y$ and $y \leq_A x$.
  If $y$ is obtained from $x$ by adding at least 1 adjunct, then it is impossible to obtain $x$ from $y$ without deleting this adjunct.
  But then $y \leq_A x$ does not hold.
  Hence the only case where $x \leq_A y$ and $y \leq_A x$ can both be true is if one can be obtained from the other by adding 0 adjuncts.
  But that is possible only if $x = y$.
:::

::: exercise
Suppose that $s$ is *The old men quickly manned the boat*.
Write down five members of $A_L(s)$.
:::

::: solution
We need to list 5 adjunct extensions of *The old man quickly manned the boat*.
Note that every sentence is an adjunct extension of itself.

1. The old man quickly manned the boat.
1. The very old man quickly manned the boat.
1. The old man very quickly manned the boat.
1. The old man quickly manned the old boat.
1. The very old man very quickly manned the very old boat.
:::

::: exercise
Continuing the previous exercise, draw the corresponding figure for your fragment of $A_L(s)$.
:::

::: solution
fixme: typeset this
:::

::: exercise
Suppose we take the set of natural numbers and order it by $\leq$ in the usual way, yielding a single line of numbers.
Is this a meet semilattice?
Justify your answer.
:::

::: solution
Yes, the line of natural numbers is a meet semilattice.
Intuitively, the meet of two natural numbers is the one that's further left on the number line.

Mathematically, we have to show two properties:

1. For any two natural numbers $x$ and $y$, there is a non-empty set of lower bounds.
   This holds.
   Suppose we want all the lower bounds of $x$ and $y$, and that $x \leq y$.
   Then the set of lower bounds contains all $z$ such that $z \leq x$.
   At the very least, this set contains $x$ itself and thus cannot be empty.
1. We also need to show that for any two natural numbers $x$ and $y$, its set of lower bounds contains a unique greatest lower bound.
   But if $x \leq y$, the greatest element among their lower bounds is $x$ itself.
:::

::: exercise
If we take optionality in this sense as an intrinsic property of adjuncts, then we can use the structure of $L$ under $\leq_A$ to infer the well-formedness of one string from another.
In particular, the following two laws follow from optionality:

1. If $s$ is well-formed, then so is every string that $s$ is an adjunct extension of.
1. If $s$ is ill-formed, then so is every adjunct extension of $s$.

In other words, well-formedness travels downward in each meet semilattice $A_L(s)$, and ill-formedness travels upward.

Explain why these entailments follow from the optionality of adjuncts.
:::

::: solution
Suppose that $t$ is a well-formed sentence containing 0 or more adjuncts.
Since each adjunct is optional, it can be removed without rendering the string ill-formed.
By removing adjuncts, we can obtain any sentence $s$ such that $s \leq_A t$.
Hence the well-formedness of $t$ implies the well-formedness of every such $s$.

In the other direction, suppose that $t$ is ill-formed.
Then every $u$ such that $t \leq_A u$ must also be ill-formed.
Assume towards a contradiction that $u$ is actually well-formed.
As we just saw, if $u$ is well-formed then so is every $s$ that $u$ is an adjunct extension of, including $t$.
But this contradicts our initial assumption that $t$ is ill-formed, so $u$ cannot be ill-formed after all.
Hence it is necessarily the case that whenever $t \leq_A u$ and $t$ is ill-formed, $u$ is ill-formed too.
:::

::: exercise
Explain why a monotonically increasing function from $L$ to $\mathbf{2}$ with $F \leq_2 T$ must be monotonically decreasing if we do exactly one of the following:

- switch the order to $T \leq_2 F$,
- switch the order $\leq_A$ in $L$.

:::

::: solution
If $f$ is a monotonically increasing from $L$ to $\mathbf{2}$, then $x \leq_A y$ implies $f(x) \leq_2 f(y)$.
If we switch the order of $\leq_A$, then we have $y \leq_A x$ where we previously had $x \leq_A y$. 
Hence $f$ now is such that $y \leq_A y$ implies $f(x) \leq_2 f(y)$, making $f$ monotonically decreasing.

Similarly, if we flip the order of $\leq_2$ instead, then $f(x) \leq_2 f(y)$ becomes $f(x) \geq_2 f(y)$ for all $x$ and $y$.
Then $f$ is such that $x \leq_A y$ implies $f(x) \geq_2 f(y)$, which once again makes $f$ a monotonically decreasing function.
:::

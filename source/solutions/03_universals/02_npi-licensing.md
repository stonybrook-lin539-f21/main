# NPIs and monotonicity

::: exercise
Consider the sentence *every student slept*.
Does it allow for similar inferences via entailment?
:::

::: solution
Yes. If *every student slept*, then both of the following are true:

1. Every male student slept.
1. Every sophomore slept.
:::

::: example
Let $A$ be the set of all students.
The sentence *No student slept* asserts for each student $s \in A$ that $s$ did not sleep.
Suppose this is true.
Then *No X slept* is necessarily true if X denotes some set $B \subseteq A$ because we already know for each $s \in B$ that $s$ did not sleep.
Since there is no subset of $A$ for which this entailment fails, *no* is indeed downward entailing.
:::

::: exercise
Construct a similar argument to show that *every* is downward entailing.
:::

::: solution
We can do this by substituting just a few terms in the example:

Let $A$ be the set of all students.
The sentence *Every student slept* asserts for each student $s \in A$ that $s$ did in fact sleep.
Suppose this is true.
Then *Every X slept* is necessarily true if X denotes some set $B \subseteq A$ because we already know for each $s \in B$ that $s$ did sleep.
Since there is no subset of $A$ for which this entailment fails, *no* is indeed downward entailing.
:::

::: exercise
Represent the following sentences in terms of this functional notation:

- No professor writes good lecture notes.
- Every professor could earn more in industry.
- This professor, no student likes.

:::

::: solution
The central thing to keep in mind is that the arguments are determined by meaning, not the linear order in the string.
The first argument is what we are quantifying over, the second one what is being done.

- No(professor, writes good lecture notes)
- Every(professor, could earn more in industry)
- No(student, likes this professor)

:::

One thing the functional notation makes very clear is that a sentence like *no student slept* consists of two distinct parts that contribute to the meaning.
The first one, represented by X, is the set of things or objects that *no* picks from.
The second one, represented by Y, states what each one of them does.
Our previous examples of entailment only looked at X.
We made inferences from *no students* to *no sophomores* and *no male student*.
But what happens if we instead look at Y?

The answer is "not much" if we look at *no*.
But things get more interesting with *every*, so let us look at that one first.
Consider a sentence like *every student ran*, and contrast it against *every student ran a 5k*.
Is there an entailment here, and if so, in what direction?
Every person who runs a 5k is a person who runs, but the opposite is not true because somebody who runs, say, 1 mile is still a person who runs, but they're not a person who runs a 5k.
So the set of 5k-runners is necessarily a subset of all runners, but the set of runners is not guaranteed to be a subset of the set of 5k-runners (although this can happen if literally every runner is running a 5k).
It is also clear that if every student ran a 5k, then every student ran, whereas the opposite does not hold. 
So all of a sudden the direction of inference is the other way round --- if the sentence is true for Y, then it is true for every **superset** of Y.
This shows that even though *every* was downward entailing with respect to X, it is **upward entailing** with respect to Y.

::: exercise
Show that *no* is downward entailing with respect to Y.
:::

::: solution
Consider a concrete example first.
Suppose *No student runs* is true.
Then *No student runs a 5k* is also true.
The set of individuals that run a 5k is a subset of the individuals that run, so we made an inference from a set $S$ to a subset of $S$, which means that we have downward entailment.

More generally, if $\mathrm{No}(X,Y)$ is true, then there is no individual $i \in X$ such that $i$ belongs to the set of individuals that do $Y$.
But then $i$ cannot belong to any subset of $Y$, either, giving us downward entailment with respect to $Y$.
:::

::: example
Consider the sentences
*Every student ran a 5k*
and
*Every student ran*.
Clearly if the former is true, the latter must be too.
We also know already that the set of students that ran a 5k (call it $5k$) is a subset of the students that ran (call it $R$).
So we have $5k \subseteq R$.

Now suppose that $\text{\emph{every student}}(5k) = 1$.
Then $\text{\emph{every student}}(R) \geq 1$ because $R \supseteq 5k$ and the function is monotonically increasing.
So the fact that the sentence is true for $5k$ entails that it is true for every superset of $5k$.
This is exactly what it means to be upward entailing.
:::

::: exercise
Construct an example for downward entailment similar to the one above for upward entailment.
:::

::: solution
Again this only requires swapping out a few words:

Consider the sentences
*No student ran a 5k*
and
*No student ran*.
Clearly if the latter is true, the former must be too.
We also know already that the set of students that ran a 5k (call it $5k$) is a subset of the students that ran (call it $R$).
So we have $5k \subseteq R$.

Now suppose that $\text{\emph{no student}}(R) = 1$.
Then $\text{\emph{every student}}(5k) \geq 1$ because $5k \subseteq R$ and the function is monotonically decreasing.
So the fact that the sentence is true for $R$ entails that it is true for every subset of $R$.
This is exactly what it means to be downward entailing.
:::

::: exercise
Alternatively, we may view downward entailment as a monotonically increasing function if sets are ordered by the superset relation instead of subset.
Explain why!
:::

::: solution
By ordering sets by the superset relation instead of the subset relation, we flip their order: if $X < Y$ (i.e. $X \subseteq Y$), we now have $Y < X$ (i.e. $Y \supseteq X$).
Downward entailment means that if a statement is true with respect to $Y$, then it is true with respect to every $X$ that $Y$ is a superset of.
But in our new ordering, that's every $X$ such that $Y < X$.
Hence downward entailment can be rephrased as follows: if $f(Y) = 1$, then $f(X) \geq 1$ for every $X > Y$.
And that is an instance of being monotonically increasing.
:::

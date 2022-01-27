# (Semi)Lattices

Posets are already a special kind of structure.
Among all the possible ways of defining a relation over a set, only those yield a poset where the relation is a partial order.
But some posets are even more special because they furnish particular upper or lower bounds for the elements of the poset.
These posets are called **semilattices** and **lattices**.


## Greatest lower bounds and least upper bounds

The previous unit was only concerned with identifying lower bounds and upper bounds, but not all lower bounds and upper bounds are the same.
Some are "closer" to the elements whose bounds we want to compute.
This gives us the notion of **greatest lower bound** and **least upper bound**.

::: example
We return once more to the poset of subsets of $\setof{1,2,3}$ ordered by the subset relation $\subseteq$.
We have already seen that the upper bounds of $\setof{1}$ are $\setof{1}$, $\setof{1,2}$, $\setof{1,3}$, and $\setof{1,2,3}$.
And the lower bounds of $\setof{1}$ are the empty set and $\setof{1}$ itself.

~~~ {.include-tikz size=mid}
lattice_123_bounds1.tikz
~~~

Among those lower bounds, the greatest lower bound is $\setof{1}$ because it is closest to $\setof{1}$.
And the least upper bound is also $\setof{1}$.
:::

::: example
We also know already that given the poset above,
$\mathrm{ub}(\setof{\setof{2}, \setof{3}, \setof{2,3}}) = \setof{\setof{2,3}, \setof{1,2,3}}$ and 
$\mathrm{lb}(\setof{\setof{2}, \setof{3}, \setof{2,3}}) = \setof{\emptyset}$.

~~~ {.include-tikz size=mid}
lattice_123_bounds2-3-23.tikz
~~~

In this case, the least upper bound is $\setof{2,3}$ because $\setof{2,3}$ is less than $\setof{1,2,3}$ (we have $\setof{2,3} \subseteq \setof{1,2,3}$).
The greatest lower bound is $\emptyset$ because there was only one lower bound to begin with.
:::

Looking at those examples, you might have already noticed a peculiar connection.
The greatest lower bounds of some subset $S$ are exactly the upper bounds of the lower bounds of $S$.
And the least upper bounds of $S$ are exactly the lower bounds of the upper bounds of $S$.

::: definition
Given a poset $\tuple{S, \leq}$ and some arbitrary subset $T \subseteq S$, we call $\mathrm{lub}(T) \is \mathrm{lb}(\mathrm{ub}(T))$ the set of **least upper bounds** of $T$.
An element of $\mathrm{lub}(T)$ is also called a **lub** or a **supremum** or a **join**.
Similarly, $\mathrm{glb}(T) \is \mathrm{ub}(\mathrm{lb}(T))$ is the set of **greatest lower bounds** of $T$.
An element of $\mathrm{glb}(T)$ is also called a **glb** or an **infimum** or a **meet**.
:::

::: example
Let us return to the first example, where we saw that the set of upper bounds of $\setof{1}$ is $\setof{ \setof{1}, \setof{1,2}, \setof{1,3}, \setof{1,2,3} }$ while the least upper bound of $\setof{1}$ is $\setof{1}$ itself.
Following our definition, we compute the lub as 
$$\mathrm{lub}(\setof{\setof{1}}) = \mathrm{lb}(\mathrm{ub}(\setof{\setof{1}})) = \mathrm{lb}(\setof{ \setof{1}, \setof{1,2}, \setof{1,3}, \setof{1,2,3} }) = \setof{\setof{1}}.$$
This tells us that $\setof{1}$ is the only lub of $\setof{1}$, as expected.
:::

::: exercise
Given the same poset as in the previous examples, compute all of the following:


- $\mathrm{lub}(\setof{\setof{1,2}, \setof{2,3}})$
- $\mathrm{glb}(\setof{\setof{1,2}, \setof{2,3}})$
- $\mathrm{lub}(\setof{\emptyset})$
- $\mathrm{glb}(\setof{\emptyset, \setof{1,2,3}})$
- $\mathrm{glb}(\setof{\setof{1}, \setof{2,3}, \setof{1,2,3}})$
- $\mathrm{lub}(\setof{\setof{1}, \setof{2}, \setof{3}})$

:::


## Uniqueness of lubs and glbs

In the examples so far, there has always been a unique lub and a unique glb.
But this isn't always the case with posets.

::: example
We have already seen in the previous units that some posets many not have any lower bounds or upper bounds for at least some subsets of the carrier.

~~~ {.include-tikz size=mid}
poset_nobounds.tikz
~~~

If there's no lower bounds or upper bounds, then there can't be any greatest lower bounds or least upper bounds either.
:::

::: example
With the poset below, $\mathrm{ub}(S)$ and $\mathrm{lb}(S)$ are non-empty for any non-empty subset $S$ of the carrier.
That is to say, any collection of one or more elements has at least one upper bound and at least one lower bound.

~~~ {.include-tikz size=mid}
poset_nouniquemeet.tikz
~~~

However, $\mathrm{lub}(\setof{c,d})$ is actually empty.
To see this, we first compute $\mathrm{ub}(\setof{c,d}) = \setof{a,b,e}$.
We next calcuate $\mathrm{lb}(\setof{a,b,e})$, which is the empty set because there is no $x$ in $\setof{a,b,e}$ such that $x \leq y$ for all $y \in \setof{a,b,e}$.
Putting these two results together, we get $\mathrm{lub}(\setof{c,d}) = \emptyset$.
:::

The reasoning in the example above can be used to prove a powerful result: lubs and glbs are unique.

::: proposition
Let $T$ be a subset of the carrier of some poset $\tuple{S, \leq}$.
If $\mathrm{lub}(T) \neq \emptyset$, then it contains exactly one element.
If $\mathrm{glb}(T) \neq \emptyset$, then it contains exactly one element.
:::

::: exercise
Try to explain to yourself why this result holds.

*Hint*: Suppose towards a contradiction that $\mathrm{lub}(T)$ does contain at least two distinct elements $x$ and $y$.
How would $x$ and $y$ have to be ordered by $\leq$?
Is this possible in a poset?
:::

Since lubs and glbs are unique, it is often convenient to assume that the functions $\mathrm{lub}$ and $\mathrm{glb}$ return this unique element rather than a set containing the element.
Quite generally, we can reduce the use of sets in the notation by quite a bit.
It is often convenient to write $x \vee y$ as a shorthand for $\mathrm{lub}(\setof{x,y})$, and $x \wedge y$ as a shorthand for $\mathrm{glb}(x, y)$.
If you didn't like notation like $\mathrm{glb}(\setof{ \setof{1}, \setof{2} })$, you can now rejoice because you have the more legible alternative $\setof{1} \wedge \setof{2}$.
The notation can be generalized such that $\mathrm{lub}(\setof{s_1, \ldots, s_n}) = s_1 \vee s_2 \vee \cdots \vee s_n$, and similarly for $\mathrm{glb}$ and $\wedge$.
The operations $\vee$ and $\wedge$ are referred to as **join** and **meet**.

::: exercise
Writing $\mathrm{glb}(\setof{s_1, \ldots, s_n})$ as $s_1 \wedge s_2 \wedge \cdots \wedge s_n$ is possible because $\wedge$ is an associative operation: $(x \wedge y) \wedge z = x \wedge (y \wedge z)$. 
Explain why $\wedge$ is associative.

*Hint*: You want to show that $\mathrm{glb}(\setof{ \mathrm{glb}(\setof{x, y}), z}) = \mathrm{glb}(\setof{x, \mathrm{glb}(\setof{y, z})})$ if one adopts the convention that the $\mathrm{glb}$ function returns a unique element rather than a set.
:::

::: example
A quick remark on terminology: beginners often confuse the symbols $\vee$ and $\wedge$.
There's multiple tricks that might help you remember which is which.

First, think of the poset of subsets of $\setof{1,2,3}$ we had in the first example of this unit.
In this lattice, intersecting two elements ($\cap$) is the same as taking their meet ($\wedge$), whereas taking their union ($\cup$) is the same as taking their join ($\vee$).
So the symbols for meet and join mirror those for intersection and union.

In addition, you can think of the meet operation as looking at all the lower bounds below and limiting them to just one at the very top, just like $\wedge$ is broad at the bottom and has only enough room for one thing at the top.
The join operation $\vee$ is the mirror image of that.
We look at the upper bounds above and limit it to just one thing at the very bottom.

Finally, the meet symbol $\wedge$ looks like one half of the letter *m* at the beginning of *meet*.
And $\vee$ is the final part of the final letter *n* of *join*.
This is perhaps the hokiest way of memorizing the symbols, but it's the one that worked best for me back in the days.
:::


## (Semi)Lattices

As we have seen, not every poset furnishes a join or a meet for every subset of the carrier.
The posets that do are particularly well-behaved and hence get special terms: **join semilattice** and **meet semilattice**.

::: definition
A poset $\tuple{S, \leq}$ is a **join semilattice** iff $x \vee y$ exists for all $x, y \in S$.
It is a **meet semilattice** iff $x \wedge y$ exists for all $x, y \in S$.
It is a **semilattice** iff is a join semilattice or a meet semilattice.
:::

::: exercise
For each one of the following depictions of a poset, say whether it is a join semilattice, a meet semilattice, both, or neither.

\begin{forest}
    [True [False]]
\end{forest}

\begin{forest}
    [A
        [D]
        [B
            [C]
        ]
    ]
\end{forest}

\begin{forest}
    [,phantom
        [A
            [D]
            [B
                [C]
            ]
        ]
        [E]
    ]
\end{forest}

\begin{forest}
    [Y
        [A
            [D]
            [B
                [C,name=c]
            ]
        ]
        [E,name=e]
    ]
    %
    \draw (e.south) to (c.north);
\end{forest}

\begin{forest}
    [Y
        [A
            [D,name=d]
            [B
                [C,name=c]
            ]
        ]
        [E,name=e]
    ]
    %
    \draw (e.south) to (c.north);
    \draw (d.south) to (c.north);
\end{forest}

\begin{forest}
    [,phantom
        [X,name=x]
        [Y
            [A,name=a
                [D,name=d]
                [B
                    [C,name=c]
                ]
            ]
            [E,name=e]
        ]
    ]
    %
    \draw (e.south) to (c.north);
    \draw (d.south) to (c.north);
    \draw (x.south) to (a.north);
\end{forest}

\begin{forest}
    [Z
        [X,name=x]
        [Y
            [A,name=a
                [D,name=d]
                [B
                    [C,name=c]
                ]
            ]
            [E,name=e]
        ]
    ]
    %
    \draw (e.south) to (c.north);
    \draw (d.south) to (c.north);
    \draw (x.south) to (a.north);
\end{forest}

\begin{forest}
    [Z
        [X,name=x]
        [Y
            [A,name=a
                [D,name=d]
                [B
                    [C,name=c]
                ]
            ]
            [E,name=e]
        ]
    ]
    %
    \draw (e.south) to (c.north);
    \draw (d.south) to (c.north);
    \draw (x.south) to (a.north);
    \draw (x.south) to (e.north);
\end{forest}

:::

In practice, the distinction between join and meet semilattices isn't all that relevant. 
You can convert between join semilattices and meet semilattices by reversing the order: $x \mathrel{R} y$ becomes $y \mathrel{R} x$.
In terms of drawings, that's the same as flipping the semilattice upside-down, or rotating it by 180 degrees.

::: example
Consider the poset whose carrier contains the sets $\setof{1}$, $\setof{2}$, and $\setof{1,2}$, ordered by the subset relation $\subseteq$.
This is a join semilattice. 
It is not a meet semilattice because $\setof{1}$ and $\setof{2}$ have no meet.
However, we can just replace $\subseteq$ with $\supseteq$.
Now the poset is no longer a join semilattice, but it is a meet semilattice.

~~~ {.include-tikz size=mid}
semilattice_switch.tikz
~~~
:::


Some posets are so well-behaved that they are both join semilattices and meet semilattices.
These posets are **lattices**.

::: definition
A poset is a **lattice** iff it is both a join semilattice and a meet semilattice.
:::


::: example
The poset of subsets of $\setof{1,2,3}$ ordered by the subset relation $\subseteq$ is a lattice.
That's because it is both a join semilattice and a meet semilattice.
We cannot really show this manually here, since we would have to check for any collection of elements that is has a unique join and a unique meet.
And with $8$ elements, there would be $2^8 = 256$ combinations, and for each one we would have to compute join and meet to ensure that it exists and is unique.

Rather than brute-forcing it like this, it is better to think about the nature of the poset.
First of all, we only need to show that there is a unique join and a unique meet for any two elements of the poset (because as pointed out above, join and meet are associative).
The ordering relation of the poset is subset, and the carrier includes all possible subsets of $\setof{1,2,3}$.
Given two sets $A$ and $B$, their least upper bound will be equivalent to $A \cup B$, and their greatest lower bound will be the same as $A \cap B$.
We know that $A \cap B$ and $A \cup B$ always exist, and we know that they cannot produce any sets that aren't subsets of $\setof{1,2,3}$.
This ensures that there is always a unique join and a unique meet.
:::

::: example
The poset $\tuple{\mathbb{N}, \leq}$ of natural numbers ordered by $\leq$ in the usual fashion is also a lattice.
In this case there would be infinitely many cases to check, so again we cannot brute-force this by looking at all possible cases.
And once again it is sufficient to consider the join and meet of two arbitrary elements.
Pick two such numbers $m$ and $n$.
Since $\leq$ is a total order, either $m \leq n$ or $n \leq m$ have to hold.
Assume the former.
Then $m \wedge n = m$ and $m \vee n = n$.
Once again we get a unique solution for join and meet that is guaranteed to exist no matter how $m$ and $n$ are chosen.
:::

::: example
The poset $\mathbf{2}$ of truth values is also a lattice.

~~~ {.include-tikz size=mid}
lattice_2.tikz
~~~

In this case, the lattice is small enough to verify by hand that meet and join exist in all relevant cases, which are $T \wedge T$, $T \wedge F$, and $F \wedge F$ (and similarly for $\vee$).
:::

::: exercise
Why don't we need to check $F \wedge T$ (or $F \vee T$)?
:::

::: exercise
Consider the poset depicted below.
Say whether it is a join semilattice, a meet semilattice, or both (and hence a lattice).

~~~ {.include-tikz size=mid}
lattice_pentagon.tikz
~~~
:::

::: exercise
Say whether the following statement is true or false.
Justify your answer.


If a poset $\tuple{S, \leq}$ with a finite carrier $S$ does not contain a unique element $x \in S$ such that $x \leq y$ for all $y \in S$, then this poset cannot be a meet semilattice.
:::

::: exercise
Say whether the following statement is true or false.
Justify your answer.


If a poset $\tuple{S, \leq}$ with a finite carrier $S$ contains a unique element $x \in S$ such that $x \leq y$ for all $y \in S$, then this poset is guaranteed to be a meet semilattice.
:::

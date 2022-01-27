# (Semi)Lattices

::: example
Let us return to the first example, where we saw that the set of upper bounds of $\setof{1}$ is $\setof{ \setof{1}, \setof{1,2}, \setof{1,3}, \setof{1,2,3} }$ while the least upper bound of $\setof{1}$ is $\setof{1}$ itself.
Following our definition, we compute the lub as 
$$\mathrm{lub}(\setof{\setof{1}}) = \mathrm{lb}(\mathrm{ub}(\setof{\setof{1}})) = \mathrm{lb}(\setof{ \setof{1}, \setof{1,2}, \setof{1,3}, \setof{1,2,3} }) = \setof{\setof{1}}.$$
This tells us that $\setof{1}$ is the only lub of $\setof{1}$, as expected.
:::

::: solution
Given the same poset as in the previous examples, compute all of the following:

- $\mathrm{lub}(\setof{\setof{1,2}, \setof{2,3}}) = \setof{\setof{1,2,3}}$
- $\mathrm{glb}(\setof{\setof{1,2}, \setof{2,3}}) = \setof{\setof{2}}$
- $\mathrm{lub}(\setof{\emptyset}) = \setof{\emptyset}$
- $\mathrm{glb}(\setof{\emptyset, \setof{1,2,3}}) = \setof{\emptyset}$
- $\mathrm{glb}(\setof{\setof{1}, \setof{2,3}, \setof{1,2,3}}) = \setof{\emptyset}$
- $\mathrm{lub}(\setof{\setof{1}, \setof{2}, \setof{3}}) = \setof{\setof{1,2,3}}$

:::

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

::: solution
Suppose towards a contradiction $\mathrm{lub}(T)$ contains at least two elements $x$ and $y$ such that $x \neq y$.
By definition, then, it must be the case that $x \leq y$ and $y \leq x$.
But since our structure is a poset, $\leq$ must be antisymmetric, so that $x \leq y$ and $y \leq x$ jointly imply $x = y$, which contradicts our initial assumption that $x \neq y$.
:::

::: exercise
Writing $\mathrm{glb}(\setof{s_1, \ldots, s_n})$ as $s_1 \wedge s_2 \wedge \cdots \wedge s_n$ is possible because $\wedge$ is an associative operation: $(x \wedge y) \wedge z = x \wedge (y \wedge z)$. 
Explain why $\wedge$ is associative.

*Hint*: You want to show that $\mathrm{glb}(\setof{ \mathrm{glb}(\setof{x, y}), z}) = \mathrm{glb}(\setof{x, \mathrm{glb}(\setof{y, z})})$ if one adopts the convention that the $\mathrm{glb}$ function returns a unique element rather than a set.
:::

::: solution
Assume w.l.o.g. that $\mathrm{glb}(\setof{x,y}) = a$ and $\mathrm{glb}(\setof{y,z}) = b$.
Then $\mathrm{glb}(\setof{\mathrm{glb}(\setof{x,y}), z}) = \mathrm{glb}(\setof{a,z})$ contains the unique $m$ such that $m \leq a$, $m \leq z$, and there exists no $m' \neq m$ such that $m \leq m'$, $m' \leq a$, and $m' \leq z$.
Since $a$ is the greatest lower bound of $x$ and $y$, we can restate this as $m \leq x$, $m \leq y$, $m \leq z$, and there exists no $m' \neq m$ such that $m \leq m'$, $m' \leq x$, $m' \leq y$, and $m' \leq z$.

Similarly, $\mathrm{glb}(\setof{x, \mathrm{glb}(\setof{y,z})}) = \mathrm{glb}(\setof{x,b})$ contains the unique $n$ such that $n \leq x$, $n \leq y$, and there exists no $n' \neq n$ such that $n \leq n'$, $n' \leq x$, and $n' \leq b$.
Since $b$ is the greatest lower bound of $y$ and $z$, this can be restated as $n \leq x$, $n \leq y$, $n \leq z$, and there exists no $n' \neq n$ such that $n \leq n'$, $n' \leq x$, $n' \leq y$, and $n' \leq z$.

Based on those definitions, it necessarily is the case that $m = n$.
:::

::: solution
For each one of the following depictions of a poset, say whether it is a join semilattice, a meet semilattice, both, or neither.

\begin{forest}
    [both
    [True, no edge
        [False]
    ]
    ]
\end{forest}

\begin{forest}
    [join (because $D \wedge C$ does not exist)
    [A, no edge
        [D]
        [B
            [C]
        ]
    ]
    ]
\end{forest}

\begin{forest}
    [neither (because $A \wedge E$ and $A \vee E$ do not exist)
    [,phantom, no edge
        [A
            [D]
            [B
                [C]
            ]
        ]
        [E]
    ]
    ]
\end{forest}

\begin{forest}
    [join ($D \wedge C$ still does not exist)
    [Y, no edge
        [A
            [D]
            [B
                [C,name=c]
            ]
        ]
        [E,name=e]
    ]
    ]
    %
    \draw (e.south) to (c.north);
\end{forest}

\begin{forest}
    [both
    [Y, no edge
        [A
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
\end{forest}

\begin{forest}
    [meet (because $X \vee Y$ does not exist)
    [,phantom, no edge
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
    ]
    %
    \draw (e.south) to (c.north);
    \draw (d.south) to (c.north);
    \draw (x.south) to (a.north);
\end{forest}

\begin{forest}
    [both
    [Z, no edge
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
    ]
    %
    \draw (e.south) to (c.north);
    \draw (d.south) to (c.north);
    \draw (x.south) to (a.north);
\end{forest}

\begin{forest}
    [neither (because $A \wedge E$ and $A \vee E$ are not unique)
    [Z, no edge
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
    ]
    %
    \draw (e.south) to (c.north);
    \draw (d.south) to (c.north);
    \draw (x.south) to (a.north);
    \draw (x.south) to (e.north);
\end{forest}

:::

::: exercise
Why don't we need to check $F \wedge T$ (or $F \vee T$)?
:::

:::
Because $\wedge$ and $\vee$ are commutative: $T \wedge F = \mathrm{glb}(\setof{T,F}) = \mathrm{glb}(\setof{F,T}) = F \wedge T$ (and the same for $\vee$).
:::

::: exercise
Consider the poset depicted below.
Say whether it is a join semilattice, a meet semilattice, or both (and hence a lattice).

~~~ {.include-tikz size=mid}
lattice_pentagon.tikz
~~~
:::

::: solution
It is a lattice.
For any two elements $x$ and $y$ such that $x \leq y$, we have $x \wedge y = x$ and $x \vee y = y$.
Hence we only need to consider the meet and join of elements that are unordered with respect to each other:

- $b \wedge c = a$
- $b \vee c = e$
- $d \wedge c = a$
- $d \vee c = e$

:::

::: exercise
Say whether the following statement is true or false.
Justify your answer.

If a poset $\tuple{S, \leq}$ with a finite carrier $S$ does not contain a unique element $x \in S$ such that $x \leq y$ for all $y \in S$, then this poset cannot be a meet semilattice.
:::

::: solution
This statement is true.
Since the carrier is finite, there must be at least one $x$ such that there is no $y \neq x$ with $y \leq x$.
If this $x$ is not unique, then there are at least two such $x_1$ and $x_2$, which must be unordered with respect to each other.
But then $\mathrm{lb}(\setof{x_1,x_2}) = \emptyset$ and $x_1 \wedge x_2$ is undefined, revealing the poset not to be a meet semilattice.
:::

::: exercise
Say whether the following statement is true or false.
Justify your answer.

If a poset $\tuple{S, \leq}$ with a finite carrier $S$ contains a unique element $x \in S$ such that $x \leq y$ for all $y \in S$, then this poset is guaranteed to be a meet semilattice.
:::

::: solution
This statement is false.
It suffices to exhibit a single counterexample.
Consider the poset $P \is \tuple{S, \leq}$ with carrier $S \is \setof{a,b,c,d,e}$ and a weak partial order $\leq$ such that $a \leq y$ for all $y \in S$.
Suppose furthermore that we have $b \leq d$, $b \leq e$, $c  \leq d$, $c \leq e$ and that $b$ is unordered to respect with $c$ and that $d$ is unordered with respect to $e$.
Then $d \wedge e$ is undefined and $P$ cannot be a meet semilattice.
:::

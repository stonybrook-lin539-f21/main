**Prerequisites**

- sets
- functions (notation)
- general (numbers)

# Sets as instances of multisets

Multisets are a natural generalization of sets.
But if this is true, then sets should fall out as just a special case of multisets.
Let us see if this is true.

First, every set $S$ can be regarded as a multiset with co-domain $\mathbb{N}$ but range $\setof{0,1}$.
All the members of $S$ are mapped to $1$, everything else to $0$.
So far so good.
Now consider the set operations union, intersection, and relative complement.
For multisets $A_M$ and $B_M$, $A_M \cup B_M$ maps every $a$ to $\max(A_M(a), B_M(a))$.
For sets, the only two possible values for $A_M(a)$ and $B_M(a)$ are $0$ and $1$.
Let's consider each scenario in turn with union:

- $a \in A$, $a \in B$, so $a \in A \cup B$; then $A_M(a) = B_M(a) = 1$, and $\max(1,1) = 1$, whence $a \in A_M \cup B_M$.
- $a \in A$, $a \notin B$, so $a \in A \cup B$; then $A_M(a) = 1$, $B_M(a) = 0$, and $\max(1,0) = 1$, whence $a \in A_M \cup B_M$.
- $a \notin A$, $a \in B$, so $a \in A \cup B$; then $A_M(a) = 0$, $B_M(a) = 1$, and $\max(1,0) = 1$, whence $a \in A_M \cup B_M$.
- $a \notin A$, $a \notin b$, so $a \notin A \cup B$; then $A_M(a) = 0$, $B_M(a) = 0$, and $\max(0,0) = 0$, whence $a \notin A_M \cup B_M$.

Intersection and relative complement work in exactly the same fashion.

Even the formula for cardinality works as expected: given a set $A$, $\card{A}$ is the number of elements it contains, whereas $\card{A_M}$ is the sum of the counts of each element.
But since every $a \in A_M$ has a count of $1$, this sum is the same as $\card{A}$:

\begin{align*}
    \card{A_M}  & = \sum_{a \in A_M} A_M(a)\\
                & = A_M(a_1) + \cdots + A_M(a_n)\\
                & = 1 + \cdots + 1\\
                & = \card{A}
\end{align*}


We can even confirm why the cardinality of the powerset of some set $S$ must be $2^{\card{S}}$.
The formula for calculating the cardinality of the powerset of a multiset $S_M$ is $\prod_{s \in S_M} (S_M(s) + 1)$.
Every member of a set has a count of $1$, for a set $S$ this formula expands to $\prod_{s \in S} (1 + 1) = \prod_s{ \in S}$.
So if $S$ has $n$ members, the cardinality of $\wp(S)$ is
$$
\underbrace{2 \times \cdots \times 2}_{n \text{ times}}.
$$
But that is the same as $2^n$, which is the same as $2^{\card{S}}$.
It all fits together exactly as it should.

This shows that multisets are indeed a faithful generalization of sets.
And it also gives us a good example of how one and the same object can be viewed in multiple ways.

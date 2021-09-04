**Prerequisites**

- sets (comparison, powerset)
- multisets (operations)

# Multiset relations

The (proper) subset and superset relations are readily extended to multisets.

::: definition
Given two multisets $A_M$ and $B_M$, $A_M$ is a subset of $B_M$ ($A_M \subseteq B_M$) iff it holds for all $a \in A_M$ that $A_M(a) \leq B_M(a)$.
The subset relation is proper ($A_M \subsetneq B_M$) iff $A_M(a) < B_M(a)$ for all $a \in A_M$.
Superset and proper superset are defined in an analogous fashion.
:::

Note that this definition of subset entails that the powerset of a multiset can be much larger than that of a set.

::: example
Returning once more to $A_M \is \setof{a:3, b:2, c:1}$ and $B_M \is \setof{a:1, b:1, c:2, d:1}$, we can see immediately that neither is a subset of the other.
First, $A_M \not\subseteq B_M$ because $A_M(a) = 3 \not\leq 1 = B_M(a)$.
In the other direction, $B_M \not\subseteq A_M$ because $B_M(d) = 1 \not\leq 0 = A_M(d)$.

The powerset of $B_M$ contains every multiset that is a subset of $B_M$.
These are

- $\setof{a:1, b:1, c:2, d:1}$
- $\setof{a:1, b:1, c:2, d:0}$
- $\setof{a:1, b:1, c:1, d:1}$
- $\setof{a:1, b:1, c:1, d:0}$
- $\setof{a:1, b:1, c:0, d:1}$
- $\setof{a:1, b:1, c:0, d:0}$
- $\setof{a:1, b:0, c:2, d:1}$
- $\setof{a:1, b:0, c:2, d:0}$
- $\setof{a:1, b:0, c:1, d:1}$
- $\setof{a:1, b:0, c:1, d:0}$
- $\setof{a:1, b:0, c:0, d:1}$
- $\setof{a:1, b:0, c:0, d:0}$
- $\setof{a:0, b:1, c:2, d:1}$
- $\setof{a:0, b:1, c:2, d:0}$
- $\setof{a:0, b:1, c:1, d:1}$
- $\setof{a:0, b:1, c:1, d:0}$
- $\setof{a:0, b:1, c:0, d:1}$
- $\setof{a:0, b:1, c:0, d:0}$
- $\setof{a:0, b:0, c:2, d:1}$
- $\setof{a:0, b:0, c:2, d:0}$
- $\setof{a:0, b:0, c:1, d:1}$
- $\setof{a:0, b:0, c:1, d:0}$
- $\setof{a:0, b:0, c:0, d:1}$
- $\setof{a:0, b:0, c:0, d:0}$

The powerset of $B \is \setof{a,b,c,d}$, on the other hand, has only $2^{\card{B}} = 2^4 = 16$ members.

The contrast is even more pronounced when we consider a multiset like $\setof{a:9}$.
While $\wp(\setof{a})$ only consists of $\emptyset$ and $\setof{a}$, $\wp(\setof{a:9})$ has $10$ members.
:::

::: jupyterpython
def is_subset(A, B):
    for a in A.elements():
        if A[a] > A[b]:
            return False
    return True

def powerset(A):
    ps = [A]
    for key in A.keys():
        for val in range(A[key]):
            buffer = []
            for subset in ps:
                subset = subset.copy()
                subset[key] = val
                if subset not in buffer:
                    buffer.append(subset)
            ps += buffer
    return(ps)

from pprint import pprint
from collections import Counter

A = Counter({"a": 3, "b": 2, "c": 1})
B = Counter({"a": 1, "b": 1, "c": 2, "d": 1})

print("Powerset of {} is:".format(B))
pprint(powerset(B))

print()
print("Powerset of {} is:".format(A))
pprint(powerset(Counter(A)))
:::

The cardinality of the powerset of a multiset is computed by adding 1 to each count and then multiplying all counts.
Again we can express this more precisely and succinctly with a formula:

$$
\card{\wp(S_M)} \is \prod_{s \in S_M} \left ( S_M(s) + 1 \right )
$$

The operator $\prod$ behaves exactly like $\sum$, except that it is a shorthand for multiplication rather than addition.
So the formula above expands to $( S_M(s_1) + 1 ) \mult ( S_M(s_2) + 1 ) \mult \cdots \mult ( S_M(s_n) + 1 )$.

::: example
We have already seen that $B_M \is \setof{a:1, b:1, c:2, d:1}$ has 24 subsets, so its powerset has cardinality 24.
Our formula yields exactly the same value.

\begin{align*}
    \card{\wp(B_M)} &= \prod_{s \in B_M} \left ( B_M(s) + 1 \right )\\
                    &= ( B_M(a) + 1 ) \mult ( B_M(b) + 1 ) \mult ( B_M(c) + 1 ) \mult (B_M (d) + 1 )\\
                    &= ( 1 + 1 ) \mult ( 1 + 1 ) \mult ( 2 + 1 ) \mult ( 1 + 1 )\\
                    &= 2 \mult 2 \mult 3 \mult 2\\
                    &= 24\\
\end{align*}
:::

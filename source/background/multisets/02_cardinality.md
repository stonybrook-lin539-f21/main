**Prerequisites**

- general (big operators)
- sets (cardinality)
- multisets (operations)

# Cardinality of multisets

Given a multiset $S_M$, we write $S_M(a)$ for the count of $a$ in $S_M$.

::: example
Let $A_M \is \setof{a:3, b:2, c:1}$ and $B_M \is \setof{a:1, b:1, c:1, d:1}$.
Then $A_M(a) = 3$ and $B_M(a) = 1$, whereas $A_M(c) = B_M(c) = 1$.
:::

The **cardinality** of a multiset with finitely many elements is the sum of all its counts.
As a formula, this looks as follows:

$$
    \card{S_M} \is \sum_{s \in S_M} S_M(s)
$$

This formula uses the symbol $\sum$ as an abbreviation for addition.
The subscript on $\sum$ tells us that $s$ should be substituted in all possible ways by elements of $S_M$.
For multiset $S_M \is \setof{s_1: c_1, s_2: c_2, \ldots , s_n: c_n}$ the formula expands to $S_M(s_1) + S_M(s_2) + \cdots + S_M(s_n)$, which in turn reduces to $c_1 + c_2 + \cdots + c_n$.

::: example
Consider once more the multisets $A_M \is \setof{a:3, b:2, c:1}$ and $B_M \is \setof{a:1, b:1, c:2, d:1}$, for which the following hold:

\begin{align*}
    \card{A_M} &= \sum_{s \in A_M} A_M(s)\\
               &= A_M(a) + A_M(b) + A_M(c)\\
               &= 3 + 2 + 1\\
               &= 6\\
    \card{B_M} &= \sum_{s \in B_M} B_M(s)\\
               &= B_M(a) + B_M(b) + B_M(c) + B_M(d)\\
               &= 1 + 1 + 2 + 1\\
               &= 5\\
    \card{A_M \cup B_M} &= 8\\
    \card{A_M \cap B_M} &= 3\\
    \card{A_M - B_M} &= 3\\
    \card{B_M - A_M} &= 2\\
\end{align*}
:::

::: jupyterpython
def card(multiset):
    return sum(multiset.values())

print("|{}| = {}".format(A, card(A)))
print("|{}| = {}".format(B, card(B)))
print("Union of {} and {} is {}".format(A, B, multiset_union(A, B)))
print("Intersection of {} and {} is {}".format(A, B, multiset_intersection(A, B)))
print("Relative complement of {} and {} is {}".format(A, B, A-B))
:::

::: exercise
Calculate the cardinality of the following multisets:


- $\setof{a:17}$
- $\setof{\text{John}: 5, \text{Mary}: 5, \text{Bill}: 10}$
- $\setof{a: 0, b: 0, c:0}$

:::

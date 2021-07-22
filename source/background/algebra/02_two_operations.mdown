# Algebras with two operations

The notions of magma, semigroup, monoid, and group only apply to algebras with a single operation.
But of course one can easily imagine algebraic structures with multiple operations.
The natural numbers with addition and multiplication are one of the most natural examples that you have all known since grade school, although you probably didn't call it an algebraic structure back then.

Mathematicians have also studied such algebraic structures in great depth, and you can spend an entire lifetime learning about them.
Perhaps the three most important types, however, are semirings, rings, and fields.
This notebook focuses almost exclusively on semirings as rings and fields are again not that common in linguistics.
But since rings and fields are just special cases of semirings, the latter still provide a good foundation for understanding the former.

## Semirings

### Definition

Intuitively, a semiring is a combination of two monoids over the same carrier set.
But not any arbitrary monoids will do, instead the two monoids have to be tightly integrated.

::: definition
An algebra $\tuple{C, \oplus, \otimes, 0, 1}$ is a **semiring** iff all of the following hold:


- $\tuple{C, \oplus, 0}$ is a commutative monoid
- $\tuple{C, \otimes, 1}$ is a monoid
- $\otimes$ distributes over $\oplus$:
  $a \otimes (b \oplus c) = (a \otimes b) \oplus (a \otimes c)$
  and
  $(b \oplus c) \otimes a = (b \otimes a) \oplus (c \otimes a)$
- $0$ is an annihilator for $\otimes$: $a \otimes 0 = 0 \otimes a = 0$

:::

::: example
The prototypical semiring is the natural numbers with addition and multiplication: $\tuple{\mathbb{N}, +, \times, 0, 1}$.


First of all, it holds that $\tuple{\mathbb{N}, +, 0}$ is a commutative monoid and $\tuple{\mathbb{N}, \times, 1}$ is a monoid (also a commutative one, in fact, but that's not required by the definition of semiring).
Second, addition distributes over multiplication in the intended fashion:

$$
5 \times (7 + 3) = (7 \times 5) + (3 \times 5) = 50 = 5 \times 10
$$

Since multiplication is commutative, this also shows that $5 \times (7 + 3) = (5 \times 7) + (3 \times 7)$. 
As desired, then, distributivity holds irrespective of the order of arguments.
Finally, the identity element for addition is $0$, and $n \times 0 = 0 \times n = 0$ for every natural number $n$.
So the additive identity is indeed an annihilator for multiplication.
This takes care of the last property, showing that we do indeed have a semiring.
:::

### Detailed discussion

The example might have clarified things a bit, but it's still a good idea to go through the definition step by step.
The first thing to keep in mind here is that $0$ and $1$ do not refer to the actual numbers $0$ and $1$.
They are just arbitrary names for the identities, we could have just as well called them $x$ and $y$.
The names $0$ and $1$ are inspired by the fact that if one interprets $\oplus$ as addition and $\otimes$ as multiplication (as we did in the previous example), then their respective identity elements are indeed the numbers $0$ and $1$.
But since $\oplus$ and $\otimes$ stand for arbitrary operations, the identity elements might not even be numbers at all in the general case.

::: example
Suppose we generalize the string concatenation operation $\stringcat$ from strings to sets of strings such that $U \stringcat V = \setof{ u \stringcat v \mid u \in U, v \in V}$.
For example, $\setof{ \String{ab}, \String{c} } \stringcat \setof{ \String{dab}, \String{c} } = \setof{ \String{abdab}, \String{abc}, \String{cdab}, \String{cc}}$.
Then $\tuple{ \wp(\Sigma^*), \cup, \stringcat, \emptyset, \setof{\emptystring}}$ is a semiring.
Notice that the identity elements are now $\emptyset$ for $\cup$ and $\setof{\emptystring}$ for the generalized string concatenation operation $\stringcat$.
:::

::: exercise
Show that both of the following hold:


- $\tuple{ \wp(\Sigma^*), \cup, \emptyset }$ is a commutative monoid
- $\tuple{ \wp(\Sigma^*), \stringcat, \setof{\emptystring}}$ is a monoid

:::

Next, the distributive property has to hold in both directions.
If $\otimes$ is commutative, it suffices to check distributivity in one direction, but for non-commutative $\otimes$ both directions have to be checked.

::: exercise
Show with a concrete example that our generalized version of $\stringcat$ is not commutative.
Then give two concrete examples for each one of the following distributivity equations:


- $A \stringcat (B \cup C) = (A \stringcat B) \cup (A \stringcat C)$
- $(B \cup C) \stringcat A = (B \stringcat A) \cup (C \stringcat A)$

:::

The last condition requires that the additive identity also plays a special role for the multiplicative operation: it must be an annihilator.
Whereas an identity element for operation $O$ makes $O$ map everything to itself, an annihilator instead makes $O$ map everything to said annihilator.
In formal terms: an identity $e$ has the property $x \otimes e = e \otimes x = x$, whereas an annihilator $a$ gives $x \otimes a = a \otimes x = a$ (note that both directions must hold even if $\otimes$ is not commutative).
Just like distributivity, the requirement that the additive identity must also be a multiplicative annihilator establishes a close link between the two monoids.
This is the very essence of a semiring: two monoids that are tightly integrated.

::: exercise
The identity element for $\cup$ is $\emptyset$.
Explain why $\emptyset$ is an annihilator for our set-version of $\stringcat$.
:::

One more thing!
While it is common usage to call $\oplus$ the additive operation and $\otimes$ the multiplicative operation, this does not entail that the operations are exactly like addition and multiplication.
Any two operations will do as long as they meet all the required axioms.
However, what axioms must be met differs between the two operations.
Only $\oplus$ absolutely has to be commutative.
It has to be the case that $\otimes$ distributes over $\oplus$, but not the other way round.
And while the identity for $\oplus$ must be an annihilator for $\otimes$, the opposite need not hold (though it certainly can in some cases).

::: exercise
Suppose that we swap the operations in our semiring so that we get $\tuple{\wp(\Sigma^*), \stringcat, \cup, \setof{\emptystring}, \emptyset}$.
Give all the reasons why this is no longer a semiring.
:::

Just like monoids and groups, semirings have the advantage that they establish connections between mathematical ideas that seem entirely unrelated.
At first glance, addition and multiplication of natural numbers has nothing to do with constructing sets of strings via concatenation and union.
But the algebraic analysis of the two systems reveals important similarities.
Knowing that two systems are semirings is similar to knowing that two phonological phenomena are tier-based strictly local.
It does not tell the full story, but it gives you an important baseline that you can make good use of for various purposes.

::: exercise
Which one of the following are semirings?
Justify your answer!
If an algebraic structure is not a semiring, it is enough to list one axiom that is not satisfied (as an extra challenge, you may try to list as many reasons as possible).


- $\tuple{ \setof{0,1}, \max, \min, 0, 1 }$ 
- $\tuple{ \mathbb{N}, +, +, 0, 0 }$ 
- $\tuple{ \Sigma^*, \mathrm{lcs}, \stringcat, \emptystring, \emptystring }$, where $\mathrm{lcs}(u,v)$ returns the longest common substring of $u$ and $v$;
for instance, $\mathrm{lcs}(baaaa, aaaab) = aaaa$

- 
$\tuple{ \mathbb{N} \times \Sigma^*, \oplus, \otimes, \tuple{0,\emptyset}, \tuple{1, \setof{\emptystring}} }$, where $\tuple{m, A} \oplus \tuple{n, B} = \tuple{m + n, A \cup B}$ and $\tuple{m, A} \otimes \tuple{n, B} = \tuple{m \times n, A \stringcat B}$


:::

## Rings and fields

Now that you have a better idea what semirings are, rings and fields are easy.
A **ring** is a semiring $\tuple{C, \oplus, \otimes, 0, 1}$ where $\oplus$ also has an inverse.
So $\tuple{C, \oplus, 0}$ isn't just a commutative monoid, but a commutative (= Abelian) group.

::: example
We already encountered $\tuple{ \mathbb{N}, +, \times, 0, 1}$ as an example of a semiring.
This structure is not a ring since addition has no inverse.
But we can broaden $\mathbb{N}$ to $\mathbb{Z}$, the set of integers.
Then every number has an inverse for addition, so that $\tuple{\mathbb{Z}, +, 0}$ forms an Abelian group.
And hence $\tuple{ \mathbb{Z}, +, \times, 0, 1 }$ is a ring.
:::

If the multiplicative operation $\otimes$ also gives rise to an Abelian group, the ring is a **field**.

::: example
While $\tuple{ \mathbb{Z}, +, \times, 0, 1}$ is a ring, it is not a field.
That is because the set of integers does not provide multiplicative inverses.
But we can again broaden the carrier set, this time from the set $\mathbb{Z}$ of integers to the set $\mathbb{Q}$ of rationals.
The structure $\tuple{ \mathbb{Q}, \times, 1}$ is an Abelian group, as is $\tuple{ \mathbb{Q}, +, 0 }$.
So $\tuple{ \mathbb{Q}, +, \times, 0, 1 }$ is a semiring that is built from two Abelian groups, making it a field.
:::

As mentioned at the beginning, rings and fields are better known than semirings, but the latter are more important for anything related to formal language theory.
So if you can only remember one of the three, make sure it's semirings.
But anybody who understands how a semiring works will also have an easy time remembering rings and fields as special cases of semirings.

| Structure | $\oplus$     | $\otimes$   |
| --:       | :-:          | :-:         |
| Semiring  | comm. monoid | monoid      |
| Ring      | comm. group  | monoid      |
| Field     | comm. group  | comm. group |

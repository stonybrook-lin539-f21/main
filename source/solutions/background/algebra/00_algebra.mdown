# Algebras

## Definition

You're all familiar with the subfield of **algebra**, which is covered extensively in middle school and high school.
But **algebra** isn't just the name of a field, it is also the name of a specific kind of mathematical object.

::: definition
An **algebra** (or **algebraic structure**) $\mathcal{A} \is \tuple{C, \oplus}$ consists of a set $C$ (the **carrier**) and a finitary operation $\oplus$.
:::

An operation is finitary iff it only takes a fixed number of arguments.

::: example
Addition is finitary, as it takes two arguments.
This makes it a binary operation.
:::

::: example
The infinite sum operation takes infinitely many values and returns their sum.
For example, one might feed this function the values $1$, $0.1$, $0.01$, $0.001$, $\ldots$, and obtain the sum $1.111\cdots$.
This operation is not finitary.
:::

All operations we will consider are finitary.
In fact, we will focus exclusively on binary operations, as little else is every needed for linguistics.

Even with this simplification, though, algebras are very abstract objects.
It's not surprising that the subfield of mathematics that studies algebras is called **abstract algebra**.
The abstractness of algebras, while initially disorienting, is incredibly useful because it reveals similarities between mathematical objects that look very different.
For example, $\mathbb{N}$ with addition and $\Sigma^*$ with string concatenation are very similar algebraically.
Do not worry too much about abstractness, we will quickly home in on specific subtypes of algebras that are of interest for linguistics.

## Total and partial algebras

The definition above does not tell us much about $\oplus$.
One of the most basic requirements is that $\oplus$ should be defined for all elements of the carrier.
That is to say, there are no inputs for which $\oplus$ does not have a defined output.
In this case, the algebra is **total**, otherwise it is **partial**.

::: definition
An algebra $\mathcal{A} \is \tuple{C, \oplus}$ is **total** iff $a \oplus b$ is defined for all $a, b \in C$.
Otherwise $\mathcal{A}$ is **partial**.
:::

::: example
Consider $\tuple{\mathbb{N}, +}$, the algebra of natural numbers with addition.
There are no two natural numbers $a$ and $b$ such that $a + b$ is undefined.
Hence $\tuple{\mathbb{N}, +}$ is a total algebra.
:::

::: example
Consider $\tuple{\mathbb{N}, /}$, the natural numbers with division.
This algebra is partial because $\frac{a}{b}$ is undefined if $b = 0$.
:::

Careful: the term **total** for algebras is intuitively similar to a relation being total as both convey that the operation or relation does not miss any elements.
But do not put too much stock into this, the two are still distinct properties and should not be confused.
A total algebra and a total relation are not the same thing.

We will only consider total algebras, which are much better behaved than partial algebras.


## Magma: Closure under $\oplus$

Another standard assumption for algebras is that they are closed under their operation.
Such an algebra is called a **magma**.

::: definition
An algebra $\tuple{C, \oplus}$ is a **magma** iff $a \oplus b \in C$ for all $a, b \in C$.
:::

::: example
Consider once more the algebra $\tuple{\mathbb{N}, +}$.
Clearly, $x + y$ is a natural number as long as $x$ and $y$ are natural numbers.
So the set of natural numbers is closed under addition, making $\tuple{\mathbb{N}, +}$ a magma.
:::

::: example
The partial algebra $\tuple{\mathbb{N}, /}$ is not a magma.
This is witnessed by $\frac{3}{2} = 1.5$.
Even though $3$ and $2$ are natural numbers, division maps them to a value that is not a natural number.
:::

::: exercise
Whether $\tuple{\mathbb{N}, -}$ is a magma depends on one's definition of subtraction.
Explain why!
:::

::: exercise
Which of the following is a magma?
Give counterexamples where necessary.


- the integers with subtraction
- the rationals with multiplication
- the odd natural numbers with addition
- $\Sigma^*$ with string concatenation
- the set of all English sentences with sentence-level conjunction via *and*
- the set of all creatures that ever lived, under the ancestor operation $\oplus$ (where $a \oplus b$ returns the closest shared ancestor of $a$ and $b$, $a \oplus a = a$).

:::

Almost every algebra you will ever come across is total and a magma.
Without those two properties, algebras get a lot harder to study.
The more properties are heaped on, the better behaved algebras are.
Three types of algebras are of particular importance: semigroups, monoids, and groups.
They are covered in the next notebook.

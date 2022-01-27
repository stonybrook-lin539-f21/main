# Tuples: Basics

Like sets, tuples are collections of elements.
Like multisets, tuples also allow on element to be present multiple times, so they are not idempotent.
Unlike multisets, tuples also care about the order of the elements.
All of this means that tuples are the result of taking a multiset and adding order.
This makes them very similar to strings, but tuples are more general because they can contain arbitrary objects, including other tuples.


## Basic properties

An $n$-tuple $t$ consists of exactly $n$ elements.
We also say that $t$ has **length** $n$.
Tuples are usually written between pointy brackets, e.g. the pair $\tuple{a,b}$, the triple $\tuple{a,b,c}$, or the $1$-tuple $\tuple{a}$.

::: example
The pair $\tuple{a,a}$ is distinct from the 1-tuple $\tuple{a}$, the triple $\tuple{a,a,a}$, or the $4$-tuple $\tuple{a,a,a,a}$.
Since order matters, we also have $\tuple{a,b} \neq \tuple{b,a}$ if $a \neq b$.
If, say, $a = b = 1$ then $\tuple{a,b} = \tuple{1,1} = \tuple{b,a}$.
:::

::: example
Tuples may contain other objects, including other tuples.
The content of these objects is not considered when computing a tuples length.
Hence $\tuple{a,b}$ and $\tuple{a,\setof{b,c}}$ are distinct tuples, but they are both of length 2.
:::

::: exercise
Fill in the gaps with $=$ and $\neq$ as appropriate, assuming that $a$ and $b$ are distinct elements:

- $\tuple{a} \_ \tuple{b}$
- $\tuple{a,b,a} \_ \tuple{a,b,b}$
- $\tuple{a,b,a,a} \_ \tuple{a,b,a,a}$
- $\tuple{a,a,b,a} \_ \tuple{a,b,a,a}$
- $\tuple{a,a,b,a} \_ \tuple{a,a,\setof{b},a}$
- $\tuple{a,a,b,a} \_ \tuple{a,\tuple{a,b},a}$
:::

One often writes $A^n$ for the set of all $n$-tuples whose elements are drawn from $A$.

::: example
Suppose $A \is \setof{a,b}$.

- $A^2 = \setof{ \tuple{a,a}, \tuple{a,b}, \tuple{b,a}, \tuple{b,b}}$
- $A^1 = A = \setof{ \tuple{a}, \tuple{b}}$

:::

::: exercise
If $A \is \setof{a}$, then what is $A^5$?
:::

::: exercise
If $A \is \setof{\setof{a}}$, then what is $A^1$?
:::

Note that just like $a \neq \setof{a}$, it also holds that $a \neq \tuple{a}$.
A container with $a$ in it is not the same thing as $a$ by itself.


## Concatenation

Two tuples $a$ and $b$ can be concatenated into a single large tuple $a \tuplecat b$ that contains all elements of $a$ and $b$, in the same order.

::: definition
Given an $m$-tuple $a \is \tuple{a_1, \ldots, a_m}$ and an $n$-tuple $b \is \tuple{b_1, \ldots, b_n}$,
their **concatenation** is the $m+n$-tuple
$a \tuplecat b \is \tuple{a_1, \ldots, a_m, b_1, \ldots, b_n}$.
:::

Tuple concatenation is associative.
This means that for any tuples $a$, $b$, and $c$, it holds that $a \tuplecat (b \tuplecat c) = (a \tuplecat b) \tuplecat c$.

::: example
The concatenation of $\tuple{x,y}$ and $\tuple{z}$ is $\tuple{x,y,z}$.
If we concatenate $\tuple{x,y,z}$ and $\tuple{y,y,y}$, we get $\tuple{x,y,z,y,y,y}$.

We could have gotten the same result by proceeding in a different order.
We first concatenate $\tuple{z}$ and $\tuple{y,y,y}$ into $\tuple{z,y,y,y}$.
We then concatenate $\tuple{x,y}$ and $\tuple{z,y,y,y}$ to obtain $\tuple{x,y,z,y,y,y}$.
That's indeed the same output as before.
Overall, then,
$$(\tuple{x,y} \tuplecat \tuple{z}) \tuplecat \tuple{y,y,y} = \tuple{x,y} \tuplecat (\tuple{z} \tuplecat \tuple{y,y,y}) = \tuple{x,y,z,y,y,y,y}.$$
:::

::: exercise
Calculate the result of the following concatenations:

- $\tuple{a,b} \tuplecat ((\tuple{c} \tuplecat \tuple{a,b}) \tuplecat \tuple{a,c,e})$
- $(\tuple{a,b} \tuplecat \tuple{c}) \tuplecat (\tuple{a,b} \tuplecat \tuple{a,c,e})$

:::

::: exercise
Write down all possible ways of obtaining $\tuple{a,b,c,d}$ via concatenation of tuples whose length is at least $1$.
For instance, one possible way is $\tuple{a,b} \tuplecat \tuple{c, d}$, but there's several more.
:::

::: exercise
Tuple concatenation is not commutative.
That is to say, for some tuples $a$ and $b$ it is not the case that $a \tuplecat b = b \tuplecat a$.
Illustrate this with an example.
:::


## The empty tuple

Remember that strings had a special empty string $\emptystring$.
The tuple-counterpart for this is the **empty tuple** $\tuple{}$.
It is the only 0-tuple.
With respect to concatenation, the empty tuple behaves like $0$ with respect to addition.
That is to say, concatenating a tuple with the empty tuple does not change said tuple.

::: exercise
Compute $\tuple{a} \tuplecat \tuple{}$ and $\tuple{} \tuplecat \tuple{a,a,a}$.
:::


## Difference to strings

Strings can be regarded tuples over some fixed alphabet of symbols.
For instance, the string $\String{abc}$ can be viewed as the tuple $\tuple{a,b,c}$.
However, tuples are more general because their elements do not need to be symbols of some alphabet.
Just like sets and multisets, tuples can contain arbitrary objects.
So a tuple may consist of sets, multisets, other tuples, functions, relations, any combination of those, and much, much more.

::: example
All of the following are valid tuples:


- $\tuple{\setof{5, -5}, 25}$ is a pair that consists of the set $\setof{5, -5}$ and the number $25$
- $\tuple{\mathbb{N}, \mathbb{N}, \mathbb{N}}$ is a triple where each component is the set of natural numbers
- $\tuple{\mathbb{N}, \setof{3,7, \setof{112}}, +, -}$ is a $4$-tuple that consists of the set of natural numbers, the set $\setof{3,7, \setof{112}}$, and the operations of addition and subtraction
- $\tuple{a, \tuple{b, \tuple{}, \tuple{c}, \tuple{d,e}, b}, \setof{1,2,3, \tuple{}}}$ is triple that consists of $a$, the 5-tuple $\tuple{b, \tuple, \tuple{c}, \tuple{d,e}, b}$, and the set $\setof{1,2,3, \tuple{}}$

:::

::: exercise
What is the length of the following tuples?

- $\tuple{a,b,c}$
- $\tuple{a, \tuple{b,c}}$
- $\tuple{\tuple{a}, \tuple{b}, \tuple{c}}$
- $\tuple{\tuple{a,b,c}}$
- $\tuple{\tuple{}, \tuple{}, \tuple{}}$

:::

::: exercise
Does the concatenation of $\tuple{a,b}$ and $\tuple{c}$ yield the same result as the concatenation of $\tuple{a,b}$ and $\tuple{\tuple{c}}$?
Justify your answer!
:::


## Recap

- Tuples can be regarded as a generalization of strings.
  In fact, strings are often defined as just a shorthand notation for tuples.
- Like strings, tuples are ordered ($\tuple{a,b} \neq \tuple{b,a}$) and lack idempotency ($\tuple{a} \neq \tuple{a,a}$).
- Tuples can be concatenated, again just like strings.
- The empty tuple $\tuple{}$ contains no elements at all.
  It is the tuple-counterpart to the empty string $\emptystring$.
- In contrast to strings, tuples can consist of objects of arbitrary complexity, not just symbols drawn from a fixed alphabet.

|           | **unordered** | **idempotent** | **can only contain symbols** |
| --:       | :-:           | :-:            | :-:                          |
| sets      | Y             | Y              | N                            |
| multisets | Y             | N              | N                            |
| tuples    | N             | N              | N                            |
| strings   | N             | N              | Y                            |


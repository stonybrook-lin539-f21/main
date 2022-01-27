# Relations

::: exercise
Let $R$ be the relation that connects words to their parts of speech (N for nouns, V for verbs, A for adjectives, P for prepositions, D for determiners, and so on).
List the following for English:

- export $R$
- apple $R$
- $R$ P

:::

::: solution

- export $R$ = $\setof{\text{N}, \text{V}}$
- apple $R$ = $\setof{\text{N}}$
- $R$ P = $\{ p \mid p \text{ is a preposition of English} \} = \{ \text{above}, \text{at}, \text{because of}, \text{before}, \text{behind}, \text{in}, \text{inside}, \text{into}, \text{near}, \text{of}, \text{off}, \text{on}, \text{onto}, \text{to}, \text{under} \}$ (and any others I might have missed)

:::

::: exercise
For each one of the following, say whether it is a function or just a relation.

- the parent-of relation (e.g. $j \mathrel{P} m$ for "John is a parent of Mary")
- the parent-of relation in a world where the one-child policy is enforced globally
- the relation between a car's license plate and its owners
- the prefix relation, where $u$ is a prefix of $v$ iff there is some $w \in \Sigma^*$ such that $v = u \stringcat w$

:::

::: solution

- the parent-of relation is not a function since one individual can be the parent of multiple children
- the parent-of relation in a world where the one-child policy is enforced globally is a function
- the relation between a car's license plate and its owners is a relation assuming that a car can have multiple owners
- the prefix relation is a relation because a string can be a substring of more than one string

:::

::: exercise
Is the following statement true or false?
Justify your answer.

Every relation $R$ can be regarded as a function that maps $x$ to $x \mathrel{R}$.
:::

::: solution
This statement is correct: $\tuple{x,y} \in R$ iff $y \in x \mathrel{R}$ iff $y \in f(x)$.
In addition, $f$ is guaranteed to be a function because there can be no $x$ such that $x \mathrel{R}$ is anything but a single, invariant set.
:::

# Boolean lattices

The fact that De Morgan's law holds for sets as well as propositional logic is no accident.
The two are close siblings from an algebraic perspective.

Let $S$ be some fixed set.
We may order $\wp(S)$ by the subset relation to obtain the familiar powerset lattice, with join corresponding to union and meet to intersection.
In fact, this lattice satisfies two additional properties that make it a **Boolean lattice** (or **Boolean algebra**).

::: definition
A lattice $\tuple{L, \leq}$ is


- **distributive** iff join distributes over meet, and the other way round,
- **bounded** iff there is a least element 0 and and a greatest element 1 such that for all $l \in L$, $0 \leq l \leq 1$,
- **complemented** iff every eleement $a$ has a complement $\neg a$ such that $a \wedge \neg a = 0$ and $a \vee \neg a = 1$.

A lattice is **Boolean** iff it satisfies all three of the criteria.
:::

::: exercise
Show that $\tuple{\wp(S), \subseteq}$ is a Boolean lattice.
More specifically:


- Show that distributivity holds: $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ and $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
- What are the least and greatest elements of $\wp(S)$?
- For any arbitrary $A \in \wp(S)$, what is its complement $\neg A$?

:::

As you might already expect, propositional logic also has the structure of a Boolean lattice.
All we have to do is figure out the carrier set, and the rest will follow immediately.
First, let $L$ be the set of all propositional formulas.
We define an ordering $\leq$ such that $\phi \leq \psi$ ($\phi, \psi \in L$) iff $\phi$ always entails $\psi$.
In other words, $\phi \leq \psi$ iff $\phi \rightarrow \psi$ is a tautology.

We're almost done, but not quite.
Note that $\tuple{L, \leq}$ is not a poset because antisymmetry is violated.

::: example
Consider the formulas $a$ and $\neg \neg a$.
Clearly $a \rightarrow \neg \neg a$ and $\neg \neg a \rightarrow a$. 
So we ahve $a \leq \neg \neg a$ and $\neg \neg a \leq a$, yet $a$ and $\neg \neg a$ are distinct memebers of $L$. 
This contradicts antisymmetry.
:::

In order to fix this, we instead look at the quotient structure $\tuple{L_\sim, \leq}$, where $\phi \sim \psi$ iff $\phi$ and $\psi$ entail each other.
So $L_\sim$ consists of equivalence classes of propositional formulas whose truth values never differ from each other.
Strictly speaking, we have to define $\leq$ for this new set $L_\sim$, but the idea is simple: $[\phi] \leq [\psi]$ iff $\phi$ entails $\psi$.
That is to say, we can order any two equivalence classes by looking at the entailment between their respective members.
This makes $\tuple{L_\sim, \leq}$ a poset.

Note that there is a unique least element, the equivalence class $[a \wedge \neg a]$, or simply $[\bot]$.
And there is a unique greatest element $[a \vee \neg a]$, or simply $[\top]$.
Any two elements $[\phi]$ and $[\psi]$ have a unique join $[\phi \vee \psi]$, and a unique meet $[\phi \wedge \psi]$.
So the lattice operations of join ($\vee$) and meet ($\wedge$) correspond exactly to logical or ($\vee$) and logical and ($\wedge$).
We already know that the latter are distributive, and it is also easy to see that for every $[\phi] \in L$ there is some complement $\neg [\phi] \in L$ such that $[\phi] \wedge \neg [\phi] = [\bot]$ and $[\phi] \vee \neg [\phi] = [\top]$.
In fact, this complement $\neg [\phi]$ is simply $[\neg \phi]$, showing the close connection between logical negation and complement in this structure.
Overall, then, $\tuple{L_\sim, \leq}$ is a poset where any two elements have a unique join and meet, where join and meet distribute over each, with unique least and greatest bounds, and a complement for every element of the $L_\sim$.
That's just a very roundabout way of saying that $\tuple{L_\sim, \leq}$ is a Boolean lattice, just like $\tuple{\wp(S), \subseteq}$, and that's why De Morgan's Law holds for both sets and propositional logic.

::: exercise
Instead of the propositional formulas themselves, we could also look at their truth values.
Show that $\tuple{ \setof{F, T}, \leq }$ with $F \leq T$ is also a Boolean lattice.
:::

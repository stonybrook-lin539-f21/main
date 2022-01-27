# Tautologies

A tautology is a formula that is always true, irrespective of what assignment function one picks.
A simple example is $a \vee \neg a$.

| $a$ | $\vee$ | $\neg$ | $a$ |
| :-: | :-:    | :-:    | :-: |
| 0   | 1      | 1      | 0   |
| 1   | 1      | 0      | 1   |

Sometimes the **verum** symbol $\top$ is used to denote an arbitrary tautology.
So $\top$ is short for a proposition that is always true.
Its opposite is the **falsum** $\bot$, which is always false.

Tautologies are very useful for simplifying formulas.
For one thing, if one knows that the formula $\phi$ is a tautology, then one can always replace it by $1$ without computing the truth values of any of its parts.
But one can also use tautologies to convert $\phi$ into a fully equivalent yet distinct formula $\psi$.

The rest of this section lists some important tautologies.

## Commutativity of $\wedge$ and $\vee$

From the truth tables of $\wedge$ and $\vee$, it follows immediately that

- $\phi \wedge \psi \leftrightarrow \psi \wedge \phi$
- $\phi \vee \psi \leftrightarrow \psi \vee \phi$

## Double negation

It always holds that $\phi$ is equivalent to $\neg \neg \phi$, no matter what formula or propositional symbol $\phi$ corresponds to.
So $\phi \leftrightarrow \neg \neg \phi$ is a tautology.

::: exercise
Explain how this also entails that $\neg \phi \leftrightarrow \neg \neg \neg \phi$.
:::

## De Morgan's Law

In set theory, De Morgan's law states that $A \cap B = \overline{\overline{A} \cup \overline{B}}$ and $A \cup B = \overline{\overline{A} \cap \overline{B}}$.
A direct analogue of that holds in propositional logic.
Both of the following are tautologies:

- $\phi \wedge \psi \leftrightarrow \neg (\neg \phi \vee \neg \psi)$
- $\phi \vee \psi \leftrightarrow \neg (\neg \phi \wedge \neg \psi)$

This means that every instance of $\phi \wedge \psi$ can be replaced by $\neg (\neg \phi \wedge \neg \psi)$, and similarly for negation.

::: exercise
Give the truth table for each one of the two tautologies.
:::

## Decomposition of implication

Implication can be decomposed into negation and disjunction:

- $\phi \rightarrow \psi \leftrightarrow \neg \phi \vee \psi$

::: exercise
Rewrite each  one of the following formulae using only $\neg$ and $\wedge$ (yes, logical and, not logical or):


- $p \rightarrow q$
- $(p \vee (q \rightarrow \neg p))$
- $p \rightarrow (q \rightarrow r)$

:::

## Implication chains as conjunction

Some implicational chains can be converted to a single implication with $\wedge$ in the antecedent.

- $\phi \rightarrow (\psi \rightarrow \rho) \leftrightarrow \phi \wedge \psi \rightarrow \rho$

Bracketing is crucial.
It is not the case that $(\phi \rightarrow \psi) \rightarrow \rho$ is equivalent to $\phi \wedge \psi \rightarrow \rho$.

::: exercise
Give truth tables for the two formulas below to show that only the first is a tautology.

- $\phi \rightarrow (\psi \rightarrow \rho) \leftrightarrow \phi \wedge \psi \rightarrow \rho$
- $(\phi \rightarrow \psi) \rightarrow \rho \leftrightarrow \phi \wedge \psi \rightarrow \rho$
:::

## Distributivity of $\wedge$ and $\vee$

The operators $\wedge$ and $\vee$ distribute over each other

- $\phi \wedge (\psi \vee \rho) \leftrightarrow (\phi \wedge \psi) \vee (\phi \wedge \rho)$
- $\phi \vee (\psi \wedge \rho) \leftrightarrow (\phi \vee \psi) \wedge (\phi \vee \rho)$

::: exercise
Show via truth tables that both formulae are indeed tautologies.
:::

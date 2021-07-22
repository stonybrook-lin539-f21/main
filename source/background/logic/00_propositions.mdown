# Propositions 

## Intuition

A proposition is a statement that is either true or false.
This does not mean that one can necessarily tell whether a proposition is true, nor that the proposition makes any sense considering what our world is like.
It just means that the statement is such that it can have a truth value.

::: example
All of the following are propositions, even though whether they're true or false can depend greatly on context:


- Nobody likes ponies.
- He always snores like a pig.
- $2 + 2 = 4$
- We might see another stock market crash soon.
- A language is regular iff it is recognized by a finite-state automaton.

:::

::: example
The following are not propositions.


- Are you mad?
- Please open a window.
- Hell, yeah!
- A cute kitten
- John and Mary

:::

::: example
Some cases are borderline and require some more detailed analysis.
Take *Either John leaves or I will*.
As a literal description of how the world is, this can be either true or false, so it's a proposition.
But we can also interpret it as a command that the addressee must choose between John and the speaker.
Commands have no truth value and thus aren't propositions.
:::

::: exercise
For each one of the following, say whether it is a proposition.
If you say no, justify your answer.


- John and Peter met yesterday.
- The DeLorean DMC-12 is a sports car originally manufactured by John DeLorean's DeLorean Motor Company.
- Who would say no to that.
- That son of a gun has fooled us all.
- Colorless green ideas sleep furiously.
- John and Mary have only one child, who has three siblings.

:::

## Entailment

Some propositions are atomic in the sense that one cannot break them down into smaller propositions, whereas others are clearly built up from smaller propositions.

::: example
The sentence *John rode a bike and Mary her dragon* might be true or false, so it's a proposition.
But it is not an atomic proposition because it's built up from two smaller propositions.
One is *John rode a bike*, the other one *Mary rode her dragon* (that English allows for the verb to be omitted in the second conjunct is irrelevant for this point).
:::

As a result, propositions can be related to each other so that the truth value of one follows immediately from the other.
This is called **entailment**.

::: example
If *John rode a bike and Mary her dragon* is true, then it must also be true that John rode a bike, and it must be true that Mary rode her dragon.
In the other direction, if *John rode a bike* is false, then so is *John rode a bike and Mary her dragon*.
:::

Entailment can also hold between propositions that do not stand in an obvious part-whole relation to each other.

::: example
Consider the sentences *If pigs can fly, then Sokrates is a chain-smoking dragon* and *No human is a dragon*.
Assuming that both are true, the sentence *Sokrates is human* entails that pigs cannot fly.
:::

The entailments in these two examples are slightly different.
For the first, it suffices to recognize how one proposition was built up from smaller ones.
The second one presents a more complex reasoning pattern that hinges on the meaning of the quantifier *no*.
Logic was devised as a means to study these different kinds of entailments, but over the centuries it has evolved to a highly flexible system that can be used for all kinds of purposes.

::: exercise
For each one of the following pairs of sentences, say whether entailment holds, and if so, in which direction.
If entailment does not hold, explain why.


- 
John likes his son's sisters. |
John likes his daughters.

- 
I am 30 years old. |
My age is a multiple of 15.

- 
1 is not a prime number. |
No prime numbers is less than 2.

- 
John and Bill both left the party early. |
Bill left the party around 9.

- 
The 45th US president isn't universally beloved. |
Donald Trump isn't universally beloved.

- 
If $2 + 2 = 4$, then $2 + 2 = 4$. |
$2 + 2 = 4$


:::

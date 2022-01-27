# Common abbreviations

## w.l.o.g. - without loss of generality

This abbreviation is often used in proofs.
It means that we assume a specific property or condition that does not affect the validity of the proof.
Here is an example:

::: theorem
If somebody is holding three marbles in their hands, then at least one hand is holding at least two marbles.
:::

::: proof
Assume w.l.o.g. that the right hand is holding strictly less than two marbles.
So it is holding either no marbles or exactly one marble.
Either way the left hand is holding at least two marbles.
:::

The use of *w.l.o.g.* here modifies the restriction to the *right* hand.
This restriction is made so that one does not have to speak of *one hand* and *the other hand*, which makes the proof slightly more readable.
But obviously the proof would work just as well if we had assumed that it is the left hand that holds less than two marbles, not the right one.

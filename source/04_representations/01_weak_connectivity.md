# Failed attempts at restricting the class of hierarchies

We have encountered a variety of hierarchies in the previous unit.
They're shown below to jog your memory.

~~~ {.include-tikz size=mid}
123.tikz
~~~
~~~ {.include-tikz size=mid}
adjectival_gradation.tikz
~~~
~~~ {.include-tikz size=mid}
blake_partialorder.tikz
~~~
~~~ {.include-tikz size=mid}
pcc_hierarchy_right_reduced.tikz
~~~

They are all weak partial orders, and some of them are linear orders.
But weak partial orders can take a lot more general shapes than what we see above.

::: example
Consider the **identity function** $\mathrm{id}$, which connects every node to itself and nothing else. 
We can view this function as a relation that connects each node to itself and nothing else.
This is a weak partial order.
It clearly satisfies reflexivity.
Transitivity holds because $a \mathrel{R} b$ and $b \mathrel{R} c$ hold only if $a = b = c$, wherefore $a \mathrel{R} c$ is the same as $a \mathrel{R} a$, which is guaranteed by reflexivity.
Antisymmetry holds for the same rason: $a \mathrel{R} b$ holds only if $a = b$, so it is trivially true that $a \mathrel{R} b$ and $b \mathrel{R} a$ implies $a = b$.
:::

The four hierarchies above hence are all weak partial orders, but the opposite does not hold.
Not every weak partial order is a possible linguistic hierarchy.
Our task, then, is to identify a proper subclass of weak partial orders that more narrowly circumscribes the class of possible hierarchies.

## A first attempt: Lattices

The top three structures above are lattices, but the fourth structure for the PCC is not.
Remember, a partially ordered set $S$ is a lattice iff it is both a meet semilattice and a join semilattice.
In other words, for all $x, y \in S$ it holds that there is a greatest lower bound $x \wedge y$ and a least upper bound $x \vee y$.

::: exercise
Compute each one of the following for the corresponding hierarchy above (assume for each figure that if a node $x$ has a connection to some higher node $y$, this represents $x \leq y$, not $y \leq x$).


- $1 \wedge 2$
- $2 \vee (1 \wedge 3)$
- $\text{positive} \wedge \text{comparative} \wedge \text{superlative}$
- $\text{Nom} \wedge (\text{Gen} \vee \text{Acc})$

:::

::: exercise
The PCC structure is neither a join semilattice nor a meet semilattice.
Explain why.

*Hint*: Find two elements that have no unique supremum or no unique infimum.
:::

::: exercise
Remember that we removed all elements from the PCC lattice where the first and second component are the same person.
If we put these nodes back into the structure, would the result be a lattice?
:::

With the exception of the PCC, the class of lattices seems to be a good fit.
It even provides a good characterization for phenomena we haven't considered at all yet.

For example, there is a phenomenon that is very similar to the PCC that is known as the **Gender Case Constraint** (GCC).
Like the PCC, the GCC forbids certain combinations of pronouns in the same clause.
Unlike the PCC, the relevant pronouns are subject and objects rather than direct and indirect object.
More importantly, the GCC limits these combinations based on gender instead of person.
So far the GCC is only attested for Zapotec, a Mesoamerican language spoken in Mexico that has four distinct genders.
The following combinations are allowed:

$\downarrow$S/O$\rightarrow$ | 1 | 2 | 3 | 4 |
--: | :-: | :-: | :-: | :-: |
1   | -   | Y   | Y   | Y   |
2   | N   | -   | Y   | Y   |
3   | N   | N   | -   | Y   |
4   | N   | N   | N   | -   |

This looks very similar to the U-PCC, generalized from 3 values to 4.
So it isn't too surprising that the GCC is a monotonic map given a gender hierarchy that, once again, forms a lattice.

~~~ {.include-tikz size=mid}
gcc_hierarchy.tikz
~~~

::: exercise
Show that the Zapotec GCC is monotonic over this hierarchy.
:::

So it looks like we might be able narrow down the class of potential hierarchies from any weak partial order to lattices --- if we can deal with the PCC hierarchy somehow.
That would be a significant reduction.
Unfortunately, the PCC isn't the only exception.
The class of lattices simply is too restrictive.

## Lattices are too specific: Evidence from tense

Some hierarchies do not form lattices.
One case where one can see this is with verbal tense.
Consider the English tense paradigm \emph{go}-\emph{went}-\emph{gone}.
This looks like an ABA pattern.
But suppose that we use the order $\text{past} < \text{participle} < \text{present}$.
This is intuitively plausible since past events occur before present events, whereas the participle is usually used for the simple perfect, which describes events that aren't quite as distant as those described by simple past.
With this ordering, \emph{go}-\emph{went}-\emph{gone} is actually \emph{went}-\emph{gone}-\emph{go}.
The $^*$ABA-violation has disappeared.
And given this ordering of verbal forms, no ABA violations are attested at all.

If this were the end of it, then we would have a linear order for tense, and since linear orders are lattices, we could still stick with lattices as a reasonable model of linguistic hierarchies.
But as you all know, verbs can have more temporal forms than just those three, and one of them is the future tense.
Once one considers future, things become more complicated.

1. Future can be syncretic with past and participle to the exclusion of present. 
   An example is Serbo-Croatian *hteo sam* (past), *hteo* (participle), *hoću* (present), *hteću* (future).
   This pattern is AABA.

1. Present and future can be syncretic to the exclusion of past and participle.
   An example is the ABCC pattern *xward*, *xoria*, *xweid*, *xweid* in Kurdish.

1. Present, participle, and past can be syncretic to the exclusion of future.
   This is the case for French, where the present, past and participle of *aller* 'go' all use them stem *all-*, whereas the future is built with the stem *ir-*.

The Serbo-Croatian data suggests an ordering
$\text{past} < \text{participle} < \text{future} < \text{present}$,
whereas the French pattern requires
$\text{past} < \text{participle} < \text{present} < \text{future}$.
The Kurdish data is compatible with both.
Each one of the two hierarchies is a lattice, but we need a hierarchy that can accommodate all those tense patterns at once.
No linear order can do this.
Instead, we need a partial order.

~~~ {.include-tikz size=mid}
tense_hierarchy.forest
~~~

::: exercise
For each one of the three data paradigms above, show that it is monotonic over this tense hierarchy.
:::

This is not a lattice as neither of the following meets exists:

- $\text{future} \wedge \text{participle}$,
- $\text{future} \wedge \text{past}$ exist.

Instead, it is a (join) semilattice.
Remember that semilattices also played a major role for the Adjunct Island Constraint.
So perhaps all linguistic hierarchies that aren't lattices are at least semilattices.
That would be nifty.
But the PCC hierarchy isn't a semilattice, either, and once again this isn't the only problematic case.

::: exercise
Why can't we generalize the tense semilattice to a lattice by also setting $\text{past} < \text{future}$?
:::


## Semilattices (and weak partial orders) are too specific

The counterexample to semilattices comes from case.
However, this time it isn't about case syncretism but noun stem allomorphy.
Noun stem allomorphy refers to the fact that case may not only be reflected in the choice of suffix, but also in the form of the stem.
This is shown below for Latin *rex*, which means *king*.

| Case | Singular | Plural   | 
| --:  | :--      | :--      | 
| Nom  | rex      | reg-es   | 
| Gen  | reg-is   | reg-um   | 
| Dat  | reg-i    | reg-ibus | 
| Acc  | reg-em   | reg-es   | 
| Abl  | reg-e    | reg-ibus | 

As you can see, nominative singular uses the special form *rex* without a dedicated case suffix, whereas all other cases are built with the stem *reg* instead.
Curiously, there seems to be only two options for noun stem allomorphy across languages.
Either all cases use the same stem, or only nominative gets to use a different stem.
So in a system with nominative, accusative, genitive, and dative, the only possible stem patterns are AAAA and ABBB.
This is monotonic over the case hierarchy, repeated here for your convenience.

~~~ {.include-tikz size=mid}
blake_partialorder.tikz
~~~

But the case hierarchy allows for many other monotonic maps, none of which seem to occur with noun stem allomorphy.
Rather than stipulating them away, one would prefer a mechanism that modifies the hierarchy for case and thereby yields a suitable hierarchy for noun stem allomorphy.
The only possible solution that limits the set of monotonic maps is the following:

~~~ {.include-tikz size=mid}
stem_allomorphy.tikz
~~~

This figure looks quite a bit different from what we have encountered so far.
An arrow from $x$ to $y$ represents $x \leq y$.
Arrows that can be inferred via transitivity are omitted.
So $\text{Acc} < \text{Dat}$ even though there is no arrow that directly connects the two.
Note how this hierarchy essentially creates a cycle from accusative to genitive, dative, other cases, and back to accusative.

::: exercise
A monotonic mapping must map all cases in the Acc-Gen-Dat-Others-Acc cycle to the same value.
Explain why.
:::

The hierarchy above allows for the two attested noun stem allmorphy patterns, and nothing else.
So it provides a very tight characterization of this phenomeon.
But the hierarchy is not a semilattice, let alone a lattice.
In fact, it isn't even a weak partial order, so it can't be a semilattice, either, as this is a special kind of partially ordered set.

In order to be a weak partial order, $\leq$ as defined by the figure must be reflexive, transitive, and antisymmetric.
We usually take reflexivity for granted.
But note that in this case, it is also implied by transitivity for most cases.
For instance, $\text{Acc} \leq \text{Gen} \leq \text{Dat} \leq \text{Others} \leq \text{Acc}$, so $\text{Acc} \leq \text{Acc}$ by transitivity.
But this example also shows that antisymmetry does not hold: both $\text{Acc} \leq \text{Gen}$ and $\text{Gen} \leq \text{Acc}$ hold, yet accusative and genitive are distinct elements of the hierarchy.
This shows that $\leq$ is reflexive and transitive, but not antisymmetric.
Consequently, $\leq$ isn't a weak partial order.
Instead, it is a **preorder** (also called a **quasi-order**).

Our quest to find a more restrictive characterization for linguistic hierarchies has turned pretty dire all of a sudden.
If some hierarchies aren't even weak partial orders, then they cannot be semilattices or lattices either.
Remember, semilattices and lattices are special cases of partially ordered sets, i.e. sets with a weak partial order defined over them.
The class of preorders is even bigger than the class of weak partial orders.
Despite our best intentions, things have become less restrictive.
Do not despair, though.
The next unit shows a way of out of this malaise.
It requires a shift in perspective, though, as it relies on graphs instead of orders.

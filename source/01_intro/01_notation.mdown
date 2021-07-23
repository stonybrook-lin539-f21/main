# Reading mathematics

While these materials are designed to be as approachable as possible, a certain mathematical style of writing will be indispensable.
This includes special notation, some math-specific jargon, and even a particular way of interpreting English sentences.
Mathematicians do not do this to sound smarter than they are or to isolate themselves from the uninformed layman, but because it makes it easier for them to communicate their ideas.
This is no different from any other field of research --- a specialized field of study requires a specialized means of communication.
It will take you a while to get used to this way of talking and writing, but here are a few tips to make sure you don't throw in the towel too early.

## Dealing with symbol shock

The most salient aspect of mathematical communication is the heavy reliance on special symbols.
This starts with formulas like $f(x) = kx + d$ and quickly develops into complex statements such as the following:

1.  Let $\mathcal{L}$ be a totally ordered collection of languages $L_1, \ldots, L_n$ ($n \geq 1$) such that for all $1 \leq i,j \leq n$ we have $L_j \not\subseteq L_i$ iff $i < j$.

1.  For any given string $s$ and PCFG $G$, the probability of $s$ is $\sum_{d \in D_G(s)} \prod_{r \in d} p_G(r)$ where $D_G(s)$ is the set of derivation trees of $G$ that yield $s$, $r$ is a tree bigram of a derivation tree, and $p_G(r)$ is the probability of $r$ according to $G$.

1.  A *$k$-interval*, or simply *$k$-val*, is a $5$-tuple $\tuple{k,G_l, G_r, G_o, G_f}$ such that $k \geq 1$ and each $G$ is an SL-$1$ grammar that specifies, respectively, the left edge, right edge, open slots, and the fillers.
    The corresponding *$k$-val formula* (with free variables $x_1$, $\ldots$, $x_k$) is 
    \begin{multline*}
        \exists l,r
        \bigg [
            \bigwedge_{g \in G_l} \neg g(l)
            \wedge
            \bigwedge_{g \in G_r} \neg g(r)
            \wedge
            \bigwedge_{1 \leq i \leq k} 
            \bigwedge_{g \in G_o} \neg g(x_i)
            \wedge
            l \prec x_1
            \wedge
            x_k \prec r
            \wedge
            \\
            \forall z
            \Big [
                \big (
                    (l \prec z \wedge z \prec x_1)
                    \vee
                    (x_k \prec z \wedge z \prec r)
                    \vee
                    \bigvee_{1 \leq i < k}
                    (x_i \prec z \wedge z \prec x_{i+1})
                \big )
                \rightarrow
                \bigwedge_{g \in G_f} \neg g(z)
            \Big ]
        \bigg ]
    \end{multline*}
    For any empty $G$, $\bigwedge_{g \in G} \neg g(x)$ is always satisfied.

Unless you've had previous mathematical training, these passages probably made your eyes glaze over and your brain freeze in horror:
"What is this stuff?
What's $i$ again, why is there a big sigma, and what is the subscript there?
Why can't they just say what they want in plain English?
I can't understand this, it's hopeless, I'm just not made for math."
Don't despair, you've just experienced *symbol shock*.

Symbol shock refers to the phenomenon that just looking at a page of math can be so disheartening that you can't think clearly.
It's like being at the base of Mount Everest, looking up, and feeling that you'll never be able to reach the top.
So rather than trying you give up immediately, or you overcompensate and rush forward in a frenzy without paying attention to what you're doing.
Neither approach will get you to the goal.
In order to deal with symbol shock, you have to develop the central survival skills of mathematics: take your time, and keep a cool head.

You cannot read math like a novel or even your average textbook.
An 8 page paper can easily keep you busy for days before you fully understand it.
Revolutionary proofs may only span a few pages yet take trained mathematicians months to understand.
Math takes time, so do not rush.
As soon as you internalize this simple rule, symbol shock will be much less of a problem.
When a new symbol is introduced, pause and commit it to memory.
When you see a complex formula, work through it symbol by symbol until you understand what's going on here.
Just. Take. Your. Time.

This is actually why I think that math is easier to learn by reading than by listening.
With a text, you can reread every sentence until you get it.
You can go back 3 pages to revisit a point you thought was clear to you but now seems to be at odds with what you're reading.
You can't do that in a lecture.
But you actually have to do all those things, you have to slow down, go back, reread.
Math isn't all that hard, but you have to be very disciplined about it.

With time, you will get much better at reading math and it will take you much less effort, but for the beginning I suggest that you do the following to better deal with symbol shock:

- Assign colors to specific symbols and types of objects.
  In my personal experience, I can tell pretty easily how well I understand a paper based on how I would color its math.
  At first, it's all just black, but as I get a deeper understanding of the objects and how they hang together I construct an internal coloring system for myself.
  So grammars are blue, automata green, certain variables that keep reoccurring are purple and teal, and so on.
  If you print the pdf versions of the units, you can literally add colors to all the symbols, and that way the logic of the pages will reveal itself more clearly to you.

- Think about **why** certain symbols were chosen.
  Mathematicians care a great deal about good notation, and it really shows.
  A math paper with a well-designed notation is a pleasure to read.
  There's certain established conventions.
  For instance, indices are usually chosen to be $i, j, k$, variables are $x, y, z$, and functions are $f, g, h$.
  But that's just a rule of thumb.
  A labeling function may be $\ell$, which looks like an $l$ but is slightly different so that $l$ can be used to refer to labels instead.
  Never try to memorize notation in a brute-force manner, try to understand the design principles behind it.
  If you know why the notation looks the way it does, you'll have a much easier time remembering even minor details and nuances.

- Set yourself realistic goals.
  Don't attempt to read 20 pages in one sitting.
  Instead, plan for 3 or 4 reading sessions of 5 pages each.
  And go in with the expectation that you will have to read some passages multiple times, and that you'll have to go back a few pages to look up some symbol or definition.

- Don't give up.
  None of the things we cover are some super-advanced hardcore math problems that will make your head explode unless you have an IQ of 150.
  What we are doing is the math-equivalent of running a 5k: most college students aren't fit enough yet to do it, but they can reach that level with a few months of training.
  It requires tenacity and discipline, though.


## Dealing with some other stumbling blocks

### No implicatures

Mathematical writing is also peculiar because, as we linguists like to say, implicatures are often cancelled implicitly.
That's a smarty pants way of saying that only the literal meaning is the intended one.
So the phrase "Let $S$ be a set containing two odd numbers" does not entail that $S$ only contains two odd numbers.
It could contain all kinds of additional things, including other odd numbers, but at the very least it contains two odd numbers.
If we wanted the set to contain two odd numbers and nothing else, we would have written "Let $S$ be a set containing exactly two odd numbers, and nothing else".
Tricky, hmm?
For the uninitiated reader, it is easy to miss something important by assuming that the statement is more specific than it actually is.

Another common pitfall arises with statements like "Every blue dragon is a chain smoker".
Is this claim true or false?
A linguist will tell you that it is neither, and instead contains a presupposition violation (yes, linguists like their fancy terms) because the sentence assumes that blue dragons exist, which they obviously do not.
A mathematician doesn't care for such linguistic subtleties and instead considers the statement true because there exists no blue dragon that isn't a chain smoker.
That is perfectly fine for mathematics, but it's very different from how a layperson would interpret the sentence.
Again, when dealing with math you shouldn't assume anything that isn't stated explicitly.

Quite generally, you should try to identify minimal examples:
when you see a statement or definition, always think about the simplest object that satisfies it, and ask yourself how much this object can change before it no longer fits the description.

### Questioning definitions

Speaking of definitions, you should always ask yourself why something is defined the way it is.
I don't mean this in some kind of existentialist way like "What does it mean to be red?", but a utilitarian one: considering that we could have defined something in a million slightly different ways, what might be the reason that makes this the most useful, elegant or productive definition?
Remember, definitions can't be true or false, they can only be useful or useless.
So what is it that makes a given definition useful?
In exploring this question, you will get a much better understanding of what the definition even defines, and that is key to studying the kind of object that is being defined.

### Making definitions concrete

Another helpful strategy in dealing with definitions is to come up with two distinct lists: examples that fit the definition, and examples that do not fit the definition.
Both are equally important.
Sometimes a definition may be so abstract and general that it is hard to see what would not fit the definition.
In seeking out those examples, you gain a much better idea of the defined class of objects.

To give just one example, an *algebra* is a set $S$ with a function $+$ that takes elements of $S$ as input and produces elements of $S$ as its output.
We also say that $S$ is *closed under $+$*.
That is a very general definition, and one can immediately think of tons of algebras:

- the natural numbers with addition
- the integers with subtraction
- the real numbers with base 2 logarithm
- the set of all possible strings with concatenation

But what is an example of something that is not an algebra?
Well, the natural numbers with division, for instance.
The natural numbers are 0, 1, 2, 3, and so on, but $\frac{5}{2} = 2.5$, which is not a natural number.
This shows that division can take two natural numbers as input and return something that is not a natural number.
Hence the natural numbers with division is not an algebra.
The real numbers with division, however, would be.

If all those examples got you confused because you don't quite remember the difference between natural numbers and integers, or what exactly a logarithm is, don't worry.
For most of this class, we actually won't be using the things you heard about in high school and have forgotten since then.
Where we do need them, they're slowly introduced like any other new concept.
So don't worry about this and focus on the important insight here: whenever you see an abstract definition, think about what kind of more concrete objects (do not) fit the definition.

### Implication and equivalence are not the same

English, as all natural languages, is pretty sloppy in how it expresses conditions.
Consider the following lovely sentence: "If you don't give me your money, I will shoot you".
Now the common understanding is that if you do hand over your money, you will not be shot.
But if your robber happens to be a mathematician you are very unlucky because they might still shoot you --- while you draw your final breath they will gleefully point out that they didn't say "If you don't give me your money, I will shoot you, and if you give me your money I will not shoot you."
Your murderer took advantage of the fact that we often express a biconditional ($a$ implies $b$, and the other way round) with the same language we use for implications ($a$ implies $b$, but $b$ does not necessarily imply $a$).
In mathematics, this distinction is very important.
So pay close attention to whether the text uses an *if* or an *iff* (which is short for *if and only if*).
The former is an implication, the latter a biconditional.

::: example
The following is an implication but not an equivalence/biconditional: "If you are an actress, then you are female".
After all, not every female is an actress.
On the other hand, "You are a bachelor iff you are an unmarried man" is a biconditional.
Every unmarried man is a bachelor, and every bachelor (in the non-academic sense) is an unmarried man.
:::

## Recap

- Avoid symbol shock!
    - don't rush, take your time
    - break readings into chunks
    - add colors
    - try to understand the notation
- Definitions
    - read them carefully
    - think about what (does not) fit the definition
    - think about why this particular definition was chosen, rather than some alternative
- Writing style
    - Don't assume implicatures.
      Read in a very literal fashion.
    - Don't confuse implications (*if*) and biconditionals (*iff*).

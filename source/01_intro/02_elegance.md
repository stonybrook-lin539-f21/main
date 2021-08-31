# Mathematical elegance

Mathematics is a very elegant enterprise, but it takes some expertise to appreciate that elegance.
Just like a glass of premium whiskey, mathematics may be overwhelming and downright unpleasant to the uninitiated.
This is particularly true for one trait of mathematics: minimalism.
Mathematicians do not like to introduce completely new primitives, instead everything is built from a minimal set of building blocks.

For a concrete example of a system that would not please mathematicians, consider the Roman number system.
It starts out very promising, as 1 is I, 2 is II, and 3 III.
This would allow us to give a nice, compact definition of the possible numbers.

::: definition
The recursive Roman number system (RR) is defined as follows:

- I is a number.
- If $x$ is a number, then so is $x$I.

:::

The definition tells us that all of the following are numbers in the RR-system: I, II, III, IIII, and all other sequences of the letter I, e.g. IIIIIIIIIIIIIIIIII.
So the number 4 would be represented as IIII, 7 as IIIIIII, and so on.
Of course that would make it very cumbersome to write down a number like 217, and there would be no practical way to write down a number like 5 trillion trillion. 

But as you probably know, this is not how the Roman number system actually works. 
After III we get IV, not IIII.
The number 5 is V, not IIIII.
And
10 is X,
50 is L,
100 is C,
500 is D,
and
1000 is M.
These symbols are combined in complex ways to represent specific numbers.
For instance, we have XLVI for 46, MMCDXXXVIII for 2438, and MCMXCIX for 1999.

Many non-mathematicians like the idea of giving numbers like 5, 10, 50, and 100 special symbols because they feel more important and relevant to us.
For some reason they are intuitively more pleasing than 23 or 77.
They also turn up more often in daily life --- just think of the values on dollar bills.
So it is more convenient to use, say, V instead of IIIII.
And while we still cannot write 5 trillion trillion in an easy way, at least 217 is now simply CCXVII.
Therefore the average person who just wants to easily work with numbers that are relatively small but still larger than 10 may prefer the standard Roman system rather than our RR concoction.

A mathematician, however, is not interested in a system that is easy to use for daily work.
Mathematicians want a system that is easy to reason about.
The Roman system is pretty obtuse in that respect.
We no longer have I as our only primitive building block, instead there are also V, X, L, C, D, and M.
And the way these numbers can be combined is much more complicated.
Whereas the RR-system allows any arbitrary combination of Is, the Roman system has a more complicated combinatorial system.
For example, CLL is not a well-formed Roman number, nor are CMC and IVX.
Go ahead, do some research, then try to write down the combinatorial rules of the Roman number system --- you will need a much more elaborate definition.

But obviously both systems can represent exactly the same numbers.
There is no magical number that can be represented in the standard Roman system not in the RR-system.
This is why a mathematician would prefer the simpler RR-system.
It makes it much easier to prove essential results. 
Once the RR-system is better understood, one extends the results to the Roman number system by defining a mechanism for converting from one number system to the other.

The example above is slightly silly because mathematicians have more abstract ways of talking about numbers, ways where it no longer matters how numbers are actually written.
But the general principle is very close to mathematical practice and will be with us for the entirety of this course:

::: advice
- Study simple systems.
- Reduce complex systems to simple systems.
:::

::: example
Suppose we are studying the set $\mathbb{Z}$ of **integers**, which contains $0$, $1$, $-1$, $2$, $-2$, and so on.
We want to know what kind of mathematical system we get if we allow addition and subtraction of integers.
What are the properties of this system?
Well, the first thing we can say is that subtraction is a redundant operation because $m - n = m + (-n)$.
For instance, $5 - 3 = 2 = 5 + (-3)$.
So instead of $\mathbb{Z}$ with $+$ and $-$, we can focus on the simpler system $\mathbb{Z}$ with $+$ only.
That will make our life quite a bit easier because there's only one operation to worry about instead of two.
:::

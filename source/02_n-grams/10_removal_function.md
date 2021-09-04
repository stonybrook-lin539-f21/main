**Prerequisites**

- functions (domain terminology)

# Stop word removal as a function

This unit illustrates how one might define stop word removal as a mathematical function $\mathit{del}$ (read *delete*).

First, we fix some alphabet $\Sigma$ and let $S$ be some finite set of symbols drawn from $\Sigma$.
For every such $S$, we define a deletion function $\mathit{del}_S$ that maps strings over $\Sigma$ to strings over $\Sigma - S$.
In mathematical notation, $\mathit{del}_S: \Sigma^* \rightarrow (\Sigma - S)^*$.

This only tells us the domain and co-domain of $\mathit{del}_S$, but not how exactly inputs and outputs are connected to each other.
For any string of the form $u_1 \cdots u_n$ (where $n \geq 0$ and each $u_i$ is a symbol drawn from $\Sigma$), we define
$$
\mathit{del}_S(u_1 \cdots u_n)
    \is
    \begin{cases}
    \emptystring & \text{if } u_1 \cdots u_n = \emptystring\\
    \mathit{del}_S(u_2 \cdots u_n) & \text{if } u_1 \in S\\
    u_1 \stringcat \mathit{del}_S(u_2 \cdots u_n) & \text{otherwise}\\
    \end{cases}
$$

::: example
Suppose $\Sigma \is \setof{a,b}$ and $S \is \setof{a}$.
Let $s \is \mathit{abba}$.
Then $\mathit{del}_S(s)$ should yield $\mathit{bb}$.
To this end, we compute $\mathit{del}_S(s)$ in a stepwise fashion:

\begin{align*}
\mathit{del}_S(s)
&=
\mathit{del}_S(\mathit{abba})
\\
&=
\mathit{del}_S(\mathit{bba})
\\
&=
b \stringcat \mathit{del}_S(ba)
\\
&=
b \stringcat b \stringcat \mathit{del}_S(a)
\\
&=
b \stringcat b \stringcat \mathit{del}_S(\emptystring)
\\
&=
b \stringcat b \stringcat \emptystring
\\
&=
b \stringcat b
\\
&=
\mathit{bb}
\end{align*}

So $\mathit{del}_S(\mathit{abba}) = \mathit{bb}$, as expected.
:::

As you can see, $\mathit{del}_S$ is partially defined in terms of itself:
the value of $\mathit{del}_S(\mathit{abba})$ is inferred from the value of $\mathit{del}_S(\mathit{bba})$.
This is called a **recursive** definition.
We can visualize the computation of this recursive function as below:

~~~ {.include-tikz size=mid}
recursive_function.forest
~~~

Every recursive function has one or more **base cases** and a **recursion step**.
The base cases are those where the value of the function can be determined without recursion.
For $\mathit{del}$, there is only the base case $\mathit{del}_S(\emptystring) = \emptystring$.
Notice how in the graph above $\mathit{del}_S(\emptystring)$ does not contain any further instances of $\mathit{del}_S$.
Instead, we immediately get $\emptystring$ as the output.
The recursion step defines the function in terms of the function itself.
In the graph above, that's every instance of $\mathit{del}_S$ which has another instance of $\mathit{del}_S$ below it.

::: exercise
Here is another recursively defined function.

$$
f(x,y) \is
    \begin{cases}
        x & \text{if } y \leq 1\\
        x + f(x,y-1) & \text{otherwise}\\
    \end{cases}
$$

What does this function do?
Is there a commonly used name for it?
:::

::: exercise
This continues the previous exercise.
Draw a diagram like the one above for $f(5,4)$.
:::

::: exercise
Give a recursive definition of a function that takes two arguments: a string $u \is u_1 \cdots u_n$ over alphabet $\Sigma$, and a set $S$ of symbols drawn from $\Sigma$.
The function returns $1$ if at least one member of $S$ occurs in $u$, and $0$ otherwise.
:::

::: exercise
This continues the previous exercise.
Draw a diagram like the one above for $f(\mathit{aaba}, \setof{b})$ and $f(\mathit{aaba}, \setof{c,d,e})$.
:::

# Connectedness of graphs

Graphs can have varying degrees of connectivity.
Connectedness measures the degree to which every node in the graph is reachable from some other graph.

A **disconnected** graph is one where there are nodes $a$ and $b$ such that even if one ignores the direction of the edge relation, one cannot get from $a$ to $b$.
So if we were to construct the graph in the real world as a kind of mobile, we would not be able to hang the graph on the wall with a single hook because not all parts hang together --- at least one part would fall to the ground.

A **weakly connected** graph is such that it forms one cohesive whole via the edge relation, but there might be nodes $u$ and $v$ such that neither one can be reached from the other unless one ignores the direction of edges.
A **connected graph** satisfies the strong property that for all nodes $u$ and $v$, $u$ is reachable from $v$ or the other way round.
A **strongly connected** graph, finally, is such that every node is reachable from every node.

::: definition
A directed graph is

- *weakly connected* iff the reflexive, symmetric, transitive closure of its edge relation is total,
- *connected* iff the reflexive, transitive closure of its edge relation is total,
- *strongly connected* iff the reflexive, transitive closure of its edge relation is identical to $V \times V$,
- *disconnected* iff it is not weakly connected.

:::

::: example
The undirected graph we saw at the beginning of the previous unit is disconnected, and the same goes for any directed version of it.
For example, there is no edge between $1$ and $3$, one simply cannot be reached from the other.

~~~ {.include-tikz size=big}
modulo3_undirected_notransitive.tikz
~~~

However, we can identify parts of the graph that are connected.

~~~ {.include-tikz size=small}
modulo3_undirected_component.tikz
~~~

Even though there is no edge between $0$ and $6$, the transitive closure of the edge relation does connect the two.

Now let us look at a directed graph, where multiple degrees of connectedness need to be distinguished.

~~~ {.include-tikz size=small}
modulo3_directed_strong.tikz
~~~

The directed graph above is strongly connected.
When we take the reflexive, transitive closure of the edge relation, every node is reachable from every node.
This is exactly what it means to be strongly connected.

But a slight change in the edge relation suffices to reduce strong connectedness to connectedness.

~~~ {.include-tikz size=small}
modulo3_directed_connected.tikz
~~~

Even if we look at the reflexive, transitive closure of the edge relation, there is no path from $3$ to $0$, from $6$ to $0$, or from $9$ to $0$.
So we can no longer reach every node from every node.
But for any two nodes $a$ and $b$, it still holds that $a$ can be reached from $b$ or $b$ can be reached from $a$.
Hence the reflexive, transitive closure of the edge relation is still total, and we have a connected graph.

Finally, consider what happens if we remove one edge from the graph above.

~~~ {.include-tikz size=small}
modulo3_directed_weak.tikz
~~~

Now even the reflexive, transitive closure of the edge relation does not connect $6$ and $9$, so the graph cannot be connected.
However, $6$ and $9$ are still reachable from each other if we consider the reflexive, symmetric, transitive closure of the edge relation.
Therefore, the graph is weakly connected.
:::

Intuitively, the three degrees of connectivity can be described in terms of how we have to move along the arrows in a graph to read one node from another one:

- If we can reach every node from every node by following a sequence of arrows, the graph is strongly connected.
- If we can reach $a$ from $b$ by following a sequence of arrows, but not necessarily $b$ from $a$, the graph is connected.
- If we have to sometimes go against the direction of the arrow to get from $a$ to $b$, the graph is weakly connected.

::: exercise
Is every strongly connected graph weakly connected?
Justify your answer.
:::

::: exercise
Suppose that a graph $G$ is weakly connected.
Is is guaranteed to be connected if we take the reflexive, symmetric, transitive closure of the edge relation?
:::

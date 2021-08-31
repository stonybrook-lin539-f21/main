# Functions: Basic notation

**Functions**, also called **maps** or **mappings**, are ubiquitous in mathematics.
The laymen usually thinks of things like $f(x) = x + 1$ when they hear the word *function*, but the concept is much more general.

## Functions convert input arguments to an output

Anything can be thought of as a function as long as it takes a fixed number of **arguments** as its input and converts them to an output.
Crucially, the output is not allowed to vary while the input is kept the same.

::: example
A car wash can be regarded as a function that takes as input a car and returns as its output a clean car (in an ideal world, at least).
A dirty Dodge Viper comes out as a clean Dodge Viper, and a clean Audi A4 still comes out as a clean Audi A4.
The output is always perfectly predictable from the input.
:::

::: example
Suppose $f(x)$ can be randomly chosen between $x+1$ and $2 \mult x$.
This is not a function because one and the same input can produce different outputs.
:::

::: exercise
Let $f$ be a function that takes as its input a number $n$ and returns $n+1$ on a weekday and $n+2$ on the weekend.

- Is $f$ a function?
- What if $f$ instead takes two arguments: a number $n$, and the name of the day of the week.

:::

This special property of functions is known as **right uniqueness**.
Right uniqueness guarantees that functions are deterministic in the sense that one can predict the output from the input with 100% accuracy.

**Caution**: The functions used in programming languages are not necessarily functions in the mathematical sense because their output can vary even if the input stays the same.

::: jupyterpython
import random
import re

# a programming function that is not a mathematical function
def random_output(number):
    # randomly choose between two outputs
    if random.choice([True, False]):
        return 2 * number
    else:
        return 3 * number

# let's see what happens when we run the function multiple times
for _ in range(10):
    print("The output of random_output({}) is {}".format(5, random_output(5)))
:::

<!-- ```python -->
<!-- import random -->
<!-- import re -->
<!-- import ipywidgets -->
<!-- from ipywidgets import Button, Layout -->
<!--  -->
<!-- from IPython.display import display -->
<!--  -->
<!-- # a programming function that is not a mathematical function -->
<!-- def random_output(number): -->
<!--     # randomly choose between two outputs -->
<!--     if random.choice([True, False]): -->
<!--         return 2 * number -->
<!--     else: -->
<!--         return 3 * number -->
<!--  -->
<!-- b = ipywidgets.Button(description='Click to run randomization', -->
<!--            layout=Layout(width='50%', height='80px')) -->
<!-- display(b) -->
<!--  -->
<!-- def on_button_clicked(b): -->
<!--     for _ in range(10): -->
<!--         print("The output of random_output({}) is {}".format(5, random_output(5))) -->
<!--      -->
<!-- b.on_click(on_button_clicked) -->
<!-- ``` -->


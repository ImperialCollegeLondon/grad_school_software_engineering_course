---
title: "Tools II: Code Formatters"
teaching: 3
exercises: 2
questions:
- How to format code with no effort on the part of the coder?
objectives:
- Know how to install and use a code formatter
keypoints:
- Code formatting means how the code is typeset
- It influences how easily the code is read
- It has no impact on how the code runs
- Almost all editors and IDEs have some means to set up an automatic formatter
- 5 minutes to set up the formatter is redeemed across the time of the project i.e. the cost is close to nothing
---

## Why does formatting matter?

* Code is read more often than written
* Setting up a formatter in your editor takes 5 minutes
* Those 5 minutes are redeemed across the lifetime of the project

## Rules to choose a code formatter

1. Choose one
1. Stick with it

We chose [black](https://pypi.org/project/black/) because it has very few
options with which to fiddle.

>## Formatting example
>
> Using Visual Studio Code:
>
> 1. Open the file `messy.py`. Its contents should match:
>
>    ```python
>    x = {  'a':37,'b':42,
>    'c':927}
>    y = 'hello '+       'world'
>    class foo  (     object  ):
>       def f    (self   ):
>           return       y **2
>       def g(self, x,
>           # pylint: disable=missing-docstring
>           y=42
>           ):
>           return x--y
>    def f  (   a ) :
>       return      37+-a[42-a :  y*3]  noqa: E203
>    ```
>
> 1. Ensure that you have activated your "course" conda environment (see
>    [previous episode])
> 1. Make a trivial change to the file and save it: it should be reformatted
>    automagically.
> 1. Use the `undo` function of VS Code to return the code to its unformatted
>    state. Before saving again delete a ':' somewhere. When saving, the code
>    will likely not format. It is syntactically invalid. The formatter cannot
>    make sense of the code and thus can't format it.
>
> >## Solution
> >
> > After saving, the code should be automatically formatted to:
> >
> > ```python
> > x = {"a": 37, "b": 42, "c": 927}
> > y = "hello " + "world"
> >
> >
> > class foo(object):
> >     def f(self):
> >         z = 3
> >         return y ** 2
> >
> >     def g(self, x, y = 42):
> >         # pylint: disable=missing-docstring
> >         return x - -y
> >
> >
> > def f(a):
> >     return 37 + -a[42 - a : y * 3]  # noqa: E203
> >
> > ```
> >
> > Ah! much better!
> >
> > Still, the sharp-eyed user will notice at least one issue with this code.
> > *Formatting code does not make it less buggy!*
> {: .solution}
{: .challenge}

[previous episode]: http://localhost:4000/l1-01-tools-I/index.html#selecting-an-environment-in-visual-studio-code

{% include links.md %}

---
title: "Tools II: Code-Formatters"
teaching: 3
exercises: 2
questions:
- How to format code with no effort on the part of the coder?
objectives:
- Know how to install and use a code formatter
keypoints:
- Code formatting means how the code is type-set
- It influences how easily the code is read
- It has no inpact on how the code runs
- Almost all editors and IDE's have some means to setup an automatic formatter
- 5 minutes to setup the formatter is redeemed across the time of the project
- I.e. the cost is close to nothing
---

# Why formatting matters?

* Code is read more often than written
* Setting up a formatter in your editor takes 5 minutes
* Those 5 minutes are redeemed across the lifetime of the project

# Rules to choose a code-formatter

1. Choose one
1. Stick with it

We chose [black](https://pypi.org/project/black/) because it has very few
options with which to fiddle.

>## Formatting example
>
> Using Visual Studio Code:
> 1. Open options or the file ".vscode/settings.json"
> 1. Set up the black as the "python.formatting.provider"
> 1. Optionally, set up "editor.formatOnSave" and "editor.formatOnType"
> 1. Put the following into a file `myscript.py` and save it.
>    ```python
>    from typing import List
>    import numpy as np
>    RANDOM_KEYVALUES = { np.random.choice(list("abcdefghilnop")) * str(i):
>    np.random.random() for i in np.random.choice(list(range(100)), 10)}
>    def some_function(
>
>    an_argument : int, another_argument: List, an_array: np.ndarray,
>
>    repeat: int = 10
>    ) -> np.ndarray:
>      result = 0
>      for j in range(repeat): result += (an_argument * an_array).sum() * np.cos(another_argument) * j
>      return result
>    ```
>
> 1. Now paste the code again but before saving delete a ':' somewhere. When
>    saving, the code will likely not format. It is syntactically invalid.
>    The code formatter cannot make sense and thus can't format it.
> 
> >## Solution
> >
> > After saving, the code should be automatically formatted to:
> >
> > ```python
> > from typing import List
> > import numpy as np
> >
> > RANDOM_KEYVALUES = {
> >     np.random.choice(list("abcdefghilnop")) * str(i): np.random.random()
> >     for i in np.random.choice(list(range(100)), 10)
> > }
> >
> >
> > def some_function(
> >     an_argument: int, another_argument: List, an_array: np.ndarray, repeat: int = 10
> > ) -> np.ndarray:
> >     result = 0
> >     for j in range(repeat):
> >         result += (an_argument * an_array).sum() * np.cos(another_argument) * j
> >     return result
> > ```
> >
> > Ah! much better!
> >
> > Still, the sharp-eyed numpy user will notice this code does not actually run.
> > Formatting code does not make it less buggy.
> {: .solution}
{: .challenge}

{% include links.md %}

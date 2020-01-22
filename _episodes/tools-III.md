---
title: "Tools III: Linters"
teaching: 10
exercises: 5
questions:
- How to make the editor pro-actively find errors and code-smells
objectives:
- Remember how to install and use a linter in vscode without sweat
keypoints:
- Linting is about discovering errors and code-smells before running the code
- It shortcuts the `edit-run-debug and repeat` workflow
- Almost all editors and IDE's have some means to setup an automatic linters
- 5 minutes to setup a linter is redeemed across the time of the project
- I.e. the cost is close to nothing
---

# What is linting?

Linters enforce [style rules](https://lintlyci.github.io/Flake8Rules/) on the
code, e.g.:
- disallow one letter variables outside of loops
- use `lower_snake_case` for variables
- use `CamelCase` for classes
- disallow nesting more than n deep
- detect code-smells (patterns that are often bugs, e.g. two functions with the
  same name)
- static type detection ([mypy](http://mypy-lang.org/)) where we tell the editor
  what kind of objects (`dict`, `list`, `int`, etc) a function expects

Consistent styles make a code more consistent an easier to read, whether or not
you agree with the style. Using an automated linter avoids bike-shedding since
the linter is the final arbiter.


# Why linting matters?

* code is read more often than written
* setting up a linter in your editor takes 5 minutes
* those 5 minutes are redeemed across the lifetime of the project
* linters shortcut the `edit-run-debug and repeat` workflow

# Rules to choose linters

1. Choose a few
1. Stick with them

We chose:
  - [flake8](https://pypi.org/project/black/) because it simple
  - [pylint](https://www.pylint.org/) because it is (too?) extensive
  - [mypy](http://mypy-lang.org/) because it helps keep track of object types


> ## Exercise:
>
> Setup vs-code:
>
> 1. Open options or the file ".vscode/settings.json"
> 1. Modify the following properties:
>
>     ```json
>     {
>         "python.linting.enabled": true,
>         "python.linting.pylintUseMinimalCheckers": false,
>         "python.linting.flake8Enabled": true,
>         "python.linting.pylintEnabled": true,
>         "python.linting.mypyEnabled": true
>     }
>     ```
>
> 1. Create a file `unlinted.py` with the following code and save it:
>
>    ```python
>    from typing import List
>
>
>    class printer:
>        pass
>
>
>    def ActionatePrinters(printers: List[printer]):
>        # pylint: disable=missing-docstring
>        printing_actions = []
>        for p in printers:
>
>            if p == None:
>                continue
>
>            def action():
>                print(p)
>
>            printing_actions.append(action)
>
>            p = "something"
>            print(p)
>
>        for action in printing_actions:
>            action()
>
>
>    ActionatePrinters([1, 2, 2])
>    ```
> 1. Check the current errors (click on errors in status bar)
> 1. Try and correct them
> 1. Alternatively, try and disable them (but remember: _with great power..._).
>    We've already disabled-one at the function scope level. Check what happens
>    if you move it to the top of the file at the module level.
{: .challenge}

{% include links.md %}

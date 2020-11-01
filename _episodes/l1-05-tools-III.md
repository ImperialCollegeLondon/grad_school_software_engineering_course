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
- It shortcuts the "edit-run-debug and repeat" workflow
- Almost all editors and IDEs have some means to setup automatic linting
- 5 minutes to setup a linter is redeemed across the time of the project i.e. the cost is close to nothing
---

## What is linting?

Linters enforce [style rules](https://lintlyci.github.io/Flake8Rules/) on your
code such as:

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

## Why does linting matter?

- Code is read more often than written
- Setting up a linter in your editor takes 5 minutes
- Those 5 minutes are redeemed across the lifetime of the project
- Linters shortcut the `edit-run-debug and repeat` workflow

## Rules for choosing linters

1. Choose a few
1. Stick with them

We chose:

- [flake8](https://pypi.org/project/black/) because it is simple
- [pylint](https://www.pylint.org/) because it is (too?) extensive
- [mypy](http://mypy-lang.org/) because it helps keep track of object types

> ## Exercise
>
> Setup VS Code:
>
> 1. Return to `messy.py` (now nicely formatted) in VS Code.
> 1. The output of the configured linters is shown displayed by coloured
>    underlining in the editor, coloured vertical sections of the scroll bar and
>    in bottom the status bar. Mouse over the underlined sections of the editor
>    to see the reason for each.
> 1. Check the current errors (click on errors in status bar at the bottom).
> 1. Understand why each error is present and try to correct them.
> 1. Alternatively, try and disable them (but remember: _with great power..._).
>    We've already disabled-one at the function scope level. Check what happens
>    if you move it to the top of the file at the module level.
{: .challenge}

{% include links.md %}

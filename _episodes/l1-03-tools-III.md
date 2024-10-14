---
title: "Tools III: Linters"
teaching: 5
exercises: 10
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
- requiring all code to be appropriately documented

Consistent styles make a code more consistent and easier to read, whether or not
you agree with the style. Using an automated linter avoids bike-shedding since
the linter is the final arbiter.

Linters can also catch common errors such as:

- code that is never executed
- code with undefined behaviour
- variables that are never used

## Why does linting matter?

- Code is read more often than written
- Ensures all code in a project is consistent, even if contributed by multiple
  authors
- Prevent simple bugs and mistakes
- Linters shortcut the `edit-run-debug and repeat` workflow
- Setting up a linter in your editor takes 5 minutes
- Those 5 minutes are redeemed across the lifetime of the project

## Rules for choosing linters

1. Choose one or more
1. Stick with them

We chose:

- [flake8](https://pypi.org/project/black/) because it is simple
- [pylint](https://www.pylint.org/) because it is (too?) extensive

Checkout [GitHub.com: Awesome Linters] to see the range of linters available for
different languages.

> ## Linters in other languages
> - **R**: [lintr](https://lintr.r-lib.org/), with [RStudio integration](https://lintr.r-lib.org/articles/editors.html).
> - **C++**: [clang-tidy](https://clang.llvm.org/extra/clang-tidy/) and [CppCheck](http://cppcheck.net/), although compilers can give lots of helpful linter-type warnings. For `gcc` and `clang`, it's a good idea to pass the `-Wall`, `-Wextra` and `-Wpedantic` flags to get extra ones.
> - **Fortran**: [fortran-linter](https://pypi.org/project/fortran-linter) and via compilers, like [gfortran](https://gcc.gnu.org/wiki/GFortran) or Intel’s [ifort and ifx](https://www.intel.com/content/www/us/en/developer/tools/oneapi/fortran-compiler.html)
{: .callout}

[GitHub.com: Awesome Linters]: https://github.com/caramelomartins/awesome-linters

> ## Exercise (10 min)
>
> Setup VS Code:
>
> 1. Return to `messy.py` (now nicely formatted) in VS Code.
> 1. The output of the configured linters is shown displayed by coloured
>    underlining in the editor, coloured vertical sections of the scroll bar and
>    in the bottom status bar. Mouse over the underlined sections of the editor
>    to see the reason for each.
> 1. Check the current errors (click on errors in status bar at the bottom).
> 1. Understand why each error is present and try to correct them.
> 1. Alternatively, try and disable them (but remember: _with great power..._).
>    We've already disabled-one at the function scope level. Check what happens
>    if you move it to the top of the file at the module level.
{: .challenge}

{% include links.md %}

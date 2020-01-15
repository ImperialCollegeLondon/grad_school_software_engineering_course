---
title: "Tools III: Linters"
teaching: 10
exercises: 5
questions:
- How to make the editor pro-actively find errors and code-smells
objectives:
- Install and use a linter in vscode without sweat
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
- detect code-smells (patterns that are often bugs)
- static type detection ([mypy](http://mypy-lang.org/)) where we tell the editor
what kind of objects (`dict`, `list`, `int`, etc) a function expects


# Why linting matters?

* code is read more often than written
* setting up a linter in your editor takes 5 minutes
* those 5 minutes are redeemed across the lifetime of the project
* linters shortcut the `edit-run-debug and repeat` workflow

# Rules to choose linters

1. Choose a few
1. Stick with them

We chose:
  - [flake8](https://pypi.org/project/black/) because it simple,
  - [pylint](https://www.pylint.org/) because it is (too?) extensive
  - [mypy](http://mypy-lang.org/) because it helps keep track of object types

# Example:

Setup vs-code:

1. Open options or the file ".vscode/settings.json"
1. Modify the following properties:
  ```json
  {
      "python.linting.enabled": true,
      "python.linting.pylintUseMinimalCheckers": false,
      "python.linting.flake8Enabled": true,
      "python.linting.pylintEnabled": true,
      "python.linting.mypyEnabled": true
  }
  ```
1. Check the current errors (click on errors in status bar)
1. Try and correct them
1. Alternatively, try and disable them (but remember: _with great power..._)


```python
{% include softeng/unlinted.py %}
```

{% include links.md %}

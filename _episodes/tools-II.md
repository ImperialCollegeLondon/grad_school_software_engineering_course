---
title: "Tools II: Code-Formatters"
teaching: 3
exercises: 2
questions:
- How to format code with no effort on the part of the coder?
objectives:
- Install and use code formatter in vscode without sweat
keypoints:
- Code formatting means how the code is type-set
- It influences how easily the code is read
- It has no inpact on how the code runs
- Almost all editors and IDE's have some means to setup an automatic formatter
- 5 minutes to setup the formatter is redeemed across the time of the project
- I.e. the cost is close to nothing
---

# Why formatting matters?

* code is read more often than written
* setting up a formatter in your editor takes 5 minutes
* those 5 minutes are redeemed across the lifetime of the project

# Rules to choose a code-formatter

1. Choose one
1. Stick with it

We chose [black](https://pypi.org/project/black/) because it has very few
options with which to fidle.

# Example:

Setup vs-code ([install it first](https://code.visualstudio.com/)):

1. Open options or the file ".vscode/settings.json"
1. Set up the black as the "python.formatting.provider"
1. Optionally, set up "editor.formatOnSave" and "editor.formatOnType"

```python
{% include softeng/unformatted.py %}
```

{% include links.md %}

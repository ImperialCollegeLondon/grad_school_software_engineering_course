---
title: "Data Structures"
teaching: 15
exercises: 15
questions:
- How can data-structures simplify codes?
objectives:
- Understand why different data-structures exist
- Recall common data-structures
- Recognize where and when to use them
keypoints:
- Data-structures are the representation of information the same way algorithm
  represent logic and workflows
- Using the right data-structure can vastly simplify code
- Basic data-structures include numbers, strings, tuples, lists, dictionaries
  and sets.
- Advanced data-structures include numpy array and panda dataframes
- Classes are custom data-structures
---

# What is a data-structure?

- Data-structure represent information and how that information can be
  accessed

## Examples:

The number `2` is represented with the integer `2`

```python
>>> type(2)
int
```

Acceptable behaviors for integers include `+`, `-`, `*`, `/`

```python
>>> 1 + 2
3
>>> 1 - 2
-1
```

On the other hand, text is represented by a string

```python
>>> type("text")
str
```

It does *not* accept all the same behaviours as an integer:

```python
>>> "a" + "b"
"ab"
>>> "a" * "b"
TypeError: can't multiply sequence by non-int of type 'str'
```

Integers *can* be represented as strings, but their behaviours would be
unexpected:

```python
>>> "1" + "2"
"12"
```

With integers, `+` is an *addition*, for strings its a *concatenation*.

** Using the wrong data-structures can make your code vastly more complicated.
**


# Basic data-structures

## Lists

Lists are containers of other data:

```python
# List of integers
[1, 2, 3]
# List of strings
["a", "b", "b"]
# List of lists of integers
[[1, 2], [2, 3]]
```

Lists make sense when:

- you have more than one item of data
- the items are somehow related: Lists of apples and oranges are a code-smell

   ```python
   [1, 2, 3]  # might be the right represention
   ["a", 2, "b"]  # probably wrong
   ```

- the items are ordered and can be accessed

   ```python
   >>> velocities_x = [0.3, 0.5, 0.1]
   >>> velocities_x[1]  # e.g. could be velocity a point x=1
   ```

Beware! The following might indicate a list is the wrong data-structure:

   - apples and oranges
   - deeply nested list of lists of lists

## Tuples

Tuples are **short** and **immutable** containers of other data.

```
(1, 2)
("a", b")
```

Immutable means once that once created, elements cannot be added, removed or
replaced:

```python
>>> shape = 2, 4
>>> shape
(2, 4)
>>> shape[1] = 4
TypeError: 'tuple' object does not support item assignment
```

**Note**: in python, it can be that an element of a tuple can be modified:

```Python
>>> something = ["a", "b"], 4
>>> something[0].append("c")
>>> something
(['a', 'b', 'c'], 4)
>>> something[0] = ["a", "b", "c"]
TypeError: 'tuple' object does not support item assignment
```

The tuple itself cannot be modified, but its elements can be if they themselves
are not immutable.

Tuple make sense when:

- you need a short of a few data elements
- the list does not need to be modified or should not be modified
- great for functions returning more than one *thing*

Beware! The following might indicate a tuple is the wrong data-structure:

- the elements have no relationship (apples and oranges)
- more than four or five elements
- difficult to remember which element is what
  (is it `result[1]` I need or `result[2]?`)

## Sets

Sets are containers *unique* pieces of data:

```python
>>> set([1, 2, 2, 3, 3])
{1, 2, 3}
```

They make sense when:

- each element in a container must be unique
- you need to solve ownership issues, e.g. which elements are in common between
  two lists? Which elements are different?

    ```Python
    >>> set(["a", "b", "c"]).symmetric_difference(["b", "c", "e"])
    {'a', 'e'}
    ```

## Dictionaries

Dictionaries are mappings between a key and a value (e.g. a word and it's
definition).

```Python
# mapping of animals to legs
{"horse": 4, "kangaroo": 2, "millipede": 1000}
```

They make sense when:

- you have pairs of data that go together:

    ```python
    # A list of pairs?? PROBABLY BAD!!
    [("horse", "mammal"), ("kangaroo", "marsupial"), ("millipede", "alien")]
    # Better?
    {"horse": "mammal", "kangaroo": "marsupial", "millipede": "alien"}
    # Or maybe?
    {"mammal": {"horse", "cow"}, "alien": {"millipede", "Jadoo"}}
    ```
- given x you want to know it's y: given the name of an animal you want to know
  the number of legs.

- often used as bags of configuration options

Beware! The following might indicate a list is the wrong data-structure:

   - keys are not related to each other, or values are not related to each other

    ```python
    {1: "apple", "orange": 2}
    ```

    `1` not related to `"orange"` and `2` not related to `"apple"`

   - deeply nested dictionaries of dictionaries of lists of dictionaries


## Advanced data-structures


- [numpy arays](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html)
  are multidimensional array of numbers
- [panda datframes](https://pandas.pydata.org/pandas-docs/stable/index.html")
  are collections of named 1-d arrays, i.e. excell spread-sheets on steroids
- [xarray arrays](http://xarray.pydata.org/en/stable/) are multi-dimensional
  arrays that can be indexed with rich objects, e.g. an array indexed by
  dates or by longitude and lattitude, rather than by the numbers 0, 1, 2, 3.
- [xarray datasets](http://xarray.pydata.org/en/stable/) are collections of
  named [xarray arrays](http://xarray.pydata.org/en/stable/) that share some
  dimensions.

## Custom data-structures: Data classes

Python (>= 3.7) makes it easy to create custom data-structures.

```python
>>> from typing import List, Text
>>> from dataclasses import dataclass
>>> @dataclass
... class MyData:
...   a_list: List[int]
...   b_string: Text = "something something"
>>> data = MyData([1, 2])
>>> data
MyData(a_list=[1, 2], b_string='something something')
>>> data.a_list
[1, 2]
```

Data-classes make sense when:

- you have a collections of related data that does not fit a more primitive type
- you already have a class and you don't want to write standard functions like
  `__init__`, `__repr__`, `__ge__`, etc..

Beware! The following might indicate a `dataclass` is the wrong data-structure:

- you do need specialized `__init__` behaviours (just use a class)
- single huge mother of all classes that does everything (split into smaller
  specialized classes and/or stand-alone functions)
- a `dict`, `list` or `numpy` array would do the job. Everybody knows what a
  `numpy` array is and how to use it. But even your future self might not know
  how to use your very special class.


# Exercise:

1. In your own time, find out all the thing a
   [list](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists),
   a [set](https://docs.python.org/3/tutorial/datastructures.html#sets), or
   [dict](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
   can do. Don't reinvent the square wheel.

1. Implement an oxford dictionary with two lists, one for words, one for
definitions:

    ```yaml
    scarf: (noun) a garment worn around the head or neck or shoulders for warmth
      or decoration
    snarf: (verb) make off with belongings of others
    barf: (verb) eject the contents of the stomach through the mouth
    dwarf: |
      (verb) make appear small by comparison
      (noun) a legendary bearded creature
    morph: (verb) change shape as via computer animation
    surf: |
      (verb) switch channels, on television
      (noun) waves breaking on the shore
    ```

1. Given a word, find and modify it's definition
1. Do the same with a dictionary
1. Create a subset of words rhyming with "arf" using either the two-`list` or
   the `dict` implementation
1. If now we want to also encode "noun" and "verb", what data-structure could we
use?
1. What about when there are multiple meanings for a verb or a noun?

{% include links.md %}

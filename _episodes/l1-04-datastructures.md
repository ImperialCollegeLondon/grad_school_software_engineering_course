---
title: "Data Structures"
teaching: 30
exercises: 25
questions:
- How can data structures simplify codes?
objectives:
- Understand why different data structures exist
- Recall common data structures
- Recognize where and when to use them
keypoints:
- Data structures are the representation of information the same way algorithms
  represent logic and workflows
- Using the right data structure can vastly simplify code
- Basic data structures include numbers, strings, tuples, lists, dictionaries
  and sets.
- Advanced data structures include numpy array and panda dataframes
- Classes are custom data structures
---

# What is a data structure?

```yaml
data structure: represents information and how that information can be accessed
```

Choosing the right representation for your data can vastly simplify your code
and increase performance.

Choosing the wrong representation can melt your brain. Slowly.

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

With integers, `+` is an *addition*, for strings it's a *concatenation*.

## Health impact of choosing the wrong data structure

- we could use `"1", "2", "3"` to represent numbers, rather than `1`, `2`, `3`
- we would have to reinvent how to add numbers, and multiply, and divide them
  e.g.

  ```python
  str(int("1") + int("2"))
  ```

  rather than just:

  ```python
  1 + 2
  ```

- the wrong data structures can make your code vastly more complicated
- also, the code would be much slower

Stay healthy. Stop and choose the right data structure for you!

> ## Priorities for Choosing Data Structures
>
> We've discussed how the incorrect data structure can make your code more
> complicated and also give worse performance. Quite often these two factors are
> aligned - the right data structure will combine simple code with the best
> performance. This isn't always true however. In some cases simplicity and
> performance will be in tension with one another. A good maxim to apply here is
> **"Premature optimization is the root of all evil"**. This philosophy states
> that keeping your code simple and elegant should be your primary
> goal. Choosing a data structure based on performance or other considerations
> should only be considered where absolutely necessary.
{: .callout}

# Basic data structures

Different languages provide different basic structures depending on the purpose
for which they were designed. We will consider here some of the basic data
structures available in Python for which equivalents can be found in most other
languages.

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
- the items are somehow related: Lists of apples and oranges are a [code-smell](https://en.wikipedia.org/wiki/Code_smell)

   ```python
   [1, 2, 3]  # might be the right representation
   ["a", 2, "b"]  # probably wrong
   ```

- the items are ordered and can be accessed

   ```python
   >>> velocities_x = [0.3, 0.5, 0.1]
   >>> velocities_x[1]  # e.g. could be velocity a point x=1
   ```

Beware! The following might indicate a list is the wrong data structure:

   - apples and oranges
   - deeply nested list of lists of lists

> ## Tuples
>
> Python also has tuples which are very similar to lists. The main difference is
> that tuples are immutable which means that they can't be altered after
> creation.
>
> ```python
> >>> a = ("a", "b")
> >>> a[0] = "c"
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> TypeError: 'tuple' object does not support item assignment
> ```
{: .callout}

> ## Other languages
> * C++:
>   - [std::vector](https://en.cppreference.com/w/cpp/container/vector), fast
>     read-write to element i and fast iteration operations. Slow insert
>     operation.
>   - [std::list](https://en.cppreference.com/w/cpp/container/list). No direct
>     access to element i. Fast insert, append, splice operations.
> * R: [list](http://www.r-tutor.com/r-introduction/list)
> * Julia: [Array](https://docs.julialang.org/en/v1/manual/arrays/), also
>     equivalent to numpy arrays.
> * Fortran: [array](https://www.tutorialspoint.com/fortran/fortran_arrays.htm),
>     closer to numpy arrays than python lists
{: .callout}

## Sets

Sets are containers where each element is *unique*:

```python
>>> set([1, 2, 2, 3, 3])
{1, 2, 3}
```

They make sense when:

- each element in a container must be unique
- you need to solve ownership issues, e.g. which elements are in common between
  two lists? Which elements are different?

    ```python
    >>> set(["a", "b", "c"]).symmetric_difference(["b", "c", "e"])
    {'a', 'e'}
    ```

Something to bear in mind with sets is that, depending on your language, they
may or may not be *ordered*. In Python sets are unordered i.e. the elements of a
set cannot be accessed via an index, but sets in other languages may allow this.

> ## Other languages
> * C++: [std::set](https://en.cppreference.com/w/cpp/container/set)
> * R: [set functions](
>      https://stat.ethz.ch/R-manual/R-devel/library/base/html/sets.html)
>      that operate on a standard list.
> * Julia: [Set](https://docs.julialang.org/en/v1/base/collections/#Base.Set)
> * Fortran: Nope. Nothing.
{: .callout}

## Dictionaries

Dictionaries are mappings between a key and a value (e.g. a word and its
definition).

```python
# mapping of animals to legs
{"horse": 4, "kangaroo": 2, "millipede": 1000}
```

They make sense when:

- you have pairs of data that go together:

  ```python
  # A list of tuples?? PROBABLY BAD!!
  [
    ("horse", "mammal"),
    ("kangaroo", "marsupial"),
    ("millipede", "alien")
  ]
  # Better?
  {
    "horse": "mammal",
    "kangaroo": "marsupial",
    "millipede": "alien"
  }
  ```

- given x you want to know its y: given the name of an animal you want to know
  the number of legs.

- often used as bags of configuration options

Beware! The following might indicate a dict is the wrong data structure:

- keys are not related to each other, or values are not related to each other

  ```python
  {1: "apple", "orange": 2}
  ```

  `1` not related to `"orange"` and `2` not related to `"apple"`

- deeply nested dictionaries of dictionaries of lists of dictionaries


> ## Other languages
> * C++: [std::map](https://en.cppreference.com/w/cpp/container/map)
> * R: cran package [hash](https://cran.r-project.org/web/packages/hash/)
> * Julia: [Dict](https://docs.julialang.org/en/v1/base/collections/#Base.Dict)
> * Fortran: Nope. Nothing.
{: .callout}

> ## Basic Data Structure Practice (15 min)
>
> You're writing a piece of code to track the achievements of players of a
> computer game. You've been asked to design the data structures the code will
> use. The software will need the following data structures as either a list, a
> dictionary or a set:
>
> - A collection containing all possible achievements
> - A collection for each player containing their achievements in the *order
>   they were obtained* (assume no duplicates)
> - A collection relating player names to their achievements
>
> You're also told that the following operations on these datastructures will be
> needed:
>
> - get a player's achievements
> - get a player's first achievement
> - add a new achievement for a player
> - get the number of achievements a player doesn't have yet
> - get a collection of the achievements a player doesn't have yet
> - find the achievements "player1" has that "player2" doesn't
>
> Implement the data structures as seems most appropriate and populate them with
> some example data. Then have a go at writing code for some of the necessary
> operations. If you picked the right structures, each action should be able to
> be implemented as a single line of code.
>
> > ## Solution
> > ```python
> > all_achievements = {"foo", "bar", "baz"}
> >
> > player_achievements = {
> >     "player1": ["foo", "baz"],
> >     "player2": [],
> >     "player3": ["baz"],
> > }
> >
> > # get a player's achievements
> > player_achievements["player2"]
> >
> > # get a player's first achievement
> > player_achievements["player1"][0]
> >
> > # add a new achievement to a player's collection
> > player_achievements["player2"].append("foo")
> >
> > # get the number of achievements a player doesn't have yet
> > len(all_achievements) - len(player_achievements["player2"])
> >
> > # get a collection of the achievements a player doesn't have yet
> > all_achievements.difference(player_achievements["player1"])
> >
> > # find the achievements player1 has that player2 doesn't
> > set(player_achievements["player1"]).difference(player_achievements["player2"])
> > ```
> > Notice that for the last action we had to turn a list into a set. This isn't
> > a bad thing but if we were having to do it a lot that might be a sign we'd
> > chosen an incorrect data structure.
> {: .solution}
{: .challenge}

## Advanced data structures

Whilst basic data structures provide the fundamental building blocks of a piece
of software, there are many more sophisticated structures suited to specialised
tasks. In this section we'll take a brief look at a variety of different data
structures that provide powerful interfaces to write simple code.

Getting access to advanced data structures often involves installing additional
libraries. As a rule of thumb, for any data structure you can think of somebody
will already have published an implementation of it and its strongly recommended
to use an available version rather than try to write one from scratch. We've
discussed the best approach to managing dependencies for a project already.

### Pandas Data Frames

The excellent and very powerful Panda's package is the go to resource for
dealing with tabular data. Anything you might think of using Excel for, Panda's
can do better. It leans heavily on NumPy for efficient numerical operations
whilst providing a high level interface for dealing with rows and columns of
data via [pandas.DataFrame][pandas].

[pandas]: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

```python
# working with tabular data in nested lists

data = [
    ["col1", "col2", "col3"],
    [0, 1, 2],
    [6, 7, 8],
    [0, 7, 8],
]

# get a single row or column
row = data[0]
col = [row[data[0].index("col1")] for row in data]

# filter out rows where col1 != 0
[data[0]] + [row for row in data[1:] if row[0] == 0]

# operate on groups of rows based on the value of col1
for val in set([row[0] for row in data[1:]]):
    rows = [row for row in data[1:] if row[0] == val]

# vs

import pandas as pd

# many flexible ways to create a dataframe e.g. import from csv, but here we
# use the use the existing data.
dataframe = pd.DataFrame(data[1:], columns=data[0])

# get a single row or column
row = dataframe.iloc[0]
col = dataframe["col1"]

# filter out rows where col1 != 0
dataframe[dataframe["col1"] == 0]

# operate on groups of rows based on the value of col1
dataframe.groupby("col1")
```

### Balltrees

A common requirement across many fields is working with data points within a 2d,
3d or higher dimensioned space where you often need to work with distances
between points. It is tempting in this case to reach for lists or arrays but
balltrees provide an interesting and very performant alternative in some
cases. An implementation is provided in Python by the [scikit-learn][] library.

[scikit-learn]: https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html

```python
# Which point is closest to the centre of a 2-d space?

points = [
    [0.1, 0.1],
    [1.0, 0.1],
    [0.2, 0.2],
    [0.1, 0.3],
    [0.9, 0.2],
    [0.2, 0.3],
]
centre = [0.5, 0.5] # centre of our space

# Using lists

distances = []
for i, point in enumerate(points):
    dist = ((centre[0] - point[0])**2 + (centre[1] - point[1])**2)**0.5
    distances.append(dist)

smallest_dist = sorted(distances)[0]
nearest_index = distances.index(smallest_dist)

# vs

from sklearn.neighbors import BallTree

balltree = BallTree(points)
smallest_dist, nearest_index = balltree.query([centre], k=1)
```

# Graphs and Networks

Another type of data structure that spans many different research domains are
graphs/networks. There are many complex algorithms that can be applied to graphs
so checkout the NetworkX library for its [data structures][networkx].

[networkx]: https://networkx.org/documentation/stable/tutorial.html

```python
edges = [
    [0, 1],
    [1, 2],
    [2, 4],
    [3, 1]
]

# Using lists

# get the degree (number of connected edges) of node 1

degree_of_1 = 0
for edge in edges:
    if 1 in edge:
        degree_of_1 += 1

# vs

import networkx as nx

graph = nx.Graph(edges)

# get the degree (number of connected edges) of node 1
graph.degree[1]

# easy to perform more advanced graph operations e.g.
graph.subgraph([1,2,4])
```

## Custom data structures: Data classes

Python (>= 3.7) makes it easy to create custom data structures.

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

Data classes make sense when:

- you have a collections of related data that does not fit a more primitive type
- you already have a class and you don't want to write standard functions like
  `__init__`, `__repr__`, `__ge__`, etc..

Beware! The following might indicate a `dataclass` is the wrong data structure:

- you do need specialized `__init__` behaviours (just use a class)
- single huge mother of all classes that does everything (split into smaller
  specialized classes and/or stand-alone functions)
- a `dict`, `list` or `numpy` array would do the job. Everybody knows what a
  `numpy` array is and how to use it. But even your future self might not know
  how to use your very special class.

> ## Exploring data structures
>
> Take some time to read in more detail about any of the data structures covered
> above or those below:
>
> - [deques](https://docs.python.org/3/library/collections.html#collections.deque)
> - [named tuples](https://docs.python.org/3/library/collections.html#collections.namedtuple)
> - [counters](https://docs.python.org/3/library/collections.html#collections.Counter)
> - [dates](https://docs.python.org/3/library/datetime.html)
> - [enum](https://docs.python.org/3/library/enum.html) represent objects that can
>   only take a few *values*, e.g. colors. Often useful for configuration options.
> - [numpy arrays](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html)
>   (multidimensional array of numbers)
> - [xarray arrays](http://xarray.pydata.org/en/stable/) (multi-dimensional
>   arrays that can be indexed with rich objects, e.g. an array indexed by
>   dates or by longitude and latitude, rather than by the numbers 0, 1, 2, 3)
> - [xarray datasets](http://xarray.pydata.org/en/stable/) (collections of
>   named [xarray arrays](http://xarray.pydata.org/en/stable/) that share some
>   dimensions.)
> 
> Don't reinvent the square wheel.
{: .challenge}

> ## Digital Oxford Dictionary, the wrong way and the right way (10 min)
> 1. Implement an oxford dictionary with two `list`s, one for words, one for
> definitions:
>
>     ```yaml
>     barf: (verb) eject the contents of the stomach through the mouth
>     morph: (verb) change shape as via computer animation
>     scarf: (noun) a garment worn around the head or neck or shoulders for warmth
>       or decoration
>     snarf: (verb) make off with belongings of others
>     sound: |
>       (verb) emit or cause to emit sound.
>       (noun) vibrations that travel through the air or another medium
>     surf: |
>       (verb) switch channels, on television
>       (noun) waves breaking on the shore
>     ```
>
> 1. Given a word, find and modify its definition
> 1. Repeat 1. and 2. with a `dict` as the datastructure.
> 1. Create a subset dictionary (including definitions) of words rhyming with
>    "arf" using either the two-`list` or the `dict` implementation
> 1. If now we want to also encode "noun" and "verb", what data structure could we
>    use?
> 1. What about when there are multiple meanings for a verb or a noun?
> 
> > ## Dictionary implemented with lists
> >
> > ```python
> > def modify_definition(word, newdef, words, definitions):
> >     index = words.index(word)
> >     definitions = definitions.copy()
> >     definitions[index] = newdef
> >     return definitions
> >
> >
> > def find_rhymes(rhyme, words, definitions):
> >     result_words = []
> >     result_definitions = []
> >     for word, definition in zip(words, definitions):
> >         if word.endswith(rhyme):
> >             result_words.append(word)
> >             result_definitions.append(definition)
> >     return result_words, result_definitions
> >
> >
> > def testme():
> >
> >     words = ["barf", "morph", "scarf", "snarf", "sound", "surf"]
> >     definitions = [
> >         "(verb) eject the contents of the stomach through the mouth",
> >         "(verb) change shape as via computer animation",
> >         (
> >             "(noun) a garment worn around the head or neck or shoulders for"
> >             "warmth or decoration"
> >         ),
> >         "(verb) make off with belongings of others",
> >         (
> >             "(verb) emit or cause to emit sound."
> >             "(noun) vibrations that travel through the air or another medium"
> >         ),
> >         (
> >             "(verb) switch channels, on television"
> >             "(noun) waves breaking on the shore"
> >         ),
> >     ]
> >
> >     newdefs = modify_definition("morph", "aaa", words, definitions)
> >     assert newdefs[1] == "aaa"
> >
> >     rhymers = find_rhymes("arf", words, definitions)
> >     assert set(rhymers[0]) == {"barf", "scarf", "snarf"}
> >     assert rhymers[1][0] == definitions[0]
> >     assert rhymers[1][1] == definitions[2]
> >     assert rhymers[1][2] == definitions[3]
> > ```
> {: .solution}
> > ## Dictionary implemented with a dictionary
> >
> > ```python
> > def modify_definition(word, newdef, dictionary):
> >     result = dictionary.copy()
> >     result[word] = newdef
> >     return result
> >
> >
> > def find_rhymes(rhyme, dictionary):
> >     return {
> >         word: definition
> >         for word, definition in dictionary.items()
> >         if word.endswith(rhyme)
> >     }
> >
> >
> > def testme():
> >
> >     dictionary = {
> >         "barf": "(verb) eject the contents of the stomach through the mouth",
> >         "morph": "(verb) change shape as via computer animation",
> >         "scarf": (
> >             "(noun) a garment worn around the head or neck or shoulders for"
> >             "warmth or decoration"
> >         ),
> >         "snarf": "(verb) make off with belongings of others",
> >         "sound": (
> >             "(verb) emit or cause to emit sound."
> >             "(noun) vibrations that travel through the air or another medium"
> >         ),
> >         "surf": (
> >             "(verb) switch channels, on television"
> >             "(noun) waves breaking on the shore"
> >         ),
> >     }
> >
> >     newdict = modify_definition("morph", "aaa", dictionary)
> >     assert newdict["morph"] == "aaa"
> >
> >     rhymers = find_rhymes("arf", dictionary)
> >     assert set(rhymers) == {"barf", "scarf", "snarf"}
> >     for word in {"barf", "scarf", "snarf"}:
> >         assert rhymers[word] == dictionary[word]
> > ```
> {: .solution}
> > ## More complex data structures for more complex dictionary
> >
> > There can be more than one good answer. It will depend on how the dictionary
> > is meant to be used later throughout the code.
> >
> > Below we show three possibilities. The first is more deeply nested. It groups
> > all definitions together for a given word, whether that word is a noun or a
> > verb. If more often than not, it does not matter so much what a word is, then
> > it might be a good solution. The second example flatten the dictionary by
> > making "surf" the noun different from "surf" the verb. As a result, it is
> > easier to access a word with a specific semantic category, but more difficult
> > to access all definitions irrespective of their semantic category.
> >
> > One pleasing aspect of the second example is that together things that are
> > unlikely to change one one side (word and semantic category), and a less
> > precise datum on the other (definitions are more likely to be refined).
> >
> > The third possibility is a
> > [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) `DataFrame`
> > with three columns. It's best suited to big-data problems where individual
> > words (rows) are seldom accessed one at a time. Instead, most operations are
> > carried out over subsets of the dictionary.
> >
> > ```python
> > from typing import Text
> > from enum import Enum, auto
> > from dataclasses import dataclass
> > from pandas import DataFrame, Series
> >
> >
> > class Category(Enum):
> >     NOUN = auto
> >     VERB = auto
> >
> >
> > @dataclass
> > class Definition:
> >     category: Category
> >     text: Text
> >
> >
> > first_example = {
> >     "barf": [
> >         Definition(
> >             Category.VERB, "eject the contents of the stomach through the mouth"
> >         )
> >     ],
> >     "morph": [
> >         Definition(
> >             Category.VERB, "(verb) change shape as via computer animation"
> >         )
> >     ],
> >     "scarf": [
> >         Definition(
> >             Category.NOUN,
> >             "a garment worn around the head or neck or shoulders for"
> >             "warmth or decoration",
> >         )
> >     ],
> >     "snarf": Definition(Category.VERB, "make off with belongings of others"),
> >     "sound": [
> >         Definition(Category.VERB, "emit or cause to emit sound."),
> >         Definition(
> >             Category.NOUN,
> >             "vibrations that travel through the air or another medium",
> >         ),
> >     ],
> >     "surf": [
> >         Definition(Category.VERB, "switch channels, on television"),
> >         Definition(Category.NOUN, "waves breaking on the shore"),
> >     ],
> > }
> >
> >
> > # frozen makes Word immutable (the same way a tuple is immutable)
> > # One practical consequence is that dataclass will make Word work as a
> > # dictionary key: Word is hashable
> > @dataclass(frozen=True)
> > class Word:
> >     word: Text
> >     category: Text
> >
> >
> > second_example = {
> >     Word(
> >         "barf", Category.VERB
> >     ): "eject the contents of the stomach through the mouth",
> >     Word("morph", Category.VERB): "change shape as via computer animation",
> >     Word("scarf", Category.NOUN): (
> >         "a garment worn around the head or neck or shoulders for"
> >         "warmth or decoration"
> >     ),
> >     Word("snarf", Category.VERB): "make off with belongings of others",
> >     Word("sound", Category.VERB): "emit or cause to emit sound.",
> >     Word(
> >         "sound", Category.NOUN
> >     ): "vibrations that travel through the air or another medium",
> >     Word("surf", Category.VERB): "switch channels, on television",
> >     Word("surf", Category.NOUN): "waves breaking on the shore",
> > }
> >
> > # Do conda install pandas first!!!
> > import pandas as pd
> >
> > third_example = pd.DataFrame(
> >     {
> >         "words": [
> >             "barf",
> >             "morph",
> >             "scarf",
> >             "snarf",
> >             "sound",
> >             "sound",
> >             "surf",
> >             "surf",
> >         ],
> >         "definitions": [
> >             "eject the contents of the stomach through the mouth",
> >             "change shape as via computer animation",
> >             (
> >                 "a garment worn around the head or neck or shoulders for"
> >                 "warmth or decoration"
> >             ),
> >             "make off with belongings of others",
> >             "emit or cause to emit sound.",
> >             "vibrations that travel through the air or another medium",
> >             "switch channels, on television",
> >             "waves breaking on the shore",
> >         ],
> >         "category": pd.Series(
> >             ["verb", "verb", "noun", "verb", "verb", "noun", "verb", "noun"],
> >             dtype="category",
> >         ),
> >     }
> > )
> > ```
> {: .solution}
{: .challenge}


{% include links.md %}

---
title: "Design Patterns"
teaching: 10
exercises: 20
questions:
- how can we avoid re-inventing the wheel when designing code?
- how can we transfer known solutions to our code?
objectives:
- recognize much-used patterns in existing code
- re-purpose existing patterns as solutions to new problems
keypoints:
- Many coders have come before
- Transferable solutions to common problems have been identified
- It is easier to apply a known pattern than to reinvent it, but first you have
  to spend some time learning about patterns.
- Iterators and generators are convenient patterns to separate loops from
  compute and to avoid copy-pasting.
---

# What is a design pattern?

```yaml
software design pattern: typical solutions to common problems
```

### Pros

1. It is easier to reuse known solutions than to invent them
1. Makes reading the code simpler to parse for collaborators
1. Makes the code easier to maintain since patterns ought to be best-in-class
  solutions

### Cons

1. shoehorning: not all patterns fit everywhere
1. patterns paper-over inadequacies that exist in one language but not another
   - the [visitor](https://en.wikipedia.org/wiki/Visitor_pattern) pattern is
     popular in Java or C++, but useless in [Julia](https://www.julia.org),
     thanks to [multiple
     dispatch](https://en.wikipedia.org/wiki/Multiple_dispatch)
   - [Haskell](https://www.haskell.org/)'s
     [functional](https://en.wikipedia.org/wiki/Functional_programming) style
     makes the [strategy](https://en.wikipedia.org/wiki/Strategy_pattern)
     pattern so obvious, it's not longer a pattern, it's the way things are done

### Examples:

- [iterator](https://en.wikipedia.org/wiki/Iterator_pattern) pattern (also see
  below) separates how to loop from what to do in a loop
- [resource allocation is
  acquisition](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization)
  idiom promotes creating fully functional objects in one go
- [dependency injection](https://en.wikipedia.org/wiki/Dependency_injection)
  makes it easier to create modular algorithms
- [factory](https://en.wikipedia.org/wiki/Factory_method_pattern) pattern
    separates creating object from the class of the object
- [adapter](https://en.wikipedia.org/wiki/Adapter_pattern) pattern interfaces
  one class to be used in an another
- [more](https://en.wikipedia.org/wiki/Software_design_pattern) and
  [more](https://refactoring.guru/design-patterns) and
  [more](https://stackoverflow.com/) patterns
- And let's not forget
  [anti-patterns](https://en.wikipedia.org/wiki/Anti-pattern#Software_engineering),
  i.e. patterns that should **not** be used

# Iterator Pattern

Iterators separates _generating items over which to loop_ from _doing the body of the loop_.
the loop.

For instance, we want to loop over all items in `xs` and `ys`:

```python
for x in xs:
    for y in ys:
        compute(x, y)
```

can be transformed to:

```python
from itertools import product

for x, y in product(xs, ys):
    compute(x, y)
```

Where `product` returns an iterator, i.e. something we can loop over.


# How iterators are defined in python

An iterator is something which follows the iterator protocol:

```python
from typing import Iterable
class MyIterator:
    def __next__(self):
        """
        Returns a new element with each call.
        Raises `StopIteration` to stop loop
        """
        pass

    def __iter__(self) -> Iterable:
        """ Might (re-)set some state """
        return self
```

For instance, an iterator implementing `range(n)` would be:

```python
class MyIterator:

    def __init__(self, n):
        self.last = n
        self.current = 0

    def __next__(self):
        self.current += 1

        if self.current >= self.last:
            raise StopIteration

        return self.current

    def __iter__(self):
        """ returns reset iterator. """
        return self
```

Then the loop:

```python
for i in MyIterator(3):
    print(i)
```

Is functionally equivalent to:

```python
iterator = MyIterator(3)

while True:
    try:
        i = iterator.__next__()
        print(i)
    except StopIteration:
        break
```


# Generators: iterators made easy


Generators create iterators using syntax that is more similar to the standard
loop:

```python
for x in xs:
    for y in ys:
        print(f"some complicated calculation with {x} and {y}")
```

We can _lift_ the loops out of the code and create a generator:

```python
def my_generator(xs, ys):
  for x in xs:
      for y in ys:
          yield x, y
```

And then loop with an iterator python creates auto-magically:

```python
for x, y in my_generator(xs, ys):
    print(f"some complicated calculation with {x} and {y}")
```

In practice, python runs through the code in `my_generator` and returns a new
element each time it hits yield. The next time it is called, it restarts from
the line _right after yield_.

# When to user generators?

1. To separate complex loops from complex calculations in the loop
1. Complex loops that occur multiple times in the code (copy-paste is a
   foot gun).
1. When running out of memory, create a [lazy iterator]
1. Use iterators when the language does not allow for generators (.e.g.
[c++](https://en.cppreference.com/w/cpp/iterator/iterator)).

## Exercise

> ## Power of two iterator
>
> What does this print out?
>
> ```python
> def powers_of_two(xs):
>     for x in xs:
>         yield 2**x
>
> for x in power_of_two([2, 4, 3, 2]):
>     print(x)
> ```
{: .challenge}

> ## Power of two iterator
> ```output
> 4
> 16
> 9
> 4
> ```
{: .solution}

> ## Interleaved power of two and squares
>
> How about this? Where does the function return two on after the first element,
> what about after the second element?
>
>  ```python
>  def interleaved(xs):
>      for x in xs:
>          yield 2 ** x
>          yield x ** 2
>
>  for x in interleaved([2, 4, 3, 2]):
>      print(x)
>  ```
{: .challenge}

> ## Interleaved power of two and squares
> ```output
> 4
> 4
> 16
> 16
> 8
> 9
> 4
> 4
> ```
{: .solution}

> ## Sequential power of two and squares
>
>
>  ```python
>  def sequential(xs):
>
>    for x in xs:
>        yield 2 ** x
>
>    for x in xs:
>        yield x ** 2
>
>  for x in sequential([2, 4, 3, 2]):
>      print(x)
>  ```
{: .challenge}

> ## Interleaved power of two and squares
> ```output
> 4
> 16
> 8
> 4
> 4
> 16
> 9
> 4
> ```
{: .solution}



> ## Iterating over points in a ring
>
> Create an iterator and/or a generator that lifts the loop over points in a
> two-dimensional ring:
>
> Take this code:
>
> ```python
> from math import sqrt
> points = [[1, 2], [0, 0], [-2, 0], [-2, 3], [-3, -4], [4, 0], [5, 5]]
> radius = 3.5
> width = 1.0
>
> inner = radius - 0.5 * width
> outer = radius + 0.5 * width
> for point in points:
>     distance = sqrt(point[0] * point[0] + point[1] * point[1])
>     if distance >= inner and distance <= outer:
>         print(f"Some complicated calculation at {point}")
> ```
>
> and create an iterator `PointsInRing`
>
> ```python
> for point in PointsInRing(points, radius, width)
>     print(f"Some complicated calculation at {point}")
> ```
>
> and/or create a generator function `point_in_ring`:
>
> ```python
> for point in points_in_ring(points, radius, width)
>     print(f"Some complicated calculation at {point}")
> ```
>
> **NOTE:**
> - `points_in_ring` and `PointsInRing` can be used over and over across
>   the code
> - they are parametrized by radius and width
> - they make the loop self-descriptive
> - they are more memory efficient ([lazy
>   evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation)) - almost always
> - better than creating and keeping in sync a second list holding
    only points in a ring (compute is cheap)
> - they make it possible to test/debug the loop alone, without worrying about
    the compute inside the loop
{: .challenge}

{% include links.md %}

---
title: "Design Patterns"
teaching: 15
exercises: 15
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
- Dependency injections is a pattern to create modular algorithms
---

# What is a design pattern?

```yaml
software design pattern: typical solutions to common problems
```

### Pros

1. It is easier to reuse known solutions than to invent them
1. Makes the code easier to understand for collaborators
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

- [iterator](https://en.wikipedia.org/wiki/Iterator_pattern) pattern (see
  below) separates how to loop from what to do in a loop
- [dependency injection](https://en.wikipedia.org/wiki/Dependency_injection)
  (see below) makes it easier to create modular algorithms
- [resource allocation is
  acquisition](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization)
  idiom promotes creating fully functional objects in one go
- [factory](https://en.wikipedia.org/wiki/Factory_method_pattern) pattern
    separates creating object from the class of the object. It is used to unify
    or simplify the creation of similar objects into a single function.
- [adapter](https://en.wikipedia.org/wiki/Adapter_pattern) pattern interfaces
  one class to be used in an another
- [more](https://en.wikipedia.org/wiki/Software_design_pattern) and
  [more](https://refactoring.guru/design-patterns) and
  [more](https://stackoverflow.com/) patterns
- And let's not forget
  [anti-patterns](https://en.wikipedia.org/wiki/Anti-pattern#Software_engineering),
  i.e. patterns that should **not** be used

# Iterator Pattern

Iterators separates _generating items over which to loop_ from _doing the body
of the loop_. It separates looping from computing.

For instance, we want to loop over all items in `xs` and `ys`:

```python
for x in xs:
    for y in ys:
        compute(x, y)
```

The code above can be transformed to:

```python
from itertools import product

for x, y in product(xs, ys):
    compute(x, y)
```


Behind the scenes,
[itertool](https://docs.python.org/3.8/library/itertools.html)'s `product`
returns an
[iterator](https://docs.python.org/3/library/stdtypes.html#iterator-types), i.e.
something we can loop over.

Using `product` is both simpler and more general. Now the number of nested loops
can be determined at runtime. It is no longer hard-coded.

```python
>>> from itertools import product
>>> list_of_lists = [[1, 2], [3, 4]]
>>> for args in product(*list_of_lists):
...     print(args)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
>>> list_of_lists = [[1, 2], [3, 4], [5, 6]]
>>> for args in product(*list_of_lists):
...     print(args)
(1, 3, 5)
(1, 3, 6)
(1, 4, 5)
(1, 4, 6)
(2, 3, 5)
(2, 3, 6)
(2, 4, 5)
(2, 4, 6)
```


# Generators: iterators made easy

Generators create iterators using syntax that is similar to the standard loop:

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
          print(f"I am in my_generator {x}, {y}")
```

And then loop with an iterator python creates auto-magically:

```python
>>> for x, y in my_generator([1, 2], ["a", "b"]):
...     print(f"some complicated calculation with {x} and {y}")
some complicated calculation with 1 and a
I am in my_generator 1, a
some complicated calculation with 1 and b
I am in my_generator 1, b
some complicated calculation with 2 and a
I am in my_generator 2, a
some complicated calculation with 2 and b
I am in my_generator 2, b
```

In practice, python runs through the code in `my_generator` and returns a new
element each time it hits yield. The next time it is called, it restarts from
the line _right after_ `yield`.

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
>
> ```python
> def interleaved(xs):
>     for x in xs:
>         yield 2 ** x
>         yield x ** 2
>
> for x in interleaved([2, 4, 3, 2]):
>     print(x)
> ```
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
> What is the output sequence in this case?
>
> ```python
> def sequential(xs):
>
>   for x in xs:
>       yield 2 ** x
>
>   for x in xs:
>       yield x ** 2
>
> for x in sequential([2, 4, 3, 2]):
>     print(x)
> ```
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

## How to use the iterator pattern

What to look for:

- Complex loops
- Complex loops that occur multiple times in the code
- Complex loops that occur multiple times in the code with only
  slight variations

What to do:

Lift the loop into a generator function and make any parameter an input argument
of the generator function.


## Other languages

- c++: create a class with the following methods:
    ```cpp
    class Iterator {
      // pre-increment
      // note: const is optional, but a priori, its a good idea.
      Iterator operator++() const;
      // or post-increment. or both.
      // note: const is optional, but a priori, its a good idea.
      Iterator operator++(int) const;

      // dereference, to access the "yielded" values
      T operator*();
      // optionally, const dereference
      const T operator*() const;

      // comparison to other iterator
      bool operator!=(const Iterator &) const;
    }
    ```
    Then use in loop:
    ```
    for(Iterator i(...), end(...); i != end; ++i)
        compute(*i);
    ```
- R: CRAN package
  [iterators](https://cran.r-project.org/web/packages/iterators/index.html)
- Julia: [iterator interface](https://docs.julialang.org/en/v1/manual/interfaces/#man-interface-iteration-1)
- Fortran: of course not


# Dependency Injection, or how to make algorithms tweakable

It's not unusual to want to change an algorithm, but only in one or two places:

```python
def my_algorithm(some_input):
    obstrucated = red_obstructor(some_input)

    return [
        bewlling.append(uncornify(webby))
        for webby in deconforbulate(obstrucated)
    ]
```

Say that rather than loop over `deconforbulate` objects, you need to loop over
`undepolified` objects.

Here's one *bad* solution:


```python
def my_awful_copy_paste_non_solution(some_input):
    obstrucated = red_obstructor(some_input)
    return [
        bewlling.append(uncornify(webby)) for webby in undepolified(obstrucated)
    ]
```

Here's a slightly better one:

```python
def my_somewhat_better_solution(some_input, is_deconfobulated: bool = True):
    if is_deconfobulated:
      generator = deconforbulate
    else:
      generator = undepolified

    obstrucated = red_obstructor(some_input)
    return [
        bewlling.append(uncornify(webby)) for webby in generator(obstrucated)
    ]
```

But it doesn't scale!

Your supervisor just popped in and  wants you to try and loop over
`unsoupilate`d, `resoupilate`d, and `gunkifucate`d objects, and probably others
as well. Using the pattern above, we have to modify the algorithm each and every
time we add a new tweak.

This scenario is based on multiple past and future real-life stories.

Thankfully, the dependency-injection design pattern can come to the rescue!

```python
from typing import Callable, Optional

def the_bees_knees_solution(some_input, generator: Optional[Callable] = None):
    if generator is None:
        generator = deconforbulate

    obstrucated = red_obstructor(some_input)
    return [
        bewlling.append(uncornify(webby)) for webby in generator(obstrucated)
    ]
```

Now the algorithm is independent of the exact generator (Yay! Separation of
concepts!). It can be used without modification with any generator that takes
`obstrucated`-like objects.

## Other languages

- c++: The tweakable element is any [function
    objects](https://en.cppreference.com/w/cpp/utility/functional) object or
    function. The algorithm takes
    [std::function](https://en.cppreference.com/w/cpp/utility/functional/function)
    as argument (simpler code, faster compilation, possibly slower performance).
    Or use a [template
    argument](https://en.cppreference.com/w/cpp/language/template_parameters)
    (slower compilation, no performance hit, often leads to complicated code).
- R: just pass the function, like in python.
- Julia: just pass the function, like in python.
- Fortran: The Fortran 2003 standard introduced [procedure
  pointers](http://fortranwiki.org/fortran/show/Procedure+pointers). Since it
  has only been 17 years, Fortran 2003 compilers can be patchy, buggy, and
  under-performant. Use at your own risk.


## How to use dependency-injection

What to look for:

- algorithms that have been copy-pasted
- slight variations of the same algorithm

What to do:

- Separate levels of details and concerns in the algorithm
- Write the algorithm as seperate functions/class for each level of details and
  concern
- Identify the "tweakable" concerns that need to be changed easily
- Make the "tweakable" concerns an argument of the algorithm

> ## Iterating over points in a ring
>
> Create an iterator and/or a generator that lifts the loop over points in a
> two-dimensional ring:
>
> Take this code:
>
> ```python
> from math import sqrt
>
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
> and create a generator function `point_in_ring`:
>
> ```python
> for point in points_in_ring(points, radius, width):
>     print(f"Some complicated calculation at {point}")
> ```
>
> At this point, `points_in_ring` uses the [Euclidian
> distance](https://en.wikipedia.org/wiki/Euclidean_distance) to figure out what
> is in the ring. Using dependency-injection, make `points_in_ring` capable of
> using any sensible distance (say the [Manhattan
> norm](https://en.wikipedia.org/wiki/Norm_(mathematics)#Taxicab_norm_or_Manhattan_norm)):
>
> ```python
> def manhattan(point: List[float]) -> float:
>     return sum(abs(x) for x in point)
>
>
> for point in points_in_ring(points, radius, width, norm=manhattan):
>     print(f"Some complicated calculation at {point}")
> ```
>
>
> **NOTE:**
> - `points_in_ring` can be used over and over across the code
> - it is parametrized by radius and width
> - it make the loop self-descriptive
> - it is more memory efficient ([lazy
>   evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation)) than a list
> - it is almost always better than creating and keeping in sync a second list
>    holding only points in a ring (compute is cheap)
> - it makes it possible to test/debug the loop alone, without worrying about
    the compute inside the loop
{: .challenge}

> ## Ring generator
>
> ```python
> from math import sqrt
> from typing import Iterable
>
>
> def points_in_ring(points: Iterable, radius: float, width: float) -> Iterable:
>     inner = radius - 0.5 * width
>     outer = radius + 0.5 * width
>     for point in points:
>         distance = sqrt(point[0] * point[0] + point[1] * point[1])
>         if distance >= inner and distance <= outer:
>             yield point
>
>
> points = [[1, 2], [0, 0], [-2, 0], [-2, 3], [-3, -4], [4, 0], [5, 5]]
>
> for point in points_in_ring(points, radius=3.5, width=1.0):
>     print(f"Some complicated calculation at {point}")
> ```
{: .solution}

> ## Ring generator with tweakable norm
>
> ```python
> from math import sqrt
> from typing import Iterable, List, Optional, Callable
>
>
> def euclidean(point: List[float]) -> float:
>     return sqrt(sum((x * x) for x in point))
>
>
> def manhattan(point: List[float]) -> float:
>     return sum(abs(x) for x in point)
>
>
> def points_in_ring(
>     points: Iterable,
>     radius: float,
>     width: float,
>     norm: Optional[Callable] = None,
> ) -> Iterable:
>     if norm is None:
>         norm = euclidean
>
>     inner = radius - 0.5 * width
>     outer = radius + 0.5 * width
>     for point in points:
>         distance = norm(point)
>         if distance >= inner and distance <= outer:
>             yield point
>
>
> points = [[1, 2], [0, 0], [-2, 0], [-2, 3], [-3, -4], [4, 0], [5, 5]]
>
> for point in points_in_ring(points, radius=3.5, width=1.0, norm=manhattan):
>     print(f"Some complicated calculation at {point}")
> ```
{: .solution}

{% include links.md %}

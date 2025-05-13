---
title: "Structuring code"
teaching: 15
exercises: 10
questions:
- How can we create simpler and more modular codes?
objectives:
- Explain the expression "separation of concerns"
- Explain the expression "levels of abstractions"
- Explain the expression "single responsibility principle"
- Explain the expression "dataflow"
- Analyze an algorithm for levels of abstractions, separable concerns and
  dataflow
- Create focussed, modular algorithms
keypoints:
- Code is read more often than written
- The structure of the code should follow a well written explanation of its
  algorithm
- Separate level of abstractions (or details) in a problem must be reflected in
  the structure of the code, e.g. with separate functions
- Separable concerns (e.g. reading an input file to create X, creating X,
  computing stuff with X, saving results to file) must be reflected in the
  structure of the code
---

# Structuring your code

> ## Nutella Cake: What's wrong in here?
>
> Pour the preparation onto the dough. Wait for it to cool. Once it is cool,
> sprinkle with icing sugar.
>
> The dough is composed of 250g of flour, 125g of butter and one egg yolk. It
> should be blind-baked at 180°C until golden brown.
>
> The preparation consists of 200g of Nutella, 3 large spoonfuls of crème
> fraîche, 2 egg yolks and 20g of butter.
>
> Add the Nutella and the butter to a pot where you have previously mixed the
> crème fraîche, the egg yolk and the vanilla extract. Cook and mix on low heat
> until homogeneous.
>
> The dough, a pâte sablée, is prepared by lightly mixing by hand a pinch of
> salt, 250g of flour and 125g of diced butter until the butter is mostly all
> absorbed. Then add the egg yolk and 30g of cold water. The dough should look
> like coarse sand, thus its name.
>
> Spread the dough into a baking sheet. If using it for a pie with a pre-cooked
> or raw filling, first cook the dough blind at 200°C until golden brown. If the
> dough and filling will be cooked together you can partially blind-cook the
> dough at 180°C for 15mn for added crispiness.
>
> Enjoy! It's now ready to serve!
>
{: .challenge}

Code is often as unreadable as this recipe, which makes things very hard to yourself
and other people working on the code. Luckily, there are some rules and principles
that can be followed to fix this and are a sign of good quality code.

In this lesson we will cover some of them, using the above recipe as an example,
when relevant.

## Separation of concerns

**[Separation of Concerns (SoC)] is a fundamental design principle in software
engineering that involves dividing a program into distinct sections, each addressing
a separate concern. A concern is a specific aspect of functionality, behaviour, or
responsibility within the system.**

One of the first issues with the recipe above was that all the different elements
were mixed up. The ingredients and the different steps of the preparation are all
described together, making it impossible to figure out where to look to find out
what to buy or how to prepare the dough or the filling.

Like the recipe, a piece of code should be split into multiple parts, each of them
dealing with one aspect of the workflow. This makes the code more readable, and also
more reusable, since the different parts could be mixed if their functionality were
clearly separated.

For example, the following code will have clear separation of concerns along the
whole workflow:

```python
def main(filename, value):
  # reading input files is one thing
  data = read_input(filename)

  # creating complex objects is another
  simulator = Simulator(data)

  # compute is still something else
  result = simulator.compute(value)

  # Saving data is another
  save(result)
```

> ## What concerns can you identify in the recipe?
>
> Using the recipe above, what concerns can you identify? Concerns might be nested!
>
> > ## Solution
> >
> > The first obvious separation could be between `Ingredients` and
> > `Preparation`. However, there is also another level between `Dough`
> > and `Filling`, so a possible structure for the concerns could be:
> >
> > - Ingredients
> >   - Dough:
> >     - ...
> >   - Filling:
> >     - ...
> >
> > - Preparation
> >   - Dough:
> >     - ...
> >   - Filling:
> >     - ...
> >   - Finishing
> >
> {: .solution}
>
> > ## Solution 2
> >
> > But there is another, more reusable solution, to separate the
> > `Dough` and the `Filling` first, and then the `Ingredients` and
> > the `Preparation`. This way, the same `Dough` could be used in
> > different cake recipes, and the same for the `Filling`.
> >
> > - Dough
> >   - Ingredients:
> >     - ...
> >   - Preparation:
> >     - ...
> >
> > - Filling
> >   - Ingredients:
> >     - ...
> >   - Preparation:
> >     - ...
> >
> > - Finishing:
> >   - Combine the dough and the filling prepared as above and...
> >
> {: .solution}
{: .challenge}

Sometimes, there are multiple ways of separating the concerns, so
spend some time upfront thinking on the simplest, yet more reusable
solution for your code.

[Separation of Concerns (SoC)]: https://en.wikipedia.org/wiki/Separation_of_concerns

## Levels of abstraction

**[Abstraction] is a concept in computer science and software engineering that involves generalizing concrete details to focus on more important, generic aspects. It helps in managing complexity by hiding implementation details and exposing only the necessary parts.**

Let's consider the following code:

```python
def analyse(input_path):
    data = load_data(input_path)

    # special fix for bad data point
    data[0].x["january"] = 0

    results = process_data(data)
    return results
```

The "special fix" mixes levels of abstraction. Our top level function now depends on
the structure of `data`. If the way data is stored changes (a low level detail) we
now also need to change `analyse` which is a high level function directing the flow
of the program.

The following code encapsulates those low level changes in another function,
honouring the different levels of abstraction.

```python
def analyse(input_path):
    data = load_data(input_path)

    cleaned_data = clean_data(data)

    results = process_data(cleaned_data)
    return results
```

Now our `analyse` function does not need to know anything about the inside workings
of the `data` object.

[Abstraction]: https://www.geeksforgeeks.org/why-are-abstractions-important-in-system-design/

## Single responsibility principle

**The [Single Responsibility Principle (SRP)] states that a class or module should have
only one reason to change, meaning it should have only one responsibility or purpose.
This principle helps in creating more maintainable, reusable, and flexible software
designs.**

This goes into a deeper level than the abstractions described above, and it is probably
the one harder to do right, besides its apparent simplicity. It literally means
that each function or method should do one thing only. This typically means also that
is short, easier to read, to debug and to re-use.

Let's consider the following code. It uses Pandas to load some data from either an Excel
file or a CSV file. In the second case, it also manipulates some columns to make sure
the right ones are there.

```python
def load_data(filename):
    if filename.suffix == ".xlsx":
        data = pd.read_excel(filename, usecols="A:B")

    elif filename.suffix == ".csv":
        data = pd.read_csv(filename)
        data["datetime"] = data["date"] + " " + data["time"]
        data = data.drop(columns=["date", "time"])

    else:
        raise RuntimeError("The file must be an Excel or a CSV file")

    assert data.columns == ["datetime", "value"]
    return data
```

This function is doing too many things despite being just 13 lines long, and might need
to change for several, unrelated reasons. If we work on the separation of concerns, we
will have several functions that:

1. Select how to read the data based on the extension.
1. Read an Excel file
1. Read a CSV file
1. Validate the data structure

```python
def load_data(filename):
    """Select how to load the data based on the file extension."""
    if filename.suffix == ".xlsx":
        data = load_excel(filename)
    elif filename.suffix == ".csv":
        data = load_csv(filename)
    else:
        raise RuntimeError("The file must be an Excel or a CSV file.")
    return data

def load_excel(filename):
    """Loads an Excel file, picking only the first 2 columns."""
    data = pd.read_excel(filename, usecols="A:B")
    validate(data)
    return data

def load_csv(filename):
    """Loads a CSV file, ensuring the date and time are combined."""
    data = pd.read_csv(filename)
    data["datetime"] = data["date"] + " " + data["time"]
    data = data.drop(columns=["date", "time"])
    validate(data)
    return data

def validate(data):
    """Checks that the data has the right structure."""
    assert data.columns == ["datetime", "value"]
```

The overall length of the code is much more, but now each function does a very specific
thing, and only one thing, and well documented. The `load_data` function only needs to
change if more formats are supported. The `load_excel` only if the structure of the
Excel file changes and the same goes for the `load_csv`. And the validate data one, only
changes if there are more or different things to validate. The code becomes cleaner,
easier to read and to re-use.

[Single Responsibility Principle (SRP)]: https://www.geeksforgeeks.org/single-responsibility-in-solid-design-principle/

## Code legibility

Code is often meant to be read by an audience who has either not so much familiarity
with it or has not work on it for a while. This audience is normally future-**you**
reading past-**you**'s code.

For example, given a point with coordinates `point[0]`, `point[1]`, `point[2]`, what do
each of them mean? Does `0` corresponds to `x`, `y`, or `z`? Or is it `r`, `theta` or
`z`? Or something else altogether?

Intelligible code aims to:

- Use descriptive names for variables and functions. The times where names should fit
within 8 characters, and whole lines be less than 72 are long past.
- Avoid sources of confusion (What does index `0` reference?)
- Lessen the cognitive load (Before using `c` don't forget to call the function
`nothing_to_do_with_c` because of historical implementation detail).

Some aspects of code legibility will be sorted - or at least flagged out - by the
formatters and linters already discussed, but others do require a conscious effort by the
developer.

## Use of global variables

While global variables were common in the past, they have become less and less popular
due to the problems they might bring to the code. Avoid the use global variables, when
possible. They make the dataflow complex by essence.

Let's consider the following code:

```python
SOME_GLOBAL_VARIABLE = 42

def compute_a(measurements):
    ...
    result *= SOME_GLOBAL_VARIABLE
    return result
```

Now the result of `compute_a` has a hidden dependency. It's never clear whether
calling it twice with the same input `measurements` will yield the same result, as
`SOME_GLOBAL_VARIABLE` might have changed.

In general make sure that all variables have the most limited scope possible. If
they're only needed within a single function define them there. Wherever
possible treat variables with wide scope as **constants** (or make them actual
constants if your language supports it) so you know they're not being modified
anywhere.

Having said that, there are situations where global variables are needed, or are just
unavoidable. A typical example would be accessing a database. That database is just one,
accessible anywhere in the program, and might change in different places. There is no
way around that, but just make sure that measures are in place to ensure that the state
of the database is known at any given time.


## Mixing IO and creating objects or making calculations

Input and output (IO) operations are tricky because they depend on the state of the system - the input file(s) contents - and change the state of the system - creating
new file(s). They need to be handled with care and, indeed, some pure functional
languages like [Haskell] consider them *dirty* operations because of that.

The general rule is that IO operations should happen within their own functions or
methods, and and just pass their contents around. This is a direct conclusion of the
[Separation of concerns](#separation-of-concerns) principle described above, as applied
to IO operations.

For example, objects that need files to be created are hard to create and re-create,
especially during testing. Make the *contents* of the file an input for the object
creation function, instead of the filename or file object. You might want to use
factory methods to support this approach.

For example, don't do this:

```python
class MyModel
    def __init__(self, some_array):
        self.some_array = array
        # BAD!! Now you need to carry this file around every time you want to
        # instantiate MyModel
        self.aaa = read_aaa("somefile.aaa")
```

Do this instead, so you can instantiate `MyModel` without having the file at hand:

```python
class MyModel
    @classmethod
    def from_file(cls, array, filename):
        aaa = read_aaa(filename)
        return cls(array, aaa)

    def __init__(self, some_array, aaa):
        self.some_array = array
        self.aaa = aaa
```
[Haskell]: https://www.haskell.org/

## Dataflow

Often code is just a sequence of transformations on data, so if we have the
following set of actions:

1. data `measurements` is read from input
1. data `a` and `b` are produced from `measurements`, independently
1. data `result` is produced from `a` and `b`

The code should reflect that structure:

```python
def read_experiment(filename):
    ...
    return measurements

def compute_a(measurements):
    ...
    return a

def compute_b(measurements):
    ...
    return b

def compute_result(a, b):
    ...
    return result
```

1. One function to read `Experiment`
1. One function/class to compute `a`: It takes `measurements` as input and
  returns the result `a`
1. One function/class to compute `b`: It takes `measurements` as input and
  returns the result `b`
1. One function/class to compute `Result`: It takes `a` and `b` as input and
  returns the result `result`:

### Unnecessary arguments and tangled dependencies

What sometimes happens is that there are unnecessary arguments and tangled
dependencies that can make the code harder to understand and, indeed, be a
source of errors.

Look at the following alternative code:

```python
# BAD! Unnecessary arguments. Now result depends on a, b, AND measurements
def compute_result(a, b, measurements):
    pass
```

Did we not say the result depends on `a` and `b` alone? The next programmer to look at
the code (e.g. future you) won't know that. Computing `result` is no longer separate
from `measurements`.

### Modifying an input argument

Some languages are designed so sometimes you don't have any choice but to modify an
input argument. Still, wherever possible avoid doing it because if you do not, other
functions using that input argument will need to know who used it first!

If possible avoid doing this.

```python
def compute_a(measurements):
    measurements[1] *= 2
    ...

def compute_b(measurements):
    some_result = measurements[1] * 0.5
    ...

def compute(measurements):
    compute_a(measurements)
    compute_b(measurements)
    ...
```

If `compute_a` takes place before `compute_b` the result would be different than if it
is the other way around. However, there is no clue in the `compute` function indicating
that is the case.

If you do need to modify the inputs then provide them as outputs of the function, such
that it is clear by successive functions that they are using modified versions of the
inputs.

```python
def compute_a(measurements):
    measurements[1] *= 2
    ...
    return measurements

def compute_b(measurements):
    some_result = measurements[1] * 0.5
    ...
    return some_result

def compute(measurements):
    measurements = compute_a(measurements)
    some_result = compute_b(measurements)
    ...
```

Now it is clear that `compute_b` is using a `measurements` object that has been
outputted by `compute_a` and, therefore, it should expect any changes made by it.

{% include links.md %}

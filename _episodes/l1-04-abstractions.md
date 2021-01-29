---
title: "Structuring code"
teaching: 10
exercises: 20
questions:
- How can we create simpler and more modular codes?
objectives:
- Explain the expression "separation of concerns"
- Explain the expression "levels of abstractions"
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

## Intelligible code?

```yaml
Intelligible: Able to be understood; comprehensible
```

Code is meant to be read by an audience who has infinite knowledge and an
infinite capacity for misunderstanding:

- knows more about general relativity than Einstein
- given a point with coordinate `point[0], point[1], point[2]`, can't remember
  whether whether `0` corresponds to `x`, `y`, or `z`

This audience is future-**you** reading past-**you**'s code.

Intelligible code aims to:

- avoid sources of confusion (what does index `0` reference?)
- lessen the cognitive load (ah! before using `c` don't forget to call the
function `nothing_to_do_with_c` because of historical implementation detail
`z`).

## Levels of abstraction

Scientific papers come with separate levels of details:

- abstract -> abstract concepts and no details
- body -> concrete concepts with some details
- appendix -> details only fit for a Ph.D. student

Similarly, code should be written with a structure separating different
levels of details:

```python
def analyse(input_path):
    data = load_data(input_path)

    # special fix for bad data point
    data[0].x["january"] = 0

    results = process_data(data)
    return results
```

The "special fix" mixes levels of abstraction. Our top level function now
depends on the structure of `data`. If the way data is stored changes (a low
level detail) we now also need to change `analyse` which is a high level
function directing the flow of the program.

## Separable concerns

Scientific papers come with separate sections dealing with separate concerns,
e.g.:

- `introduction` describes prior work
- `section I` describes the experimental setup
- `section II` describes the data analysis methods
- `section III` contains plots and a discussion  of the results

Similarly, code should be written with a structure separating separable
concerns:

```python
def main():
  # reading input files is one thing
  data = read_input(filename)

  # creating complex objects is another
  section_I = SectionI(data)

  # compute is still something else
  result_I = section_I.compute(some_value)

  # Saving data is another
  save(result_I)


def read_input(filename):
  """ Reads input data from file. """
  pass


def save(data, filename="saveme.h5"):
  """ Saves output data to file. """
  pass


class SectionI
  """ Runs experiment """
  def __init__(self, some_array):
      self.some_array = some_array

  def compute(self, y):
      """ Just does compute, nothing more, nothing less. """
      pass
```

In the code above we have made some choices:

- reading input files is separate from creating complex objects
- saving output files is separate from running computations
- objects are created in one go

A few examples of what **not** to do.

### Mixing reading files and creating objects

Objects that do need files to be created are easy to create and re-create,
especially during testing.

```python
class SectionI
    def __init__(self, some_array):
        self.some_array = array
        # BAD!! Now you need to carry this file around every time you want to
        # instantiate SectionI
        self.aaa = read_aaa("somefile.aaa")
```

### Mixing computing stuff and IO

Below, it the compute has a hidden baggage: it can't operate without reading
from file. It's not a pure function of `self`, `b`, and `filename`. Run it
twice with exactly the same `self` and the same `b` and the same `filename`,
and the results might still be different.

It creates file artifacts. Littering is a crime and hidden files are litter.

```python
class SectionI
    def run(self, b, filename="somefile.aaa"):
        # BAD!! hidden dependency on the content of the file
        aaa = read_aaa(filename)
        ...
        # BAD! Compute functions should not litter.
        save(result, "somefile")
        return result
```

### Splitting concerns too far

It's unfortunately common to find objects that need to be created and setup in
several steps. This is an
[anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern) (We'll discuss
patterns in a bit), i.e. something that should be avoided. Creating an object is
one thing and one thing only. It should be fully usable right after creation.

```python
sectionI = SectionI(...)

# BAD! just put the initialization in SectionI.__init__
sectionI.setup(...)
results = sectionI.run(...)
```

> ## Paper vs code
>
> Code should be organized the same way as the paper it will produce. If
> a concept X is described in one section, and concept Y in another, then X
> should be one function or class, and Y another.
>
> That's because the primary purpose of paper and code is to communicate with
> other people, including your future self.
{: .callout}

## Dataflow

A code is a sequence of transformations on data, e.g.:

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

Here are things that should **not** happen:

### Unnecessary arguments and tangled dependencies

Did we not say the result depends on `a` and `b` alone? The next programmer to
look at the code (e.g. future you) won't know that. Computing `result` is no
longer separate from `measurements`.

```python
# BAD! Unnecessary arguments. Now result depends on a, b, experiment
def compute_result(a, b, experiment):
    pass
```

### Modifying an input argument

If possible avoid doing this.

```python
def compute_a(measurements):
    measurements[1] *= 2
    ...

def compute_b(measurements):
    measurements[1] *= 0.5
    ...
```

Now `compute_a` has to take place before `compute_b` because `compute_a` chose
to modify it's argument, and thus `compute_b` was hacked to undo the damage. To
get `b` the data is now forced to flow first through `compute_a`.

Some languages unfortunately are designed so sometimes you don't have any choice
but to modify an input argument. Still, wherever possible avoid doing it.

### Global variables

**NEVER EVER EVER** use global variables. They make the dataflow complex by
essence.

```python
SOME_GLOBAL_VARIABLE = "a"

def compute_a(measurements):

    ...
    result *= SOME_GLOBAL_VARIABLE
    return result
```

Now the result of `compute_a` has a hidden dependency. It's never clear whether
calling it twice with the same input (`measurements`) will yield the same
result.

In general make sure that all variables have the most limited scope possible. If
they're only needed within a single function define them there. Wherever
possible treat variables with wide scope as constants (or make them actual
constants if your language supports it) so you know they're not being modified
anywhere.

> ## Dear Fortran 90 users
>
> Module variables are global. They can be modified anywhere, anytime. It's
> best not to use them.
{: .callout}
>
> ## Disentangling a recipe
>
> Disentangle the recipe below into separable concerns and level of details.
> Ensure the flow of ingredients from transform to transform to final dish is
> clear.
>
> 1. Write the solution as a recipe. Be sure to delete steps and information
>    irrelevant to the recipe. Deleting code is GOOD! (if it's under version
>    control)
> 1. Can you identify different levels of abstractions?
> 1. Can you identify different concerns?
> 1. Can you identify what is data and what are transformations of the data?
> 1. Write the solution as pseudo-code in your favorite language. Pseudo-code
>    doesn't have to run, but it has to make sense. Or write a solution as a
>    diagram, if that's your thing (e.g.
>    [UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language), [Sequence
>    diagram](https://en.wikipedia.org/wiki/Sequence_diagram)).
> 1. Can you spot inconsistencies in the original recipe? That's what happens
>    when code is copy-pasted. Invariably, versions diverge until each has set of
>    unique bugs, as well as bugs in common.
>
>
> ```md
> ### Tarte au Nutella
>
> Poor the preparation onto the dough. Wait for it to cool. Once it is cool,
> sprinkle with icing sugar.
>
> The dough is composed of 250g of flour, 125g of butter and one egg yolk. It
> should be blind-baked at 180°C until golden brown.
>
> The preparations consists of 200g of Nutella, 3 large spoonfuls of crème
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
> ```
>
{: .challenge}

{% include links.md %}

---
title: "Structuring code"
teaching: 10
exercises: 20
questions:
- how can we create simpler and more modular codes?
objectives:
- understand the expression "separation of concerns"
- understand the expression "levels of abstractions"
- understand the expression "dataflow"
- analyze an algorithm for levels of abstractions, seperable concerns and
  dataflow
- create focussed, modular algorithms
keypoints:
- Code is read more often than written
- The structure of the code should follow a well written explanation of it's
  algorithm
- Separate level of abstractions (or details) in a problem must be reflected in
  the structure of the code, e.g. with separate functions
- Separable concerns (e.g. reading an input file to create X, creating X,
  computing stuff with X, saving results to file) must be reflected in the
  structure of the code
---

# Intelligible code?

```yaml
Intelligible: Able to be understood; comprehensible
```

Code is meant to be read by an audience who has infinite knowledge and an
infinite capacity for misunderstanding:

- knows more about general relativity than Einstein
- given a point with coordinate `point[0], point[1], point[2]`, can't remember
  whether whether `0` corresponds to `x`, `y`, or `z`

This audience is future-**you** reading past-**you**'s code.

Intelligible code avoids sources of confusion (what does index `0` reference?)
and lessens the cognitive load (ah! before using `c` don't forget to call the
function `nothing_to_do_with_c` because of historical implementation detail
`z`).

# Structure of Logic

## Levels of abstraction

Scientific papers come with separate levels of details:

- abstract -> abstract concepts and no details
- body -> concrete concepts with some details
- appendix -> details only fit for a Ph.D. student

Similarly, code should be written with a structure separating different
levels of details:

```python
def abstract(config):

  result_I = section_I(config['section I'])
  result_II = section_II(result_I, config['section II'])
  result_IIa = appendix_IIa(result_II)  # BAD!! do not mix levels of details
  return conclusion(result_IIa, config['conclusion'])

def section_I(config):
  low_level_thing_with_a_name = appendix_Ia(config['something'])
  other_thing = section_III(  # BAD!! do not mix levels of details
      low_level_thing_with_a_name)
```

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
def main() -> None:

  # reading input files is one thing
  config = introduction(filename)

  # creating complex objects is another
  section_I = SectionI(config)

  # compute is still something else
  result_I = section_I(some_value)

  # Saving data is not reading from file, it is not creating complex objects, it
  # is not computing anything.
  # It just saves stuff.
  save(data)


def introduction(filename: Text) -> Dict:
  import tensorflow as tf

  config = read_from_toml_file(filename)
  # some sanity check
  if config['x'] not in ('y', 'z'):
      raise ValueError("No you can't do that")

  # some standardization
  config['x'] = tf.constant(config['x'], dtype=config['dtype'])

  return config


def save(data: tf.Tensor, filename: Text = "savme.h5") -> None:
  pass


class SectionI
  def __init__(self, some_array: tf.Tensor):
      self.values = some_array

      # BAD! don't mix reading from file and creating an object
      # Better to pass something_else as an argument
      self.something_else = read_from_csv("myfile.csv")

  def compute(self, y: tf.Tensor) -> tf.Tensor:
    pass
```


**NOTE:** Code should be organized the same way as the paper it will produce. If
a concept X is described in one section, and concept Y in another, then X
should be one function or class, and Y in another.


## Data-flow

A code is a sequence of transformations on data, e.g.:

1. data `Experiment` is read from input
1. data `A` and `B` are produced from `Experiment`, independently
1. data `Result` is produced from `A` and `B`

The code should reflect that structure:

1. One function to read `Experiment`
1. One function/class to create `A`: It takes `Experiment` as input, but **does
   not modify it**
1. One function/class to create `B`: It takes `Experiment` as input, but **does
   not modify it**
1. One function/class to create `Result`: It takes `A` and `B` as input, but
   **does not modify them**. It doesn't even know `Experiment` exists.


As much as possible, functions should not modify their arguments. Modifying
arguments introduces hard-to-remember dependencies on the order functions are
called in.


# Example: a recipe

Disentangle the recipe below into separable concerns and level of details.
Ensure the flow of ingredients from transform to transform to final dish is
clear.

1. Write the solution as a recipe. Be sure to delete steps and information
  irrelevant to the recipe. Deleting code is GOOD! (if it's under version
  control)
1. Write the solution as pseudo-code in your favorite language (pseudo-code
doesn't have to run, but it has to make sense.). If confident, feel free to use
[type annotations](https://docs.python.org/3/library/typing.html) to help
determine the data-flow.

## Recipe: Tarte au Nutella

```
Poor the preparation onto the dough. Wait for it to cool. The dough is composed
of 250g of flour, 125g of butter and one egg yolk. It should be blind-baked at
180°C until golden brown. The preparations consists of 200g of Nutella, 3 large
spoonfuls of crème fraîche, 2 egg yolks and 20g of butter. Add the Nutella and
the butter to a pot where you have previously mixed the crème fraîche, the egg
yolk and the vanilla extract. Cook and mix on low heat until homogeneous. Poor
the preparation onto the dough. Wait for it to cool. Once it is cool, sprinkle
with icing sugar. The dough, a pâte sablée, is prepared by lightly mixing by
hand 250g of flour and 125g of diced butter until the butter is mostly all
absorbed. Then add the egg yolk and 30g of cold water. Don't forget a pinch of
salt! The dough should look like coarse sand, thus it's name. Spread the dough
into a baking sheet. If using it for a pie with a pre-cooked or raw filling,
first cook the dough blind at 200°C until golden brown. If the dough and filling
will be cooked together you can partially blind-cook the dough at 180°C for 15mn
for added crispiness.

Enjoy! It's now ready to serve!
```


{% include links.md %}

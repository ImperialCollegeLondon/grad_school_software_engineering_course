---
title: "Writing unit tests"
teaching: 40
exercises: 60
questions:
  - "What is a unit test?"
  - "How do I write and run unit tests?"
  - "How can I avoid test duplication and ensure isolation?"
  - "How can I run tests automatically and measure their coverage?"
objectives:
  - "Implement effective unit tests using pytest"
  - "Execute tests in Visual Studio Code"
  - "Explain the issues relating to non-deterministic code"
  - "Implement fixtures and test parametrisation using pytest decorators"
  - "Configure git hooks and pytest-coverage"
  - "Apply best-practices when setting up a new Python project"
  - "Recognise analogous tools for other programming languages"
  - "Apply testing to Jupyter notebooks"
keypoints:
  - "Testing is not only standard practice in mainstream software engineering, it also provides distinct benefits for any non-trivial research software"
  - "pytest is a powerful testing framework, with more functionality than Python's built-in features while still catering for simple use cases"
  - "Testing with VS Code is straightforward and encourages good habits (writing tests as you code, and simplifying test-driven development)"
  - "It is important to have a set-up you can use for every project - so that it becomes as routine in your workflow as version control itself"
  - "pytest has a myriad of extensions that are worthy of mention such as Jupyter, benchmark, Hypothesis etc"
  - "Adding unit tests can verify the correctness of software and improve its structure: isolating logical distinct code for testing often involves untangling complex structures"
---

## Introduction

Unit testing validates, in isolation, functionally independent components of a
program.

In this lesson we'll demonstrate how to write and execute unit tests for a
simple scientific code.

This involves making some technical decisions...

### Test frameworks

We'll use [pytest](https://docs.pytest.org/en/latest/) as our test framework.
It's powerful but also user friendly.

For comparison: testing using `assert` statements:

```python
from temperature import to_fahrenheit

assert to_fahrenheit(30) == 86
```

Testing using the built-in `unittest` library:

```python
from temperature import to_fahrenheit
import unittest

class TestTemperature(unittest.TestCase):
    def test_to_farenheit(self):
        self.assertEqual(to_fahrenheit(30), 86)
```

Testing using `pytest`:

```python
from temperature import to_fahrenheit

def test_answer():
    assert to_fahrenheit(30) == 86
```

Why use a test framework?

- Avoid reinventing the wheel - frameworks such as pytest provide lots of
  convenient features (some of which we'll see shortly)
- Standardisation leads to better tooling, easier onboarding etc

Projects that use pytest:

- [numpy](https://github.com/numpy/numpy/blob/master/README.md)
  ([example](https://github.com/numpy/numpy/blob/master/numpy/core/tests/test_umath.py#L220))
- [pandas](https://github.com/pandas-dev/pandas)
- [SciPy](https://github.com/scipy/scipy)
- [Devito](https://github.com/devitocodes/devito/blob/master/README.md)
  ([tests](https://github.com/devitocodes/devito/tree/master/tests))

> ## Learning by example
>
> Reading the test suites of mature projects is a good way to learn about
> testing methodologies and frameworks
{: .callout}

### Code editors

We've chosen [Visual Studio Code](https://code.visualstudio.com/) as our
editor. It's free, open source, cross-platform and has excellent Python (and
pytest) support. It also has built-in Git integration, can be used to edit files
on remote systems (e.g. HPC), and handles Jupyter notebooks (plus many more
formats).

> ## Demonstration of pytest + VS Code + coverage
>
> - Test discovery, status indicators and ability to run tests inline
> - Code navigation ("Go to Definition")
> - The Test perspective and Test Output
> - Maximising coverage (`assert recursive_fibonacci(7) == 13`)
> - Test-driven development: adding and fixing a new test (`test_negative_number`)
{: .callout}

## A tour of pytest

### Checking for exceptions

If a function invocation is expected to throw an exception it can be wrapped
with a pytest `raises` block:

```python
def test_non_numeric_input():
    with pytest.raises(TypeError):
        recursive_fibonacci("foo")
```

### Parametrisation

Similar test invocations can be grouped together to avoid repetition. Note how
the parameters are named, and "injected" by pytest into the test function at
runtime:

```python
@pytest.mark.parametrize("number,expected", [(0, 0), (1, 1), (2, 1), (3, 2)])
def test_initial_numbers(number, expected):
    assert recursive_fibonacci(number) == expected
```

This corresponds to running the _same_ test with _different_ parameters, and is
our first example of a pytest decorator
(`@pytest`). [Decorators](https://realpython.com/primer-on-python-decorators/)
are a special syntax used in Python to modify the behaviour of the function,
without modifying the code of the function itself.

### Skipping tests and ignoring failures

Sometimes it is useful to skip tests (conditionally or otherwise), or ignore
failures (for example if you're in the middle of refactoring some code).

This can be achieved using other `@pytest.mark` annotations e.g.

```python
@pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
def test_linux_only_features():
    ...

@pytest.mark.xfail
def test_unimplemented_code():
    ...
```

> ## Refactoring
>
>[Code refactoring](https://en.wikipedia.org/wiki/Code_refactoring) is "the process
>of restructuring existing computer code without changing its external behavior"
>and is often required to make code more amenable to testing.
{: .callout}

### Fixtures

If multiple tests require access to the same data, or a resource that is
expensive to initialise, then it can be provided via a fixture. These can be
cached by modifying the scope of the fixture. See this example from Devito:

```python
@pytest.fixture
def grid(shape=(11, 11)):
    return Grid(shape=shape)

def test_forward(grid):
    grid.data[0, :] = 1.
    ...

def test_backward(grid):
    grid.data[-1, :] = 7.
    ...
```

This corresponds to providing the _same_ parameters to _different_ tests.

### Tolerances

It's common for scientific codes to perform estimation by simulation or other
means. pytest can check for approximate equality:

```python
def test_approximate_pi():
    assert 22/7 == pytest.approx(math.pi, abs=1e-2)
```

> ## Random numbers
>
> If your simulation or approximation technique depends on random numbers then
> consistently seeding your generator can help with testing. See
> [`random.seed()`][random-seed] for an example or the [pytest-randomly][]
> plugin for a more comprehensive solution.
{: .callout}

[random-seed]: https://docs.python.org/3/library/random.html#random.seed
[pytest-randomly]: https://github.com/pytest-dev/pytest-randomly

### doctest

pytest has automatic integration with the Python's standard
[doctest](https://docs.python.org/3/library/doctest.html) module when invoked
with the `--doctest-modules` argument. This is a nice way to provide examples of
how to use a library, via interactive examples in
[docstrings](https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings):

```python
def recursive_fibonacci(n):
    """Return the nth number of the fibonacci sequence

    >>> recursive_fibonacci(7)
    13
    """
    return n if n <=1 else recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)
```

## Hands-on unit testing

> ## Getting started
>
> ### Setting up our editor
>
> 1. If you haven't already, see the [setup guide](../setup) for instructions on
>    how to install Visual Studio Code and conda.
> 1. Download and extract [this zip file](https://github.com/ImperialCollegeLondon/diffusion/archive/master.zip).
>    If using an ICT managed PC please be sure to do this in your user area on the
>    C: drive i.e. `C:\Users\your_username`
>    - _Note that files placed here are not persistent so you must remember to take
>      a copy before logging out_
> 1. In Visual Studio Code go to **File > Open Folder...** and find the files
>    you just extracted.
> 1. If you see an alert "This workspace has extension recommendations." click
>    **Install All** and then switch back to the **Explorer** perspective by
>    clicking the top icon on the left-hand toolbar
> 1. Open Anaconda Prompt (Windows), or a terminal (Mac or Linux) and run:
>
>    ```bash
>    conda env create --file "path_to_environment.yml"
>    ```
>
>    The `path_to_environment.yml` can be obtained by right-clicking the file
>    name in the left pane of Visual Studio Code and choosing "Copy Path". Be
>    sure to include the quotation marks. Right click on the command line
>    interface to paste.
>
> 1. **Important**: After the environment has been created go to **View
>    \> Command Palette** in VS Code, start typing "Python: Select interpreter"
>    and hit enter. From the list select your newly created environment "diffusion"
>
> ### Running the tests
>
> 1. Open `test_diffusion.py`
> 1. You should now be able to click on **Run Test** above the `test_heat()`
>    function and see a warning symbol appear, indicating that the test is
>    currently failing. You may have to wait a moment for **Run Test** to
>    appear.
> 1. Switch to the **Test** perspective by clicking on the flask icon on the
>    left-hand toolbar. From here you can **Run All Tests**, and **Show Test
>    Output** to view the coverage report (see [Lesson
>    1](../l2-01-testing_overview/) for more on coverage)
> 1. **Important**: If you aren't able to run the test then please ask a
>    demonstrator for help. It is essential for the next exercise.
{: .challenge}

### Introduction to your challenge

You have inherited some buggy code from a previous member of your research group:
it has a unit test but it is currently failing. Your job is to refactor the code
and write some extra tests in order to identify the problem, fix the code and
make it more robust.

The code solves the heat equation, also known as the
["Hello World" of Scientific Computing][heat-equation]. It models transient heat
conduction in a metal rod i.e. it describes the temperature at a distance from
one end of the rod at a given time, according to some initial and boundary
temperatures and the thermal diffusivity of the material:

![Metal Rod](https://raw.githubusercontent.com/betterscientificsoftware/images/master/Blog_0719_HeatEqnBar.png)

[heat-equation]: https://github.com/betterscientificsoftware/hello-heat-equation

The function `heat()` in `diffusion.py` attempts to implement a **step-wise
numerical approximation** via a [finite difference
method](https://en.wikipedia.org/wiki/Finite_difference_method):

![u_{i}^{t+1}=ru_{i+1}^{t}+(1-2r)u_{i}^{t}+ru_{i-1}^{t}](https://latex.codecogs.com/png.latex?u_{i}^{t&plus;1}=ru_{i&plus;1}^{t}&plus;(1-2r)u_{i}^{t}&plus;ru_{i-1}^{t})

This relates the temperature `u` at a specific location `i` and time point `t`
to the temperature at the previous time point and neighbouring locations. `r` is
defined as follows, where `α` is the thermal diffusivity: ![r=\frac{\alpha
\Delta t}{\Delta
x^2}](https://latex.codecogs.com/png.latex?r=\frac{\alpha\Delta&space;t}{\Delta&space;x^2})

We approach this problem by representing `u` as a Python list. Elements within
the list correspond to positions along the rod, `i=0` is the first element,
`i=1` is the second and so on. In order to increment `t` we update `u` in a
loop. Each iteration, according to the finite difference equation above, we
calculate values for the new elements of `u`.

![](../fig/heat_equation_implementation.png)

The `test_heat()` function in `test_diffusion.py` compares this _approximation_
with the _exact_ (analytical) solution for the boundary conditions (i.e. the
temperature of the end being fixed at zero). The test is correct but failing -
indicating that there is a bug in the code.

> ## Testing (and fixing!) the code
>
> Work by yourself or with a partner on these test-driven development tasks. Don't
> hesitate to ask a demonstrator if you get stuck!
>
> ### Separation of concerns
>
> First we'll refactor the code, increasing its modularity. We'll extract the
> code that performs a single time step into a new function that can be verified
> in isolation via a new unit test:
>
> 1. In `diffusion.py` move the logic that updates `u` within the loop in the
>    `heat()` function to a new top-level function:
>
>    ```python
>    def step(u, dx, dt, alpha):
>        …
>    ```
>
>    _Hint: the loop in `heat()` should now look like this:_
>
>    ```python
>    for _ in range(nt - 1):
>        u = step(u, dx, dt, alpha)
>    ```
>
> 2. Run the existing test to ensure that it executes without any Python errors.
>    It should still fail.
> 3. Add a test for our new `step()` function:
>
>    ```python
>    def test_step():
>        assert step(…) == …
>    ```
>
>    It should call `step()` with suitable values for `u` (the temperatures at
>    time `t`), `dx`, `dt` and `alpha`. It should `assert` that the resulting
>    temperatures (i.e. at time `t+1`) match those suggested by the equation
>    above. Use `approx` if necessary.  \_Hint: `step([0, 1, 1, 0], 0.04, 0.02,
>    0.01)` is a suitable invocation. These values will give `r=0.125`. It will
>    return a list of the form `[0, ?, ?, 0]`. You'll need to calculate the
>    missing values manually using the equation in order to compare the expected
>    and actual values.
>
> 4. Assuming that this test fails, fix it by changing the code in the `step()`
>    function to match the equation - correcting the original bug. Once you've
>    done this all the tests should pass.
>
> > ## Solution 1
> >
> > Your test should look something like this:
> >
> > ```python
> > # test_diffusion.py
> > def test_step():
> >     assert step([0, 1, 1, 0], 0.04, 0.02, 0.01) == [0, 0.875, 0.875, 0]
> > ```
> >
> > Your final (fixed!) `step()` function should look like this. The original
> > error was a result of some over-zealous copy-and-pasting.
> >
> > ```python
> > # diffusion.py
> > def step(u, dx, dt, alpha):
> >     r = alpha * dt / dx ** 2
> >
> >     return (
> >         u[:1]
> >         + [
> >             r * u[i + 1] + (1 - 2 * r) * u[i] + r * u[i - 1]
> >             for i in range(1, len(u) - 1)
> >         ]
> >         + u[-1:]
> >     )
> > ```
> >
> {: .solution}
>
> Now we'll add some further tests to ensure the code is more suitable for
> publication.
>
> ### Testing for exceptions
>
> We want the `step()` function to
> [raise](https://docs.python.org/3/tutorial/errors.html#raising-exceptions) an
> [Exception](https://docs.python.org/3/tutorial/errors.html#exceptions) when
> the following [stability condition](https://en.wikipedia.org/wiki/Von_Neumann_stability_analysis)
> _isn't_ met: ![r\leq\frac{1}{2}](https://latex.codecogs.com/png.latex?r\leq\frac{1}{2})
> Add a new test `test_step_unstable`, similar to `test_step` but that invokes
> `step` with an `alpha` equal to `0.1` and expects an `Exception` to be
> raised. Check that this test fails before making it pass by modifying
> `diffusion.py` to raise an `Exception` appropriately.
>
> > ## Solution 2
> >
> > ```python
> > # test_diffusion.py
> > def test_step_unstable():
> >     with pytest.raises(Exception):
> >         step([0, 1, 1, 0], 0.04, 0.02, 0.1)
> >
> > # diffusion.py
> > def step(u, dx, dt, alpha):
> >     r = alpha * dt / dx ** 2
> >
> >     if r > 0.5:
> >         raise Exception
> >
> >     …
> > ```
> >
> {: .solution}
>
> ### Adding parametrisation
>
> Parametrise `test_heat()` to ensure the approximation is valid for some other
> combinations of `L` and `tmax` (ensuring that the stability condition remains
> true).
>
> > ## Solution 3
> >
> > ```python
> > # test_diffusion.py
> > @pytest.mark.parametrize("L,tmax", [(1, 0.5), (2, 0.5), (1, 1)])
> > def test_heat(L, tmax):
> >     nt = 10
> >     nx = 20
> >     alpha = 0.01
> >
> >     …
> > ```
> >
> {: .solution}
>
> After completing these two steps check the coverage of your tests via the Test
> Output panel - it should be 100%.
>
> The full, final versions of [diffusion.py](https://github.com/ImperialCollegeLondon/diffusion/blob/develop/diffusion.py)
> and [test_diffusion.py](https://github.com/ImperialCollegeLondon/diffusion/blob/develop/test_diffusion.py)
> are available on GitHub.
>
> ### Bonus task(s)
>
> - Write a doctest-compatible docstring for `step()` or `heat()`
> - Write at least one test for our currently untested `linspace()` function
>   - _Hint: you may find inspiration in [numpy's test cases][numpy-test-cases],
>     but bear in mind that its [version of linspace][linspace] is more capable
>     than ours._
{: .challenge}

[numpy-test-cases]: https://github.com/numpy/numpy/blob/021163b5e2293286b26d22bdae51305da634e74d/numpy/core/tests/test_function_base.py#L222
[linspace]: https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html

## Advanced topics

### More pytest plugins

- [`pytest-benchmark`](https://pytest-benchmark.readthedocs.io/en/stable/)
  provides a fixture that can transparently measure _and track_ performance
  while running your tests:

```python
def test_fibonacci(benchmark):
    result = benchmark(fibonacci, 7)
    assert result == 13
```

> ## pytest-benchmark example
>
> Demonstration of performance regression via recursive and formulaic approaches
> to Fibonacci calculation
> ([output](https://imperiallondon.sharepoint.com/sites/RSE/Shared%20Documents/Graduate%20School%20RSE%20course/Supplementary%20teaching%20material/Essential%20Software%20Engineering%20for%20Researchers/2020-02%20pytest-benchmark%20output.png))
{: .callout}

- [`pytest-notebook`][pytest-notebook] can check for regressions in your Jupyter
  notebooks (see also [Jupyter CI][jupyter-ci])

[pytest-notebook]: https://pytest-notebook.readthedocs.io/en/latest/
[jupyter-ci]: https://github.com/mwoodbri/jupyter-ci

- [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) provides
  property-based testing, which is useful for verifying edge cases):

```python
from fibonacci import recursive_fibonacci
from hypothesis import given, strategies

@given(strategies.integers())
def test_recursive_fibonacci(n):
    phi = (5 ** 0.5 + 1) / 2
    assert recursive_fibonacci(n) == int((phi ** n - -phi ** -n) / 5 ** 0.5)
```

## Taking testing further

### Testing in other languages

- We've discussed tools and approaches for Python but analogues exist for other languages
- We (the RCS) have had success with:
  - C++: [Catch2](https://github.com/catchorg/Catch2)
  - Fortran: [pFUnit](https://github.com/Goddard-Fortran-Ecosystem/pFUnit)
  - R: [testthat](https://github.com/r-lib/testthat)
- See the Software Sustainability Institute's [Build and Test
  Examples][build-examples] for many more

[build-examples]: https://github.com/softwaresaved/build_and_test_examples

### Further resources

- [`ImperialCollegeLondon/pytest_template_application`][pytest-template]
- [A tried-and-tested workflow for software quality assurance][workflow]
  ([repo](https://gitlab.com/mwoodbri/rse18))
- [Using Git to Code, Collaborate and Share][git-course]
- RCS [courses][rcs-courses] and [clinics][]
- [Research Software Community][community]

[pytest-template]: https://github.com/ImperialCollegeLondon/pytest_template_application
[workflow]: https://doi.org/10.5281/zenodo.1409199
[git-course]: https://www.imperial.ac.uk/study/pg/graduate-school/students/doctoral/professional-development/research-computing-data-science/courses/git-to-code-callobrate-share/
[rcs-courses]: https://wiki.imperial.ac.uk/display/HPC/Courses
[clinics]: https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/support/attend-a-clinic/
[community]: https://www.imperial.ac.uk/computational-methods/rse/

{% include links.md %}

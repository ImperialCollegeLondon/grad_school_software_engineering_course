---
title: "Tools I: Packaging and virtual-environments"
teaching: 4
exercises: 6
questions:
- How to use a package manager to install third party tools and libraries
objectives:
- Use conda to install a reproducible envionment
keypoints:
- There are tens of thousands of python packages
- The choice is between reinventing the square wheel or reusing existing work
- The state of an environment can be stored on a file
- This stored environment is then easy to audit and recreate
---

# Python packages

- There are tens of thousands of python packages
- No need to reinvent the square wheel, it's  already out there
- Contributing to existing packages makes it more likely your work will be
  reused
- Contributing to open-source packages is the best way to learn how to code

# Python virtual environments

* Virtual environments isolate your setup from the rest of the system
* It ensures different project do not interfere with each other
* For instance:
  * a production environment with tried and true version of your software and
    tensorflow 1.15
  * a development environment with shiny stuff and a migration to tensorflow 2.1

# Package managers

Package managers help you install packages. Some help you install virtual environments
as well. Better known python package managers include
[conda](https://docs.conda.io/en/latest/), [pip](www.pip.org), [poetry]()

|                           | conda    | pip | poetry     |
|---------------------------|----------|-----|------------|
|audience                   | research | all | developers |
|manage python packages     | ✅       |  ✅ | ✅         |
|manage non-python packages | ✅       | ❌  | ❌         |
|choose python version      | ✅       | ❌  | ❌         |
|manage virtual envs        | ✅       | ❌  | ✅         |
|easy interface             | ❌       | ✅  | ❌         |
|fast                       | ❌       | ✅  | ✅         |


# Rules to choose a package manager

1. Choose one
1. Stick with it

We chose [conda](https://docs.conda.io/en/latest/) because it is the de-facto
standard in science, and because it natively allows to install libraries such as
[fftw](https://anaconda.org/conda-forge/fftw),
[vtk](https://anaconda.org/conda-forge/vtk), or even, Python, R, and Julia themselves.

It is the de-factor package manager on Imperial's [HPC
cluster](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/support/applications/conda/)
systems.

# Selecting an environment in Visual Studio Code

If you haven't already, see the [setup guide](../setup) for instructions on how
to install Visual Studio (VS) Code.

On Linux and Mac, one option is to first activate conda, and then start VS Code:

```bash
> conda activate name_of_environment
> code .
```

The simplest option for all platforms is to set the interpreter is via the panel
with:

- Cmd + Shift + P, and start typing "Python: Select interpreter"

On all platforms, it is possible to set the python interpreter by editing VS
Code settings. To open settings, choose one of the following:

- mac menu: Code > Preferences > Settings
- windows/linux menu: File > Preferences > Settings
- keyboard shortcut: Cmd + ,
- manually: open .vscode/settings.json

Then add the setting

```json
{
  "python.pythonPath": "Path/to/the/python/executable"
}
```



# Example:

> ## Installing and using an environment
>
> 1. If you haven't already, see the [setup guide](../setup) for instructions
>    on how to install conda.
>
> 1. Create a file `environment.yml`
>
>    ```yaml
>    name: course
>    dependencies:
>      - python>=3.6
>      - flake8
>      - pylint
>      - black
>      - mypy
>      - requests
>      - pip
>      - pip:
>        - -e git+https://github.com/ImperialCollegeLondon/R2T2.git#egg=r2t2
>    ```
>
> 1. Create the conda environment with
>
>    ```bash
>    conda env create -f environment.yml
>    ```
>
>    Windows users will want to start the app `Anaconda Prompt`.
>
>    Linux and Mac users should use a terminal app of their choice. They may see a
>    warning with instructions. Please follow the instructions.
>
> 1. We can now activate the environment:
>
>    ```bash
>    conda activate course
>    ```
> 1. And check python knows about the installed packages:
>
>    ```python
>    import numpy
>    ```
>
>    We expect this to run and not fail.
> 1. Finally, feel free to remove requests, then run
>
>    ```bash
>    conda env update -f environment.yml
>    ```
>
>     and see whether the package has been updated or removed.
{: .challenge}


> ## Installing an editable package
>
> Editable packages are packages that you can modify for development and have python
> immediately recognize your changes.
>
> Look at the last few lines of `environment.yml`. It installs
> [r2t2](https://github.com/ImperialCollegeLondon/R2T2) in *editable* mode. The package
> is automatically downloaded from the web and installed in the subfolder `src/r2t2`.
>
> Try and add `print("Hello!")` to `src/r2t2/r2t2/__init__.py`.
>
> Then start python and do
>
> ```python
> import r2t2
> ```
>
> Your greeting should appear: python did indeed take the modified file into account.
>
> Note that r2t2 was setup as a python package with a standard directory structure and a
> `setup.py` file. It's well worth investing 10mn into transforming a python script into
> a package just to make it a *shareable* development environment.
{: .challenge}


> ## Choosing the installation directory for R2T2
>
> It would be nice if we could choose the directory where the editable package goes,
> i.e. rather than have `r2t2` install in `src/r2t2` we might want to install it
> directly in an `r2t2` subfolder.
>
> Nominally, pip does allow us to do that with
> [--src](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-src).
>
> However, it is not (yet) possible to tell conda to tell to use a given option, as
> highlighted in this [issue](https://github.com/conda/conda/issues/6805). But that's
> where the fun begins, because conda is an open-source effort, *you* could pitch in and
> try and add a feature or any [other](https://github.com/conda/conda/issues). There is
> a lot to learn just from lurking around issues of open-source projects, whether it is
> about the project itself, or even about
> [language](https://github.com/JuliaLang/julia/pull/24990)
> [design](https://github.com/JuliaLang/julia/issues/4774A). There is even more to learn
> from participating.
{: .callout}

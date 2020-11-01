---
title: "Tools I: Packaging and virtual-environments"
teaching: 4
exercises: 6
questions:
- How to use a package manager to install third party tools and libraries
objectives:
- Use conda to install a reproducible environment
keypoints:
- There are tens of thousands of Python packages
- The choice is between reinventing the square wheel or reusing existing work
- The state of an environment can be stored in a file
- This stored environment is then easy to audit and recreate
---

## Python packages

- There are tens of thousands of python packages
- No need to reinvent the square wheel, it's  already out there
- Contributing to existing packages makes it more likely your work will be
  reused
- Contributing to open-source packages is the best way to learn how to code

## Python virtual environments

- Virtual environments isolate your setup from the rest of the system
- It ensures different project do not interfere with each other
- For instance:
  - a production environment with tried and true version of your software and
    tensorflow 1.15
  - a development environment with shiny stuff and a migration to tensorflow 2.1

## Package managers

Package managers help you install packages. Some help you install virtual environments
as well. Better known python package managers include
[conda](https://docs.conda.io/en/latest/), [pip](https://pip.pypa.io/en/stable/),
[poetry](https://python-poetry.org/)

|                           | conda    | pip | poetry     |
|---------------------------|----------|-----|------------|
|audience                   | research | all | developers |
|manage python packages     | ✅       |  ✅ | ✅         |
|manage non-python packages | ✅       | ❌  | ❌         |
|choose python version      | ✅       | ❌  | ❌         |
|manage virtual envs        | ✅       | ❌  | ✅         |
|easy interface             | ❌       | ✅  | ❌         |
|fast                       | ❌       | ✅  | ✅         |

## Rules for choosing a package manager

1. Choose one
1. Stick with it

We chose [conda](https://docs.conda.io/en/latest/) because it is the de facto
standard in science, and because it can natively install libraries such as
[fftw](https://anaconda.org/conda-forge/fftw),
[vtk](https://anaconda.org/conda-forge/vtk), or even Python, R, and Julia
themselves.

It is also the de facto package manager on Imperial's [HPC
cluster](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/support/applications/conda/)
systems.

## Example

> ## Installing and using an environment
>
> 1. If you haven't already, see the [setup guide](../setup) for instructions
>    on how to install conda, Visual Studio Code and Git.
>
> 1. Download this zip archive and extract it. Start Visual Studio Code and
>    select "Open folder..." from the welcome screen. Navigate to the folder
>    created from the archive and press "Select Folder".
>
> 1. From the side-bar select the file `environment.yml`. If you are prompted to
>    install the Visual Studio Code Python extension then do so. The contents of
>    `environment.yml` should match:
>
>    ```yaml
>    name: course
>    dependencies:
>      - python>=3.8
>      - flake8
>      - pylint
>      - black
>      - mypy
>      - requests
>      - pip
>      - pip:
>        - -e git+https://github.com/ImperialCollegeLondon/R2T2.git@main#egg=r2t2
>    ```
>
> 1. Create a new virtual environment using conda:
>
>    **Windows users will want to open the app `Anaconda Prompt` from the Start
>    Menu.**
>
>    **Linux and Mac users should use a terminal app of their choice. You may
>    see a warning with instructions. Please follow the instructions.**
>
>    ```bash
>    conda env create -f [path to environment.yml]
>    ```
>
>    You can obtain `[path to environment.yml]` by right clicking the file tab
>    near the top of Visual Studio Code and selecting "Copy Path" from the
>    drop-down menu. Right click on the window for your command line interface
>    to paste the path.
>
> 1. We can now activate the environment:
>
>    ```bash
>    conda activate course
>    ```
>
> 1. And check python knows about the installed packages. Start a Python
>    interpreter with the command `python` then:
>
>    ```python
>    import requests
>    ```
>
>    We expect this to run and not fail. You can see the location of the
>    installed package with:
>
>    ```python
>    requests.__file__
>    ```
>
>    ```
>    'C:\\ProgramData\\Anaconda3\\envs\\course\\lib\\site-packages\\requests\\__init__.py'
>    ```
>    {: .output}
>
>    The file path you see will vary but note that it is within a directory
>    called `course` that contains the files for the virtual environment you
>    have created. Exit the Python interpreter:
>
>    ```python
>    exit()
>    ```
>
> 1. Finally, feel free to remove requests from `environment.yml`, then run
>
>    ```bash
>    conda env update -f [path to environment.yml]
>    ```
>
>     and see whether the package has been updated or removed.
{: .challenge}

## Selecting an environment in Visual Studio Code

If you haven't already, see the [setup guide](../setup) for instructions on how
to install Visual Studio (VS) Code.

On Linux and Mac, one option is to first activate conda, and then start VS Code:

```bash
> conda activate name_of_environment
> code .
```

The simplest option for all platforms is to set the interpreter is via the
Command Palette:

- For Windows/Linux: Ctrl + Shift + P, and start typing "Python: Select
  interpreter"
- For macOS: Cmd + Shift + P, and start typing "Python: Select interpreter**

**An entry should be present with the name `course`. It may take a few minutes
to appear however.**

If you already have a Python file open then it's also possible to set the
interpreter using the toolbar at the bottom of the window.

> ## Installing an editable package
>
> Editable packages are packages that you can modify for development and have
> python immediately recognize your changes.
>
> Look at the last few lines of `environment.yml`. It installs
> [r2t2](https://github.com/ImperialCollegeLondon/R2T2) in *editable* mode. The
> package is automatically downloaded from the web and installed next to
> `environment.yml` in the subfolder `src/r2t2`.
>
> Try and add `print("Hello!")` to `src/r2t2/r2t2/__init__.py`.
>
> Then start python and do
>
> ```python
> import r2t2
> ```
>
> Your greeting should appear: python did indeed take the modified file into
> account.
>
> Note that r2t2 was setup as a python package with a standard directory
> structure and a `setup.py` file. It's well worth investing 10 minutes into
> transforming a python script into a package just to make it a *shareable*
> development environment.
{: .challenge}
>
> ## Choosing the installation directory for R2T2
>
> It would be nice if we could choose the directory where the editable package
> goes, i.e. rather than have `r2t2` install in `src/r2t2` we might want to
> install it directly in an `r2t2` subfolder.
>
> Nominally, pip does allow us to do that with
> [--src](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-src).
>
> However, it is not (yet) possible to tell conda to tell to use a given option,
> as highlighted in this
> [issue](https://github.com/conda/conda/issues/6805). But that's where the fun
> begins, because conda is an open-source effort, *you* could pitch in and try
> and add a feature or a [fix](https://github.com/conda/conda/issues). There
> is a lot to learn just from lurking around issues of open-source projects,
> whether it is about the project itself, or even about
> [language](https://github.com/JuliaLang/julia/pull/24990)
> [design](https://github.com/JuliaLang/julia/issues/4774A). There is even more
> to learn from participating.
{: .callout}

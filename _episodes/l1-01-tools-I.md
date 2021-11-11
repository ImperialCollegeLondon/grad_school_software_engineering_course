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

## Virtual environments

- Virtual environments isolate a project's setup from the rest of the system
- It ensures different projects do not interfere with each other
- For instance, you may want simultaneously:
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
|manage python packages     | ✅       | ✅  | ✅         |
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
>    on how to install Conda and Visual Studio Code.
>
> 1. Download this [zip archive](../code/course.zip) and extract it. Start Visual
>    Studio Code and select "Open folder..." from the welcome screen. Navigate
>    to the folder created from the archive and press "Select Folder".
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
>    conda env create -f "path_to_environment.yml"
>    ```
>
>    You can obtain `path_to_environment.yml` by right clicking the file tab
>    near the top of Visual Studio Code and selecting "Copy Path" from the
>    drop-down menu. Make sure to include the quotation marks in the
>    command. Right click on the window for your command line interface to paste
>    the path.
>
> 1. We can now activate the environment:
>
>    ```bash
>    conda activate course
>    ```
>
> 1. And check Python knows about the installed packages. Start a Python
>    interpreter with the command `python` then:
>
>    ```python
>    import requests
>    ```
>
>    We expect this to run without any messages. You can see the location of the
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
>    called `course` that contains all of the files for the virtual environment
>    you have created. Exit the Python interpreter:
>
>    ```python
>    exit()
>    ```
>
> 1. Finally, feel free to remove requests from `environment.yml`, then run
>
>    ```bash
>    conda env update -f "path_to_environment.yml"
>    ```
>
>     and see whether the package has been updated or removed.
{: .challenge}

## Selecting an environment in Visual Studio Code

If you haven't already, see the [setup guide](../setup) for instructions on how
to install Visual Studio (VS) Code.

The simplest option for all platforms is to set the interpreter via the Command
Palette:

- For Windows/Linux: Ctrl + Shift + P, and start typing "Python: Select
  interpreter"
- For macOS: Cmd + Shift + P, and start typing "Python: Select interpreter**

**An entry should be present with the name `course`. It may take a few minutes
to appear however.**

If you already have a Python file open then it's also possible to set the
interpreter using the toolbar at the bottom of the window.

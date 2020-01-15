---
title: "Tools III: Packaging and vitual-environments"
teaching: 3
exercises: 2
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

# Rules to choose a package manager

1. Choose one
1. Stick with it

We chose [conda](https://docs.conda.io/en/latest/) because it is the de-facto
standard in science. [pip](https://pypi.org/project/pip/) is the de-facto python
standard for installing packages (but it does help with virtual environments).

[poetry](https://github.com/sdispater/poetry) is a cool new alternative.

# Example:


1. Install the complete [anaconda](https://docs.anaconda.com/anaconda/install/)
  distribution or the smaller
  [miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)

1. Create a file `environment.yml`

  ```yaml
  {% include environment.yml %}
  ```

1. Create the conda environment with

  ```bash
  conda env create -f environment.yml
  ```

  Windows users will want to use [Powershell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7)


{% include links.md %}

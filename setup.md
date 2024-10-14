---
title: Setup
---

Completing this course requires you to have access to computer with some
software prerequisites installed. This course is currently being delivered
remotely so please make sure you have access to a suitable computer. All
attendees should download install the applications Conda, Visual Studio Code and
Git.

> ## Important!
>
> Make sure that you have the most recent versions of Conda and VSCode. Some
> features used in this lesson will not work with older versions.
{: .callout}

## Conda

Conda is a Python distribution and package manager. We use both features to
provide the version of Python that is used in these materials and to setup
self-contained environments.

You can choose to install the full version of [anaconda][] or the more minimal
[miniconda][]. Either is suitable but make sure to choose the Python 3.*
version. If prompted, choose to install only for your user account and do not
install PyCharm.

[anaconda]: https://docs.anaconda.com/anaconda/install/
[miniconda]: https://docs.conda.io/projects/conda/en/latest/user-guide/install/

To test that the installation was successful follow the instructions for your
operating system below.

### Windows

* From the start menu search for and launch `Anaconda Prompt`.
* In the launched window type `conda env list` and press enter.
* You should see output similar to the below.

```bash
# conda environments:
#
base                  *  C:\Users\ccaveayl\AppData\Local\Continuum\anaconda3\
```

### Mac and Linux

* Launch a terminal
* In the launched window type `conda env list` and press enter.
* You should see output similar to the below.

```bash
# conda environments:
#
base                  *  /home/ccaveayl/anaconda3
```

## Visual Studio Code

This course will use Visual Studio (VS) Code as an integrated development
environment (IDE). You may already have a preferred IDE that you use regularly,
however we strongly suggest that you use VS Code for this course and afterwards
replicate the setup as you choose. *If you already have VS Code installed please
make sure it is updated to the latest version.*

To install VS Code follow the instructions
[here](https://code.visualstudio.com).

You should then be able to launch VS Code and see something like:
![Screenshot of VS code](fig/vs-code.png)

## Other languages

This course will focus on Python, but **the general principles and recommendations are
equally applicable to any other programming language used in research**. Throughout the
episodes, we will include indications on what are the equivalent tools and approaches in
other programming languages, such that interested readers can check what they should use 
in those cases.

Some useful links to integrate the R, Fortran and C++ tools that will be mentioned during the
course can be found in:

- **R**: [RStudio](https://posit.co/download/rstudio-desktop/) is a popular IDE that has a set of tools to help you work productively with R (and also Python). If you don't want to download or install anything, then RStudio is also available on [Posit Cloud for free](https://posit.cloud/plans?utm_source=Website&utm_medium=IDE_Download&_gl=1*1owmnjw*_ga*NTgyNzIxNzg5LjE3MTI1ODc0Mzk.*_ga_2C0WZ1JHG0*MTcyODg5NzQ4My4yNi4wLjE3Mjg4OTc0ODMuMC4wLjA.). Alternatively, you can use [R in VSCode](https://code.visualstudio.com/docs/languages/r) (Refer: [R extension](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r)).
- **C++**: [C/C++ VSCode extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools), including a [full tutorial](https://code.visualstudio.com/docs/languages/cpp) on how to set VSCode to work with C++., but for Windows it might be easier to just use Visual Studio.
- **Fortran**: [VSCode Modern Fortran extension](https://fortran-lang.github.io/vscode-fortran-support/), which integrates with the linters and formatters and the Fortran Language Server [fortls](https://fortls.fortran-lang.org/).


{% include links.md %}

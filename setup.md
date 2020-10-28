---
title: Setup
---

Completing this course requires you to have access to computer with some
software prerequisites installed. This course is currently being delivered
remotely so please make sure you have access to a suitable computer. All
attendees should download install the applications Conda, Visual Studio Code and
Git.

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

## Git

Please follow the relevant instructions depending on your operating system.

### Windows


1. Download the Git for Windows [installer](https://git-for-windows.github.io/).
1. Run the installer and follow the steps below:
   1. Click on "Next" four times (two times if you've previously installed Git). You don't need to change anything in the Information, location, components, and start menu screens.
   1. From the dropdown menu select "Use the nano editor by default" and click on "Next".
   1. Ensure that "Git from the command line and also from 3rd-party software" is selected and click on "Next". (If you don't do this Git Bash will not work properly, requiring you to remove the Git Bash installation, re-run the installer and to select the "Git from the command line and also from 3rd-party software" option.)
   1. Ensure that "Use the native Windows Secure Channel library" is selected and click on "Next".
   1. Ensure that "Checkout Windows-style, commit Unix-style line endings" is selected and click on "Next".
   1. Ensure that "Use Windows' default console window" is selected and click on "Next".
   1. Ensure that "Enable file system caching" and "Enable Git Credential Manager" are selected and click on "Next".
   1. Click on "Install".
   1. Click on "Finish".
1. If your "HOME" environment variable is not set (or you don't know what this is):
   1. Open command prompt (Open Start Menu then type `cmd` and press [Enter])
   1. Type the following line into the command prompt window exactly as shown:
   1. `setx HOME "%USERPROFILE%"`
   1. Press [Enter], you should see `SUCCESS: Specified value was saved`.
   1. Quit command prompt by typing `exit` then pressing [Enter]

This will provide you with both Git and Bash via the program Git Bash. You
should be able to launch Git Bash from the Start Menu. Within the window that
launches enter the command `git --version` and press enter. You should see
output similar to the below:
```
git version 2.23.0.windows-1
```

### MacOS

**For OS X 10.9 and higher**, install Git for Mac by downloading and running the
most recent "mavericks" installer from [this list][installer-list]. Because this
installer is not signed by the developer, you may have to right click (control
click) on the .pkg file, click Open, and click Open on the pop up window. After
installing Git, there will not be anything in your `/Applications` folder, as
Git is a command line program. **For older versions of OS X (10.5-10.8)** use
the most recent available installer labelled "snow-leopard" [available
here][snow-leopard].

[installer-list]: http://sourceforge.net/projects/git-osx-installer/files/
[snow-leopard]: http://sourceforge.net/projects/git-osx-installer/files/

To check the installation was successful open the "Terminal" app. In the window
that launches enter the command `git --version` and press enter. You should see
output similar to the below:
```
git version 2.25.0
```

### Linux

If Git is not already available on your machine you can try to install it via
your distributions package manager. For Debian/Ubuntu run `sudo apt-get install
git` and for Fedora run `sudo dnf install git`.

To check the installation was successful open a new terminal. In the window that
launches enter the command `git --version` and press enter. You should see
output similar to the below:
```
git version 2.25.0
```


{% include links.md %}

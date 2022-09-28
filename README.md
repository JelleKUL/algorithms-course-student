# algorithms-course-student
The working files for the Algorithms course taught at the KU Leuven

## Getting Started

### Python

This courses is aimed at teaching you how to develop in Python, so you will need to check if your computer already has a python installation or download the latest version from the website: 

[https://www.python.org/downloads/](https://www.python.org/downloads/)

### Visual studio code

Unless you like to type out every character and have no Idea if what you're doing is correct, you will want a code editor. Programs like these provide very useful features like code completion, error checking and code running. We recommend you use [Visual Studio Code](https://code.visualstudio.com/) which can be installed from here, if you haven't already: 

[https://code.visualstudio.com/](https://code.visualstudio.com/)

### Git

To get the files on your computer, we will use [Git](https://en.wikipedia.org/wiki/Git). Which can be installed via the official website if you haven't already:

[https://git-scm.com/downloads](https://git-scm.com/downloads)


## Cloning the project folder on your machine

After you have installed both Python and Git, it is time to get the files on your folder. This can be done through a command line interface: **Terminal** (Linux or MacOS) or **Command Prompt** (Windows).

1. Open a  new command line window
2. Navigate to your destination folder using:

    ```bash
    > cd "path/to/folder"
    # "cd" stands for "change directory" 
    # Example: 
    # cd "Documents/algorithms"
    ```
3. Clone the project from git:

    ```bash
    > git clone https://github.com/JelleKUL/algorithms-course-student.git
    ```
4. Open your folder in your code editor
5. Start writing your code!

## Setting up a virtual environment

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.

### Installation & Activation
A virtual environment will create a new folder inside the project containing all the depencdancie files. you can choose the name of this folder yourself, but most people call it `env`, so you should probably too. Now that you have your project open in vs code, you can open up a new `Terminal` window from the toolbar and use the following commands to install and run your virtual environment:

#### Windows:
``` bash
# Create the virtual environment
> python3 -m venv env
# Activate the virtual environment
> ./env/Scripts/activate
```

#### Linux/MacOS
``` bash
# Create the virtual environment
> python3 -m venv env
# Activate the virtual environment
> . env/bin/activate
```
### Deactivation

To deactivate you virtual environment simply run:

``` bash
> deactivate
```

But you don't want to do that right now, so if you did, reactivate it.

## Installing Packages

Python is a great coding language, but it can't do everything. Luckily the community has been developing extra code for other to use. These are in the form of `Packages` and they are stored on the Python Package Index or [PyPI](https://pypi.org/).

For example, one of the most popular packages you will need is called [numpy](https://pypi.org/project/numpy/), which can be installed through the terminal window:

``` bash
# use 'pip instal "package-name"' to instal any package in the PyPI registry
> pip install numpy
``` 

Other packages can be installed in a similar manner.

All packages needed for this course are referenced in the requirements.txt file. This makes it very easy to install all of them with a single command:

``` bash
# use 'pip instal -r "file name"' to install all the packages listed in that file
> pip install -r requirements.txt
``` 


## Start Coding

Now you have everything to start your first exercises. Good luck!


## Advanced: Keeping track of your changes

If you would like to save your code, and all the changes you have ever made online, you can do so on Github.
By `Forking` a project, yu create a digital copy of the project where you can make whatever changes you like, check out the following tutorial to learn more:

[How to fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

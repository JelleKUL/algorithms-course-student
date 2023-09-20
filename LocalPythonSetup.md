# How to set up a local python environment on your computer

## Video Tutorial
[![Video tutorial](https://img.youtube.com/vi/XKifbXkIz3w/0.jpg)](https://www.youtube.com/watch?v=XKifbXkIz3w)

## 1. Getting Started

This courses is aimed at teaching you how to develop in python. There are a number of programs you need to install before you can start programming.

### Python

Of course, you need a python installation. Because of some external libraries, we will work in version 3.9. You will need to check if your computer already has a python 3.9 installation or download version 3.9 from the website: 

[https://www.python.org/downloads/](https://www.python.org/downloads/)

> **Note**
> 
> If you already have other versions installed, don't worry, we will use `Virtual environment` to choose which version will be the active python instance

### Visual studio code

Unless you like to type out every character and have no Idea if what you're doing is correct, you will want a code editor. Programs like these provide very useful features like code completion, error checking and code running. We recommend you use [Visual Studio Code](https://code.visualstudio.com/) which can be installed from here, if you haven't already: 

[https://code.visualstudio.com/](https://code.visualstudio.com/)

### Git

To get the files on your computer, we will use [Git](https://en.wikipedia.org/wiki/Git). Which can be installed via the official website if you haven't already:

[https://git-scm.com/downloads](https://git-scm.com/downloads)



## 2. Cloning the project folder on your machine

After you have installed both Python and Git, it is time to get the files on your folder. This can be done in a number of ways, but we recommend using Git to *clone* the project onto your local machine. 

### Using VS Code

Vs code has build in Git features to get you up and running.

1) Open `Visual Studio Code` from the start menu.
2) You will see a welcome page, from the `Start` Section, select `Clone Git Repository`
3) Enter this repository url at the top center input window: 
 
    ```
    https://github.com/JelleKUL/algorithms-course-student.git
    ```
    
    
4) Select where you want to save the folder. (Preferably the `H:` disk, so you can access it everywhere, but on your local machine is also fine.)
5) Open the repository with the bottom-right prompt. (or if you don't see the prompt, click `open folder` in the `Start` section and navigate to your folder.)
6) Proceed to *Setting up a virtual environment*

### Using the CLI

This can also be done through a  CLI or command line interface: **Terminal** (Linux or MacOS) or **Command Prompt** (Windows) if you are not using Visual Studio Code.

1. Open a  new command line window (**Terminal** (Linux or MacOS) or **Command Prompt** (Windows))
2. Navigate to your destination folder using:

    ```bash
    # "cd" stands for "change directory"
    # Make sure to put the path between quotation marks.
    # Example: 
    # cd "Documents/algorithms"
    cd "path/to/folder"
    ```
3. Clone the project from git:

    ```bash
    git clone "https://github.com/JelleKUL/algorithms-course-student.git"
    ```
4. Open your folder in your code editor
5. Proceed to *Setting up a virtual environment*

## 3. Setting up a virtual environment

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.

### Installation & Activation
A virtual environment will create a new folder inside the project containing all the dependency files. you can choose the name of this folder yourself, but most people call it `env`, so you should probably too. 

Now that you have your project open in vs code, you can open up a new `Terminal` window from the toolbar  in the top left of your Visual Studio Code window and use the following commands to install and run your virtual environment:

#### Windows:
Windows does not support running scripts out of the box. To enable this, you will have to activate `Developer Mode` in your system settings and change the `Execution Policy` to allow local scripts to run.

Go to `Settings -> Update & Security -> For Developers` to find these checkboxes.

After that, you can proceed to run the following commands in the terminal:
``` bash
# Create the virtual environment
# "py" is the short hand for python, pointing to the python launcher
# with "-3.9" you can select which version you would like to use for you environment.
py -3.9 -m venv env

# Activate the virtual environment
./env/Scripts/activate
```

> **Warning** **Script execution Error**
> 
> If you still can't execute scripts you need to run the following command in the powershell as an administrator by:
> 1) Search for `powershell` in the start menu.
> 2) right-click the Windows PowerShell icon.
> 3) select `run as administrator`
> 4) Run the following command:
>       ``` bash
>       Set-ExecutionPolicy -ExecutionPolicy AllSigned
>       ```
> 5) Confirm by typing `Y` in the window. 
> 6) Try running the activate command again

> **Warning** **./env/Scripts/activate not found**
>
> If you computer can't find the file to activate the virtual environment, you probably working from the wrong folder.
>   1) The folder listed in the terminal window after `PS` does not match the location of you working directory (should end with `algorithms-course-student`).
>   2) Go to you explorer window and locate your working folder.
>   3) In the top bar, click on the path and copy hte full path.
>   4) Run the following command in the terminal window:
>       ```bash
>       # After `cd`, paste your path between quotation marks.
>       # For example:
>       # cd "C:\Users\u0146408\Documents\algorithms\algorithms-course-student"
>       cd "pasted/path/to/working/folder"
>       ```
>   5) Try running the commands again.


#### Linux/MacOS
``` bash
# Create the virtual environment
python3.9 -m venv env
# Activate the virtual environment
. env/bin/activate
```

### Check for success

Once you see <span style = "color:green">(env)</span> in the front of your terminal line, your environment is active and you can proceed to the next step.

### Deactivation

To deactivate you virtual environment simply run:

``` bash
deactivate
```

But you don't want to do that right now, so if you did, reactivate it.



## 4. Installing Packages

Python is a great coding language, but it can't do everything. Luckily the community has been developing extra code for other to use. These are in the form of `Packages` and they are stored on the Python Package Index or [PyPI](https://pypi.org/).

For example, one of the most popular packages you will need is called [numpy](https://pypi.org/project/numpy/), which can be installed through the terminal window:

``` bash
# use 'pip install "package-name"' to install any package in the PyPI registry
pip install numpy
``` 

Other packages can be installed in a similar manner.

All packages needed for this course are referenced in the requirements.txt file. This makes it very easy to install all of them with a single command:

``` bash
# use 'pip instal -r "file name"' to install all the packages listed in that file
pip install -r requirements.txt
``` 
> **Warning** **Couldn't find a version of *** which qualifies ...**
> 
> This  means there are certain packages in the file that are not compatible with your python version.
> If you encouter this, you will need to make a new `venv` end make sure you use the correct python version **(3.9)**

> **Warning** **Can't find requirements.txt**
>
> Make sure you see the `requirements.txt` file in your document outlier on the left side in vs code.
> Try one of the following fixes:
> 1) Check if your terminal is in the correct working folder: check [Windows](####-Windows) for more info.
> 2) Copy the contents of the file from this github page and paste it in a new file with the same name in your working directory.

## 5. Start Coding

Open the first jupyter notebook file named `chapter1.ipynb` in `chapter1` and try to run the first code block.

> **Warning** **Running Failed**
>
>If you get an error that there is no kernel selected or that certain packages are not installed:
>1) Go to the top right corner where it either states `no kernel` or `python 3.**`
>2) Click on it.
>3) In the top bar, select the python version with `(env)` in front of it.
>4) Try running it again.

If this fails. Try to install the packages independently using:
```bash
pip install matplotlib pandas plotly
```

If you are able to sucessfully run the first code block, you are ready to start coding.

Good luck!

## 6. Documentation

Python and its packages contain a huge amount of functions. No one knows them all by heart, and you won't have to either. 
You can use the pre-written documentation for python and each package during the exam. 
It's a good idea to use them as much as possible during the lessons, so you understand how to navigate them.
Here are the most common documentations you will need:

- `python`: https://docs.python.org/3.9/
    > basic syntax and functions
- `numpy`: https://numpy.org/doc/stable/
    > tools for working with arrays and matrices
- `matplotlib`: https://matplotlib.org/stable/index.html
    > tools for plotting
- `scipy`: https://docs.scipy.org/doc/scipy/
    > tools for more complex maths
- `open3d`: http://www.open3d.org/docs/release/
    > tools for interacting with 3D data (point-clouds, meshes,...)
- `opencv`: https://docs.opencv.org/4.6.0/
    > tools for interacting with images and computer vision
- `pandas`: https://pandas.pydata.org/docs/
    > tools for manipulating cvs and excel files


## 7. Optional: Keeping track of your changes

If you would like to save your code, and all the changes you have ever made online, you can do so on Github.
By `Forking` a project, you create a digital copy of the project where you can make whatever changes you like, check out the following tutorial to learn more:

[How to fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

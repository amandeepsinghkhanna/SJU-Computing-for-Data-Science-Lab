# Computing for Data Science (CDS) Lab

Welcome to the repository for the lab session of Computing for Data Science (CDS) at St. Joseph's University, Bangalore, India. This course is intended for students of the first year MSc. Big Data Analytics. The practical aspects of the course are structured to help the students master basics of Datastructures and Algorithms in the Python programming language. In the repository you'll find code and documentation for the the codebase, algorithms and everything else that can help you in acing the course.

Table of Contents

- [Computing for Data Science (CDS) Lab](#computing-for-data-science-cds-lab)
  - [1. Repository Structure](#1-repository-structure)
  - [2. Hardware and Software Requirements](#2-hardware-and-software-requirements)
    - [2.1. Minimum Hardware Requirements](#21-minimum-hardware-requirements)
    - [2.2. Software Requirements](#22-software-requirements)
      - [2.2.1. Recommended Extensions for Visual Studio Code](#221-recommended-extensions-for-visual-studio-code)
  - [3. Concepts Covered](#3-concepts-covered)
  - [4. Recommended Reading Material](#4-recommended-reading-material)
  - [5. Contributing to the Repository](#5-contributing-to-the-repository)
  - [6. Reporting Errors in Code/Documentation](#6-reporting-errors-in-codedocumentation)

## 1. Repository Structure

The repository is structured in the following format:

```bash
SJU-Computing-for-Data-Science-Lab
|   README.md
|___codebase
|   |___01_datastructures
|   |___02_searching_algorithms
|   |___03_sorting_algorithms
|   |___04_numerical_methods
```

- This is the `README.md` file that you're reading.
- The `codebase` directory contains all the code files for the course.

## 2. Hardware and Software Requirements

### 2.1. Minimum Hardware Requirements

|#|Component|Specification|
|-|-|-|
|1|CPU|Intel: i5 or higher, AMD: Ryzen 5 or higher, Any Apple Silicon|
|2|GPU|Good to have but not required|
|3|HDD|5 GB of free storage|
|4|RAM|8 GB or higher|

- **Note:** *These are the minimum system requirements for a student to effortlessly progress through the lab sessions.*

### 2.2. Software Requirements

Following are the list of softwares required for acing your lab sessions.

|#|Software|Description|
|-|-|-|
|1|Visual Studio Code|A text/code editor that helps us in writing efficient code.|
|2|Notepad++|A text/code editor that helps us in writing efficient code.|
|3|Anaconda|A package manager for Python and R, designed to perform Data Science and Machine Learning|
|4|Git|A version control system for tracking changes in codebase.|

#### 2.2.1. Recommended Extensions for Visual Studio Code

| Extension Name                                  | Description                                                                                                                                                                                                                                                                | Version   | VS Marketplace Link                                                                       |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------|
| Python                                          | Python language support with extension access points for IntelliSense   (Pylance), Debugging (Python Debugger), linting, formatting, refactoring,   unit tests, and more.                                                                                                  | 2024.10.0 | https://marketplace.visualstudio.com/items?itemName=ms-python.python                      |
| Black Formatter                                 | Formatting support for Python files using the Black formatter.                                                                                                                                                                                                             | 2024.2.0  | https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter             |
| JetBrains Mono. A typeface for   developers_ | JetBrains Mono font pack - OpenSource monospaced font with programming   ligatures vscode extension                                                                                                                                                                        | 1.0.2     | https://marketplace.visualstudio.com/items?itemName=NarasimaPandiyan.jetbrainsmono        |
| indent-rainbow                                  | Makes indentation easier to read                                                                                                                                                                                                                                           | 8.3.1     | https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow                |
| Jupyter Notebook Renderers                      | Renderers for Jupyter Notebooks (with plotly, vega, gif, png, svg, jpeg   and other such outputs)                                                                                                                                                                          | 1.0.18    | https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-renderers          |
| Jupyter PowerToys                               | Experimental features for Jupyter notebook support in VS Code.                                                                                                                                                                                                             | 0.1.1     | https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-powertoys   |
| Data Wrangler                                   | Data viewing, cleaning and preparation for tabular datasets                                                                                                                                                                                                                | 1.4.2     | https://marketplace.visualstudio.com/items?itemName=ms-toolsai.datawrangler               |
| Markdown PDF                                    | Convert Markdown to PDF                                                                                                                                                                                                                                                    | 1.5.0     | https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf                    |
| Markdown Math                                   | Adds math support to VS Code's built-in markdown preview.                                                                                                                                                                                                                  | 0.1.0     | https://marketplace.visualstudio.com/items?itemName=koehlma.markdown-math                 |
| QuackTrack Cursor                               | A cute Duck next to Your cursor to ensure Duck debugging more pleasing!                                                                                                                                                                                                    | 1.2.62    | https://marketplace.visualstudio.com/items?itemName=2Guys1Account.quackrack-cursor        |
| Code Spell Checker                              | Spelling checker for source code                                                                                                                                                                                                                                           | 3.0.1     | https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker |
| Path Intellisense                               | Visual Studio Code plugin that autocompletes filenames                                                                                                                                                                                                                     | 2.9.0     | https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense    |
| Auto-Open Markdown Preview                      | Open Markdown preview automatically when opening a Markdown file                                                                                                                                                                                                           | 0.0.4     | https://marketplace.visualstudio.com/items?itemName=hnw.vscode-auto-open-markdown-preview |
| GitLens Git supercharged                    | Supercharge Git within VS Code Visualize code authorship at a glance via Git blame annotations and CodeLens, seamlessly navigate and explore Git   repositories, gain valuable insights via rich visualizations and powerful   comparison commands, and so much more | 15.2.1    | https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens                       |
| Todo Tree                                       | Show TODO, FIXME, etc. comment tags in a tree view                                                                                                                                                                                                                         | 0.0.226   | https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree                 |

## 3. Concepts Covered

The concepts/algorithms covered in the course are broken into four main parts:

1. [Datastructures](./codebase/01_datastructures/README.md)

   1.1. [Stack]()

   1.2. [Queue]()
  
   1.3. [Linked list]()
  
   1.4. [Heap]()
  
   1.5. [Binary Tree]()

2. [Searching Algorithms](./codebase/02_searching_algorithms/README.md)

    2.1. [Linear Search]()

    2.2. [Binary Search]()

3. [Sorting Algorithms](./codebase/03_sorting_algorithms/)

    3.1. [Bubble Sort]()

    3.2. [Selection Sort]()

    3.3. [Quick Sort]()

    3.4. [Merge Sort]()

4. [Numerical Methods](./codebase/04_numerical_methods/README.md)

    4.1. [Newton Raphson]()

    4.2. [Gradient Descent]()

## 4. Recommended Reading Material

|#|Books|
|-|-|
|1|Automate the boring stuff with Python - Al Sweigart|
|2|Learning Python - Mark Lutz|
|3|Classic Computer Scince Problems in Python - David Kopec|

## 5. Contributing to the Repository

To contribute to the codebase, you'll need to follow the Python Enhance Proposal - 8 (PEP - 8) standards found [here](https://peps.python.org/pep-0008/).

Here are contributors of the repository in the alphabetical order:

- [Amandeep Singh Khanna](https://github.com/amandeepsinghkhanna)
- [Syed Hammad](https://github.com/SyedHammad06)

If you enjoy their coding antics, please feel free to follow them on GitHub.

## 6. Reporting Errors in Code/Documentation

To report an issue in the code/documentation please raise an issue in the repository and our team of one person will look into it and fix it at the earliest.

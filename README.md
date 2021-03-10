# Plexus Coding Challange - Water Overflow Problem

## Problem Statement
There is a stack of water glasses in a form of triangle as illustrated. Each glass has a 250ml capacity. When a liquid is poured into the top most glass any
overflow is evenly distributed between the glasses in the next row. That is, half of the overflow pours into the left glass while the remainder of the overflow pours into the right glass.

![water_overflow](/images/water-overflow-problem.png)


Write a program that is able to calculate and illustrate how much liquid is in the `jth` glass of the `ith` row when `k` litres are poured into the top most glass.

# Environment Setup

## Prerequisites
Download an install Python 3.8.5, if not installed go to below link.

`https://www.python.org/downloads/release/python-385/`

## Build Project
1. Clone repo with `git clone https://github.com/sraj50/plexus-challange.git && cd plexus-challenge`
2. Run `make venv` to create virtual environment which creates a `venv` folder in project root directory.
  - Every time, activate the virtal environment to use in command line
    - NOTE: if you used `make venv-<os>`, then the `<env_name>` is named `venv`
    - Unix-like: `cd <project_dir>` then `source ./venv/bin/activate`
    - Windows: `cd <project_dir>` then `./venv/Scripts/activate`
  - In your IDE (PyCharm, Eclipse PyDev), configure the Python intepretor to point to `./venv/bin` or `venv/Scripts`
3. Run `make init` to setup and install dependences.
4. Run `make run ARGS='-i 3 -j 1 -k 3 -v'` to run the project with command line arguments which gives the below output
```
Row 000:  0.25
Row 001:  0.25 0.25
Row 002:  0.25 0.25 0.25
Row 003:  0.16 0.25 0.25 0.16
Row 004:  0.17 0.25 0.17
Row 005:  0.05 0.05
N. Glasses: 15
Total Water: 3.0
Found! Glass (i=3, j=1): 0.25
```

## Make Commands
1. `make init` - setup and install dependencies
2. `make venv-unix` - setup virtual environment for Unix-like systems
3. `make venv-windows` - setup virtual environment for Windows systems
4. `make run ARGS=""` - run the program with command line arguments provided in `ARGS`
5. `make test` - run test suite 

# Analysis

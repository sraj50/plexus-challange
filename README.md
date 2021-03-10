# Plexus Coding Challange - Water Overflow Problem

## Problem Statement
There is a stack of water glasses in a form of triangle as illustrated. Each glass has a 250ml capacity. When a liquid is poured into the top most glass any
overflow is evenly distributed between the glasses in the next row. That is, half of the overflow pours into the left glass while the remainder of the overflow pours into the right glass.

![alt text](https://github.com/sraj50/plexus-challange/tree/develop/images/water-overflow-problem.png "Water Overflow Problem")


Write a program that is able to calculate and illustrate how much liquid is in the j’th glass of the i’th row when K litres are poured into the top most glass.

# Environment Setup

## Prerequisites
Download an install Python 3.8.5, if not installed go to below link.

`https://www.python.org/downloads/release/python-385/`

## Build Project
1. Run `make venv` to create virtual environment which creates a `venv` folder in project root directory.
- On Unix-like systems run `source ./venv/bin/activate` to be in the virtual environment shell.
- In your IDE (PyCharm, Eclipse PyDev), configure the Python intepretor to point to `./venv/bin`
2. Run `make init` to setup and install dependences.
3. Run `make run ARGS='-i 3 -j 1 -k 3'` to run the project.

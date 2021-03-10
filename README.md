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
2. Run `make venv-<os>` to create virtual environment which creates a `venv` folder in project root directory for your OS.
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

## Command Line Interface
Run `make run ARGS='--help'` to show details about parameters.
```
optional arguments:
  -h, --help            show this help message and exit
  -i ROW, --row ROW     Number of rows
  -j COL, --col COL     Number of columns
  -k WATER, --water WATER
                        Amount of liquid in litres to pour into to glass
  -v, --visualise       Show visualisation of tree

```

# Analysis

## Initial Thoughts

### Data Structure
From the problem statement, it can be seen that this type of data structure is similar to a binary tree. However, it is still different from a full binary tree. A full binary is such that each node as either zero children or two children and each child has only one parent.

In this case, a child node has two parents, except the right and left most ndoes, so it is an extention to the binary tree

### Tree Traversal
BFT (Breadth First Traveral) was used to traverse the tree level by level starting from the root node. It has a time complexity of `O(n)` for every `n` node in the tree.

## Assumptions
It is assumed that liquid is poured from the root node and trickles downwards.

## Approach
1. A class `Glass` was created which represents a node in the binary tree. A `Glass` has the following properties:
    - `capacity`: capacity of liquid a glass can hold
    - `water`: amount of liquid in a glass
2. Simulate the "filling" of water from the root node:
    - based on the input of amount of liquid to pour, as long as there is some overflow, the program will continue to create child nodes if they don't exist
    - the child nodes will receive any remaining overflow amount.
3. Linking of children and parent:
    - during the fill process in step 2, as the children are being created, they are linked to their parent.
    - the private functions `_fill_glass`, `_child`, `_create_child` and `link_child` achieves this
4. Finding the water level of a particular node:
    - Breadth First Traversal (BFT) was used to traverse the tree level-by-level
    - during this process, the index (i, j) of each node was mapped using python a `dict` with the key being the coordinates and the value being the glass itself
    - to find a particular node the built-in `dict.get()` was used to find a particular node based on the coordinate

### Pros and Cons
| Pros                                                         | Cons                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Solution is extensible. For example, we could easily simulate what happens if water is poured  into **any** glass, not just the root node. | Not very space efficient. We are storing some data for each glass. |
| Once we simulate it for K-litres of liquid, we can look up the solution to any glass in that particular tree. | Probably not going to hold up well for extremely large inputs. As we are using BFT for traversal and then using dictionary to search the coordinates.|

# from .BinaryTree import BinaryTree
from Glass import Glass
from Overflow import find_glass, map_index

if __name__ == '__main__':
    glass = Glass()
    glass.fill(2)
    find_glass(3, 2, 2)
    d: dict = map_index(glass)
    print(d.get((3, 2)).water)
    # glass.traverse()

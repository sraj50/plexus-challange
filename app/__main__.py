from .BinaryTreeSearch import BinaryTreeSearch

if __name__ == '__main__':
    bst = BinaryTreeSearch()
    bst.insert(12)
    bst.insert(92)
    bst.insert(112)
    bst.insert(123)
    bst.insert(2)
    bst.insert(11)
    bst.insert(53)
    bst.insert(3)
    bst.insert(66)
    bst.insert(10)

    print(str(bst))

    print("Breadth First Traversal")
    bst.breadth_first_traversal()

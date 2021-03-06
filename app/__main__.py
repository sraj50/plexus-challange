from .BinaryTreeSearch import BinaryTreeSearch

if __name__ == '__main__':
    bst = BinaryTreeSearch()
    bst.insert(4)
    bst.insert(1)
    bst.insert(2)
    bst.insert(8)
    bst.insert(3)
    bst.insert(5)
    bst.insert(7)
    bst.insert(10)

    print(str(bst))
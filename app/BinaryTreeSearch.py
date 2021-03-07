from .Glass import Glass


class BinaryTreeSearch:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Glass(value)
        else:
            self.root.insert(value)

    def breadth_first_traversal(self, root=None):
        root = self.root if root is None else root
        to_visit = [root]
        while to_visit:
            current = to_visit.pop(0)
            print(current.data)
            if current.left:
                to_visit.append(current.left)
            if current.right:
                to_visit.append(current.right)

    def __repr__(self):
        return repr(self.root)

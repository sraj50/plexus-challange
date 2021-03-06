from .Glass import Glass


class BinaryTreeSearch:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Glass(value)
        else:
            self.root.insert(value)

    def __repr__(self):
        return repr(self.root)

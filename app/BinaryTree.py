from .Glass import Glass


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Glass(value)
        else:
            self.root.insert(value)

    def breadth_first_search(self, data, root=None):
        root = self.root if root is None else root
        to_visit = [root]
        found = False
        while to_visit:
            current = to_visit.pop(0)
            # print(current.data)
            if current.data == data:
                found = True
                break
            else:
                if current.left_child:
                    to_visit.append(current.left_child)
                if current.right_child:
                    to_visit.append(current.right_child)
        return found

    def __repr__(self):
        return repr(self.root)

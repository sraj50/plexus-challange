from .Glass import Glass


class BinaryTree:
    def __init__(self):
        self.root = None

    def create(self, rows):
        if self.root is None:
            self.root = Glass(1)
        else:
            self.root.create(self.root, rows)

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

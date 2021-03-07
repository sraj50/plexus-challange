from collections import deque


class Glass:
    def __init__(self, value):
        self.left_child: Glass = None
        self.right_child: Glass = None

        self.left_parent: Glass = None
        self.right_parent: Glass = None

        self.value = value

    def create(self, rows):
        q = deque()
        q.append(self)

        i = 0
        while len(q) > 0:
            node = q.popleft()
            if i < rows:
                left_child = node.create_child(left=True)
                right_child = node.create_child(left=False)

                q.append(left_child)
                q.append(right_child)
            i += 1

    def create_child(self, left: bool):
        if left and self.left_child:
            return self.left_child
        elif not left and self.right_child:
            return self.right_child

        return self._create_child(left)

    def _create_child(self, left: bool):
        child = Glass(self.value)

        if left:
            child.right_parent = self
            self.left_child = child
        else:
            child.left_parent = self
            self.right_child = child

        self._link_child(left)
        return child

    def _link_child(self, left: bool):
        parent = self.left_parent if left else self.right_parent
        if parent is None:
            return

        sibling = parent.left_child if left else parent.right_child
        if sibling is None:
            sibling = parent._create_child(left)

        if left:
            sibling.right_child = self.left_child
            self.left_child.left_parent = sibling
        else:
            sibling.left_child = self.right_child
            self.right_child.right_parent = sibling

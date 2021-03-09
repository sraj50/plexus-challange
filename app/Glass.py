from collections import deque


class Glass:
    def __init__(self, capacity: float = 0.25):
        self.left_child: Glass = None
        self.right_child: Glass = None

        self.left_parent: Glass = None
        self.right_parent: Glass = None

        self.capacity: float = capacity
        self.water: float = 0

    def fill(self, k: float):
        q = deque()
        q.append((self, k))

        while len(q) > 0:
            node, water_amount = q.popleft()
            overflow = node.fill_glass(water_amount)
            if overflow > 0:
                left_child = node.create_child(left=True)
                right_child = node.create_child(left=False)

                q.append((left_child, overflow/2))
                q.append((right_child, overflow/2))

    def fill_glass(self, k: float):
        remaining_water = self.capacity - self.water
        overflow = max(0.0, k - remaining_water)
        fill_amount = k - overflow

        self.water += fill_amount
        return overflow

    def create_child(self, left: bool):
        if left and self.left_child:
            return self.left_child
        elif not left and self.right_child:
            return self.right_child

        return self._create_child(left)

    def _create_child(self, left: bool):
        child = Glass(self.capacity)

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

    def traverse(self):
        to_visit = deque()
        to_visit.append(self)

        while len(to_visit) > 0:
            current = to_visit.popleft()
            print(current.water)
            if current.left_child:
                to_visit.append(current.left_child)
            if current.right_child:
                to_visit.append(current.right_child)

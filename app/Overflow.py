from collections import deque
from .Glass import Glass


def find_glass(i: int = 0, j: int = 0, k: float = 0) -> float:
    glass = Glass()
    glass.fill(k)

    if j > i:
        raise Exception(f"j cannot be greater than i for index (i={i}, j={j})")

    index_map: dict = map_index(glass)
    node = index_map.get((i, j))

    if node is None:
        return 0

    print(f"Found! Glass (i={i}, j={j}): {node.water}")
    return node.water


def traversal(glass: Glass) -> list:
    q = deque()
    levels = []
    q.append((glass, 0, True))

    while len(q) > 0:
        node, depth, row_end = q.popleft()

        if node is None:
            continue

        while len(levels) < depth + 1:
            levels.append([])

        level = levels[depth]
        level.append(node)

        entry = (node.left_child, depth + 1, False)
        q.append(entry)

        if row_end:
            entry = (node.right_child, depth + 1, True)
            q.append(entry)
    return levels


def visualise(glass: Glass):
    levels: list = traversal(glass)
    for i, row in enumerate(levels):
        row_num = str(i).zfill(3)
        str_arr = [f"Row {row_num}: "]

        for x in row:
            str_arr.append(f"{x.water}")
        print(" ".join(str_arr))


def map_index(glass: Glass) -> dict:
    levels = traversal(glass)
    d = {}
    for i, row in enumerate(levels):
        for x in row:
            d[(i, row.index(x))] = x
    return d

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
        print(f"Could not find Glass (i={i}, j={j})")
        return 0

    print(f"Found! Glass (i={i}, j={j}): {node.water}")
    return node.water


def traversal(glass: Glass) -> tuple:
    q = deque()
    levels = []
    q.append((glass, 0, True))
    n_glasses = 0
    total_water = 0

    while len(q) > 0:
        node, depth, row_end = q.popleft()

        if node is None:
            continue

        while len(levels) < depth + 1:
            levels.append([])

        level = levels[depth]
        level.append(node)
        total_water += node.water
        n_glasses += 1

        entry = (node.left_child, depth + 1, False)
        q.append(entry)

        if row_end:
            entry = (node.right_child, depth + 1, True)
            q.append(entry)
    return levels, total_water, n_glasses


def visualise(glass: Glass):
    levels, total_water, n_glasses = traversal(glass)
    for i, row in enumerate(levels):
        row_num = str(i).zfill(3)
        str_arr = [f"Row {row_num}: "]

        for x in row:
            str_arr.append(f"{x.water:.2f}")
        print(" ".join(str_arr))
    print(f"N. Glasses: {n_glasses}")
    print(f"Total Water: {total_water}")


def map_index(glass: Glass) -> dict:
    levels, total_water, n_glasses = traversal(glass)
    d = {}
    for i, row in enumerate(levels):
        for x in row:
            d[(i, row.index(x))] = x
    return d

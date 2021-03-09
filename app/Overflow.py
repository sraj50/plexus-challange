from collections import deque
from Glass import Glass


def find_glass(i: int = 0, j: int = 0, k: int = 0):
    root_glass = Glass()
    root_glass.fill(k)

    move_right_steps = j
    move_left_steps = i - j

    if j > i:
        raise Exception(f"j cannot be greater than i for index (i={i}, j={j})")

    n = root_glass
    while move_left_steps > 0:
        n = n.left_child
        if n is None:
            return
        else:
            move_left_steps -= 1

    while move_right_steps > 0:
        n = n.right_child
        if n is None:
            return
        else:
            move_right_steps -= 1

    print(f"Found! Glass (i={i}, j={j}): {n.water}")
    # return n.water


def map_index(glass: Glass) -> dict:
    q = deque()
    levels = []
    q.append((glass, 0, True))
    d = {}

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

    for i, row in enumerate(levels):
        row_num = str(i).zfill(3)
        str_arr = [f"Row {row_num}: "]

        for x in row:
            str_arr.append(f"{x.water}")
            d[(i, row.index(x))] = x
            # x.i_index = i
            # x.j_index = row.index(x)
            # print(f"({x.i_index}, {x.j_index})")
        print(" ".join(str_arr))
    print(d)
    return d

from .context import app

MAX_CAPACITY: float = 0.25


class Data:
    def __init__(self, i: int, j: int, k: float, y: float):
        self.i = i  # i index
        self.j = j  # j index
        self.k = k  # liters of liquid
        self.y = y  # expected output


def test_initialize():
    # pylint: disable=W0612,W0613
    g = app.Glass()
    assert g.capacity == MAX_CAPACITY


def test_fill_below_capacity():
    g = app.Glass()
    g.fill(0.2)
    assert g.water == 0.2


def test_fill_over_capacity():
    g = app.Glass()
    g.fill(0.5)
    assert g.water == MAX_CAPACITY


def test_overflow():
    test_dataset = [
        Data(i=0, j=0, k=0.0, y=0.0),
        Data(i=2, j=1, k=1.0, y=0.125),
        Data(i=2, j=0, k=1.0, y=0.0625),
        Data(i=100, j=5, k=1.0, y=0),
    ]

    for data in test_dataset:
        output = app.find_glass(i=data.i, j=data.j, k=data.k)
        assert data.y == output

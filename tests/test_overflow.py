from .context import app

MAX_CAPACITY: float = 0.25


def test_initialize():
    # pylint: disable=W0612,W0613
    g = app.Glass()
    assert g.capacity == MAX_CAPACITY

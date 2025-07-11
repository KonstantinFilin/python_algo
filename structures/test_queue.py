from queue import Queue
import pytest


def test_push_and_pop():
    s = Queue()

    assert s.is_empty()

    s.push("one")
    s.push("two")
    s.push("three")

    assert not s.is_empty()
    assert s.len() == 3

    i = s.pop()

    assert i == "one"
    assert s.len() == 2

    i2 = s.pop()

    assert i2 == "two"
    assert s.len() == 1

    i3 = s.pop()

    assert i3 == "three"
    assert s.len() == 0
    assert s.is_empty()

    with pytest.raises(IndexError) as ex:
        s.pop()

from stack import *


def test_len_and_append():
    s = Stack()

    assert s.len() == 0
    s.push("item")
    assert s.len() == 1


def test_is_empty():
    s = Stack()

    assert s.is_empty() is True
    s.push("item")
    assert s.is_empty() is False


def test_push_and_pop():
    s = Stack()

    assert s.is_empty()

    s.push("one")
    s.push("two")
    s.push("three")

    assert not s.is_empty()
    assert s.len() == 3

    i = s.pop()

    assert i == "three"
    assert s.len() == 2

    i2 = s.pop()

    assert i2 == "two"
    assert s.len() == 1

    i3 = s.pop()

    assert i3 == "one"
    assert s.len() == 0
    assert s.is_empty()

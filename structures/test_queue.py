from queue import Queue,QueueWithPriority
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


def test_queue_with_priority():
    pq = QueueWithPriority()

    pq.insert('a')
    pq.insert('c', 5)
    pq.insert('z', 10)
    pq.insert('q', -3)
    pq.insert('r', 4)

    assert pq.get_items() == [
        ('a', 1),
        ('c', 5),
        ('z', 10),
        ('q', -3),
        ('r', 4)
    ]

    assert pq.find_minimum() == (3, 'q')
    mn = pq.get_minimum()
    assert mn == 'q'

    assert pq.get_items() == [
        ('a', 1),
        ('c', 5),
        ('z', 10),
        ('r', 4)
    ]

    assert pq.find_minimum() == (0, 'a')
    mn = pq.get_minimum()
    assert mn == 'a'

    assert pq.get_items() == [
        ('c', 5),
        ('z', 10),
        ('r', 4)
    ]

    assert pq.find_maximum() == (1, 'z')
    mx = pq.get_maximum()
    assert mx == 'z'

    assert pq.get_items() == [
        ('c', 5),
        ('r', 4)
    ]
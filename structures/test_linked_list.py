from linked_list import *


def test_linked_list_item():
    lli = LinkedListItem("abc")
    lli0 = LinkedListItem("xyz", lli)
    lli2 = LinkedListItem("qwe")

    assert lli.get_next() is None
    assert not lli.has_next()
    assert lli.get_object() == "abc"
    assert lli0.get_next().get_object() == "abc"

    lli.set_object("def")
    assert lli.get_object() == "def"
    lli.set_next(lli2)
    assert lli.has_next()
    assert lli.get_next().get_object() == "qwe"

    assert lli2.get_object() == "qwe"
    assert lli0.has_next()
    assert not lli2.has_next()
    assert lli0.get_next().get_object() == "def"


def test_linked_list():
    ll = LinkedList()
    lli3 = LinkedListItem("jkl")
    lli2 = LinkedListItem("ghi", lli3)
    lli1 = LinkedListItem("def", lli2)
    lli0 = LinkedListItem("abc", lli1)

    assert ll.len() == 0
    assert ll.is_empty()

    ll.set_head(lli0)

    assert ll.len() == 4
    assert not ll.is_empty()

    items = ll.get_items()

    print(items)

    assert len(items) == 4
    assert items[0].get_object() == "abc"
    assert items[1].get_object() == "def"
    assert items[2].get_object() == "ghi"
    assert items[3].get_object() == "jkl"

    lli4 = LinkedListItem("ooo")
    ll.insert_start(lli4)
    items = ll.get_items()

    print(items)

    assert len(items) == 5
    assert items[1].get_object() == "abc"
    assert items[0].get_object() == "ooo"


def test_linked_list_insert_end():
    ll = LinkedList()
    lli3 = LinkedListItem("jkl")
    lli2 = LinkedListItem("ghi")
    lli1 = LinkedListItem("def", lli2)
    lli0 = LinkedListItem("abc", lli1)

    ll.set_head(lli0)

    items = ll.get_items()

    assert len(items) == 3
    assert items[0].get_object() == "abc"
    assert items[1].get_object() == "def"
    assert items[2].get_object() == "ghi"

    ll.insert_end(lli3)
    items = ll.get_items()

    assert len(items) == 4
    assert items[0].get_object() == "abc"
    assert items[1].get_object() == "def"
    assert items[2].get_object() == "ghi"
    assert items[3].get_object() == "jkl"

    ll.insert_start(LinkedListItem("zzz"))
    items = ll.get_items()

    assert len(items) == 5
    assert items[0].get_object() == "zzz"
    assert items[1].get_object() == "abc"
    assert items[2].get_object() == "def"
    assert items[3].get_object() == "ghi"
    assert items[4].get_object() == "jkl"


def test_get_first_get_next():
    ll = LinkedList()
    lli3 = LinkedListItem("jkl")
    lli2 = LinkedListItem("ghi", lli3)
    lli1 = LinkedListItem("def", lli2)
    lli0 = LinkedListItem("abc", lli1)

    ll.set_head(lli0)
    first = ll.get_first()
    last = ll.get_last()

    assert first.get_object() == "abc"
    assert last.get_object() == "jkl"


def test_linked_list_get_n():
    ll = LinkedList()
    lli3 = LinkedListItem("jkl")
    lli2 = LinkedListItem("ghi", lli3)
    lli1 = LinkedListItem("def", lli2)
    lli0 = LinkedListItem("abc", lli1)

    ll.set_head(lli0)

    n = ll.get_n(0)
    assert n.get_object() == "abc"

    n = ll.get_n(2)
    assert n.get_object() == "ghi"

    n = ll.get_n(3)
    assert n.get_object() == "jkl"


def test_linked_list_search():
    ll = LinkedList()
    lli3 = LinkedListItem("jkl")
    lli2 = LinkedListItem("ghi", lli3)
    lli1 = LinkedListItem("def", lli2)
    lli0 = LinkedListItem("abc", lli1)

    ll.set_head(lli0)

    assert ll.search("abc") == 0
    assert ll.search("def") == 1
    assert ll.search("ghi") == 2
    assert ll.search("jkl") == 3

"""

def test_linked_list_change():
    ll = LinkedList()
    lli3 = LinkedListItem("jkl")
    lli2 = LinkedListItem("ghi", lli3)
    lli1 = LinkedListItem("def", lli2)
    lli0 = LinkedListItem("abc", lli1)

    ll.set_head(lli0)
    items = ll.get_items()

    assert items[0].get_object() == "abc"
    assert items[1].get_object() == "def"
    assert items[2].get_object() == "ghi"
    assert items[3].get_object() == "jkl"

    ll.change(2, 3)
    items = ll.get_items()

    print("C")

    assert items[0].get_object() == "abc"
    assert items[1].get_object() == "def"
    assert items[2].get_object() == "jkl"
    assert items[3].get_object() == "ghi"

    print("D")
"""


def test_linked_list_insert_n():
    ll = LinkedList()
    lli3 = LinkedListItem("jkl")
    lli2 = LinkedListItem("ghi", lli3)
    lli1 = LinkedListItem("def", lli2)
    lli0 = LinkedListItem("abc", lli1)

    ll.set_head(lli0)
    items = ll.get_items()

    assert items[0].get_object() == "abc"
    assert items[1].get_object() == "def"
    assert items[2].get_object() == "ghi"
    assert items[3].get_object() == "jkl"

    ll.insert_n(LinkedListItem("ooo"), 2)
    items = ll.get_items()

    assert items[0].get_object() == "abc"
    assert items[1].get_object() == "def"
    assert items[2].get_object() == "ooo"
    assert items[3].get_object() == "ghi"
    assert items[4].get_object() == "jkl"


def test_linked_list_remove_n():
    ll = LinkedList()
    lli3 = LinkedListItem("jkl")
    lli2 = LinkedListItem("ghi", lli3)
    lli1 = LinkedListItem("def", lli2)
    lli0 = LinkedListItem("abc", lli1)

    ll.set_head(lli0)
    items = ll.get_items()

    assert items[0].get_object() == "abc"
    assert items[1].get_object() == "def"
    assert items[2].get_object() == "ghi"
    assert items[3].get_object() == "jkl"

    ll.remove_n(2)
    items = ll.get_items()

    assert items[0].get_object() == "abc"
    assert items[1].get_object() == "def"
    assert items[2].get_object() == "jkl"

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

    # assert ll.len() == 4
    assert not ll.is_empty()

    items = ll.get_items()

    print(items)

    #assert len(items) == 4
    assert items[0].get_object() == "abc"
    assert items[1].get_object() == "def"
    assert items[2].get_object() == "ghi"
    assert items[3].get_object() == "jkl"

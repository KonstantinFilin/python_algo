class LinkedListItem:
    def __init__(self, obj, nxt=None) -> None:
        self.obj = obj
        self.next = nxt

    def set_next(self, nxt)->None:
        if type(nxt).__name__ != "LinkedListItem":
            raise TypeError("head param must be instance of LinkedListItem class")
        self.next = nxt

    def set_object(self, obj)->None:
        self.obj = obj

    def has_next(self) -> bool:
        return self.next is not None

    def get_next(self):
        return self.next

    def get_object(self):
        return self.obj

    def __str__(self) -> str:
        return str(self.get_object())

    def __repr__(self) -> str:
        return str(self.get_object())


class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def set_head(self, head):
        if type(head).__name__ != "LinkedListItem":
            raise TypeError("head param must be instance of LinkedListItem class")

        self.head = head

    def get_items(self):
        ret = []

        if self.head:
            i = self.head

            while i:
                ret.append(i)
                i = i.get_next()

        return ret

    def len(self):
        return len(self.get_items())

    def is_empty(self):
        return self.head is None

    def insert_start(self, obj):
        if type(obj).__name__ != "LinkedListItem":
            raise TypeError("head param must be instance of LinkedListItem class")

        obj.set_next(self.head)
        self.set_head(obj)

    def insert_end(self, obj):
        if type(obj).__name__ != "LinkedListItem":
            raise TypeError("head param must be instance of LinkedListItem class")

        self.get_last().set_next(obj)

    def insert_n(self, obj, n):
        if n < 0:
            raise IndexError("Element index must be 0 or greater")

        if not self.head:
            raise IndexError("Empty list")

        c = 0
        no = self.head
        no_prev = None

        while no:
            if c == n:
                no_prev.set_next(obj)
                obj.set_next(no)
                return

            c += 1
            no_prev = no
            no = no.get_next()

        raise IndexError(f"Element index must be between 0 and {c - 1}")

    def remove_n(self, n):
        if n < 0:
            raise IndexError("Element index must be 0 or greater")

        if not self.head:
            raise IndexError("Empty list")

        c = 0
        no = self.head
        no_prev = None

        while no:
            if c == n:
                no_prev.set_next(no.get_next())
                return

            c += 1
            no_prev = no
            no = no.get_next()

        raise IndexError(f"Element index must be between 0 and {c - 1}")

    """
    def change(self, i, j):
        if i < 0 or j < 0:
            raise IndexError("Element index must be 0 or greater")

        if not self.head:
            raise IndexError("Empty list")

        c = 0
        no = self.head
        no_prev = None
        item_i_prev = None
        item_i = None
        item_i_next = None
        item_j_prev = None
        item_j = None
        item_j_next = None

        print("A")

        while no:
            if c == i:
                item_i_prev = no_prev
                item_i = no
                item_i_next = no.get_next()

            if c == j:
                item_j_prev = no_prev
                item_j = no
                item_j_next = no.get_next()

            if item_i and item_j:
                break

            c += 1
            no_prev = no
            no = no.get_next()

        if item_i and item_j:
            if item_i_prev:
                item_i_prev.set_next(item_j)
            if item_i_next:
                item_j.set_next(item_i_next)
            if item_j_prev:
                item_j_prev.set_next(item_i)
            if item_j_next:
                item_i.set_next(item_j_next)

        print("B")
"""

    def search(self, obj):
        c = 0
        no = self.head

        while no:
            if no.get_object() == obj:
                return c

            c += 1
            no = no.get_next()

        return -1

    def __str__(self) -> str:
        items = self.get_items()
        ret = []

        for i in items:
            ret.append(str(i.get_object()))

        return ret

    def get_first(self):
        if not self.head:
            raise IndexError("Empty list")

        return self.head

    def get_last(self):
        if not self.head:
            raise IndexError("Empty list")

        n = self.head

        while n.has_next():
            n = n.get_next()

        return n

    def get_n(self, n):
        if n < 0:
            raise IndexError("Element index must be 0 or greater")

        if not self.head:
            raise IndexError("Empty list")

        c = 0
        no = self.head

        while no and c <= n:
            if c == n:
                return no

            c += 1
            no = no.get_next()

        raise IndexError(f"Element index must be between 0 and {c - 1}")
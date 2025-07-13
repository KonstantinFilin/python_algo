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
        pass

    def insert_end(self, obj):
        pass

    def insert_n(self, obj, n):
        pass

    def remove_n(self, obj, n):
        pass

    def change(self, i, j):
        pass

    def search_obj(self, obj):
        pass


from stack import Stack

"""
Operation	Average	Worst case
Search	O(n)	O(n)
Insert	O(1)	O(1)
Delete	O(1)	O(1)
Space complexity
Space	O(n)	O(n)
"""


class Queue(Stack):
    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        item = self.items[0]
        self.items = self.items[1:]
        return item


class QueueWithPriority:
    def __init__(self) -> None:
        self.item_list = []
        self.priority_list = []

    def insert(self, element, priority=1):
        self.item_list.append(element)
        self.priority_list.append(priority)

    def len(self):
        return len(self.item_list)

    def is_empty(self):
        return self.len() == 0

    def find_minimum(self):
        mv = None
        mi = None

        if self.is_empty():
            return -1, None

        for i, p in enumerate(self.priority_list):
            if mv is None or mv > p:
                mv = p
                mi = i

        return mi, self.item_list[mi]

    def get_minimum(self):
        if self.is_empty():
            raise IndexError

        mi, mv = self.find_minimum()

        del self.item_list[mi]
        del self.priority_list[mi]

        return mv

    def find_maximum(self):
        mv = None
        mi = None

        if self.is_empty():
            return -1, None

        for i, p in enumerate(self.priority_list):
            if mv is None or mv < p:
                print(mv, p)
                mv = p
                mi = i

        return mi, self.item_list[mi]

    def get_maximum(self):
        if self.is_empty():
            raise IndexError

        mi, mv = self.find_maximum()

        del self.item_list[mi]
        del self.priority_list[mi]

        return mv

    def get_items(self):
        ret = []

        for i in range(len(self.item_list)):
            ret.append((self.item_list[i], self.priority_list[i]))

        return ret

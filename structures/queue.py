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

class Stack:
    def __init__(self) -> None:
        self.items = []

    def len(self):
        return len(self.items)

    def is_empty(self):
        return self.len() == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        item = self.items[-1]
        self.items = self.items[:-1]
        return item

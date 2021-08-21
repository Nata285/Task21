
class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.items) == 0

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

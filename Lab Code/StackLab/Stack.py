import StackEmptyException as StackEmptyException
import StackFullException as StackFullException

import collections

class Stack:
    def __init__(self, max_size=5):
        #self.top = -1
        self.max_size = max_size  # TODO comment
        #self.items = ["" for x in range(max_size)]  # Fills the stack with ""
        self.items = collections.deque()

    def is_empty(self):
        #return self.top == -1
        return len(self.items) == 0

    def is_full(self):
        #return self.top == self.max_size - 1  # Checks to see if the top item is at the maximum height
        return len(self.items) == self.max_size

    def push(self, item):
        if self.is_full():
            raise StackFullException.StackFullException
        else:
            #self.top = self.top + 1
            self.items.append(item)

    def pop(self):
        if not self.is_empty():
            item_str = self.items[-1]
            self.items.pop()
            return item_str
        else:
            raise StackEmptyException.StackEmptyException

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise StackEmptyException.StackEmptyException

    def size(self):
        return len(self.items)

    def print_stack_up(self):
        if not self.is_empty():
            stack_str = ""
            for item in self.items:
                    stack_str = item + '\n' + stack_str
            return stack_str  # Possibly you will remove this line, this is for running Unit Tests before writing code
        else:
            return "Stack is Empty"
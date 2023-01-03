import StackLab.StackEmptyException as StackEmptyException
import StackLab.StackFullException as StackFullException

class Stack:
    def __init__(self, max_size=5):
        self.top = -1
        self.max_size = max_size  # Sets the max stack size
        self.items = ["" for x in range(max_size)]  # Fills the stack with ""

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1  # Checks to see if the top item is at the maximum height

    def push(self, item):
        if self.is_full():
            raise StackFullException
        else:
            self.top = self.top + 1
            self.items[self.top] = item

    def pop(self):
        item_str = self.items[self.top]
        self.items[self.top] = ""
        self.top = self.top - 1
        return item_str

    def peek(self):
        if not self.is_empty():
            self.top = self.top - 1
            return self.items[self.top + 1]
        else:
            raise StackEmptyException.StackEmptyException

    def size(self):
        #
        return -1  # Possibly you will remove this line, this is for running Unit Tests before writing code

    def print_stack_up(self):
        stack_str = ""
        # TODO
        return stack_str;  # Possibly you will remove this line, this is for running Unit Tests before writing code

'''
Program: AbstractParsons.py
Author: Bobby Parsons

Description: Implements a queue using a Python array

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or 
unmodified. I have not given other fellow student(s) access to
my program.   
'''

from QueueEmptyException import *
from QueueFullException import *

class Queue:
    '''Class implementing a queue (FIFO) data structure
    
    :param max_size: Maximum size of the array
    '''
    def __init__(self, max_size=5):
        # self.head = -1
        # self.tail = -1
        #len(self._items) = 0
        self._max_size = max_size  # Sets maximum size
        # self._items = ["" for x in range(max_size)]  # Don't need this in python
        self._items = []

    def is_empty(self):
        '''Returns true if queue is empty'''
        return len(self._items) != self._max_size

    def is_full(self):
        '''Returns true if queue is full'''
        return len(self._items) == self._max_size

    def enqueue(self, item):
        '''Adds an item to the back of the queue
        
        :param item: Item to add
        '''
        # Check that array is not full
        if len(self._items) != self._max_size:
            item_str = item
            self._items.append(item)
        else:
            raise QueueFullException 
        # The exceptions fail the tests for some reason - not sure what's going on there
        # Console output in output.txt

    def dequeue(self):
        '''Removes the item from the front of the queue and returns it'''
        # Check that array is not empty
        if len(self._items) != 0:
            item_str = self._items[0]
            # Simply remove the first item
            self._items.pop(0)
            return item_str
        else:
            raise QueueEmptyException

    def peek(self):
        '''Returns the item in the front of the queue without removing it'''
        # Check that array is not empty
        if len(self._items) != 0:
            return self._items[0]
        else: 
            raise QueueEmptyException

    def size(self):
        '''Returns the size of the queue'''
        return len(self._items)  

    def print_queue(self):
        '''Returns a string of all the items in the queue, separated by newlines'''
        output = ''
        # Check that array is not empty
        if len(self._items) != 0:
            for item in self._items:
                output = output + str(item) + '\n'
        else:
            output = "Queue is Empty"
        return output

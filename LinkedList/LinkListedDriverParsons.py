'''
Program: LinkListedDriverParsons.py
Author: Bobby Parsons

Description: Contains a python class that implements a linked list
and has a driver to test the class

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or 
unmodified. I have not given other fellow student(s) access to
my program.   
'''

from CanParsons import Can


class OutOfRangeException(Exception):
    pass


class Node():
    def __init__(self, data, next=None):
        self._data = data
        self._next = next

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next):
        self._next = new_next


class LinkedList():
    '''Class for a linked list

    :param init_list: Standard Python List to import
    '''

    def __init__(self, init_list=[]):
        self._curr_pos = 0
        self._size = 0
        #self.data = init_list
        # self.data.append(None) #Append None so we can insert at the end
        self._head_node = None
        self._curr_node = self._head_node

        if init_list != []:
            for item in init_list:
                if self._size == 0:
                    self._head_node = Node(item)
                    self._curr_node = self._head_node
                else:
                    new_node = Node(item)
                    self._curr_node.next = new_node
                    self._curr_node = self._curr_node.next
                self._size = self._size + 1
            # Reset aftewr going through list
            self._curr_node = self._head_node

    @property
    def size(self):
        '''Returns the size of the list'''
        # return len(self.data) - 1 # Subtract the None at the end
        return self._size

    @property
    def pos(self):
        '''Returns the current position within the list'''
        return self._curr_pos

    def get(self):
        '''Gets the value at the current position'''
        return self._curr_node._data

    def forward(self):
        '''Moves the current position in the list forward'''
        # make sure future position isn't beyond the end of the list
        if self._curr_pos + 1 >= self.size:
            raise OutOfRangeException
        else:
            self._curr_pos = self._curr_pos + 1
            self._curr_node = self._curr_node.next

    def edit(self, value):
        '''Edits the value at the current position

        :param value: Value to replace the old value with
        '''
        self._curr_node._data = value

    def ins(self, value):
        '''Inserts a new value after the current position

        :param value: Value to add
        '''
        old_next = self._curr_node._next
        new_next = Node(value, old_next)
        self._curr_node.next = new_next
        self._size = self._size + 1

    def reset(self):
        '''Resets the position back to the head'''
        self._curr_node = self._head_node
        self._curr_pos = 0


if __name__ == "__main__":
    test_array = [Can('Bush\'s', 'Baked Beans', 28.0, 1.98),
                  Can('Green Giant', 'Green Beans', 8.0, .49),
                  Can('Old El Paso', 'Refried Beans', 16.0, 1.0)]

    test_list = LinkedList(test_array)

    for i in range(0, 3):
        test_list.get().print_can()
        try:
            test_list.forward()
        except:
            print('Oops! We overshot! (intentionally)')

    print('=============')

    test_list.reset()
    test_list.ins(Can('Del Monte', 'Pinto Beans', 32.0, 1.97))

    test_list.reset()
    for i in range(0, 4):
        test_list.get().print_can()
        if i < test_list.size - 1:
            test_list.forward()

    print('=============')

    test_list.edit(Can('Old El Paso', 'Refried Beans', 16.0, .75))  # Sale!

    test_list.reset()
    for i in range(0, 4):
        print(test_list.pos, end=': ')
        test_list.get().print_can()
        if i < test_list.size - 1:
            test_list.forward()

    input('Press Any Key')

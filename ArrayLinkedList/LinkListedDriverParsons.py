'''
Program: LinkListedDriverParsons.py
Author: Bobby Parsons

Description: Contains a python class that emulates the behavior of a linked list
and has a driver to test the class

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or 
unmodified. I have not given other fellow student(s) access to
my program.   
'''


class OutOfRangeException(Exception):
    pass

class LinkedList():
    '''Class for a linked list
    
    :param init_list: Standard Python List to import
    '''
    def __init__(self, init_list = []):
        self.curr_pos = 0
        self.data = init_list
        self.data.append(None) #Append None so we can insert at the end

    @property
    def size(self):
        '''Returns the size of the list'''
        return len(self.data) - 1 # Subtract the None at the end

    @property
    def pos(self):
        '''Returns the current position within the list'''
        return self.curr_pos

    def get(self):
        '''Gets the value at the current position'''
        return self.data[self.curr_pos]

    def forward(self):
        '''Moves the current position in the list forward'''
        # make sure future position isn't beyond the end of the list
        if self.curr_pos + 1 >= len(self.data):
            raise OutOfRangeException
        else:
            self.curr_pos = self.curr_pos + 1

    def edit(self, value):
        '''Edits the value at the current position
    
        :param value: Value to replace the old value with
        '''
        # Make sure we aren't editing the None at the end of the list
        if self.curr_pos == len(self.data) - 1:
            raise OutOfRangeException
        else:
            self.data[self.curr_pos] = value

    def ins(self, value):
        '''Inserts a new value at the current position
    
        :param value: Value to add
        '''
        self.data.insert(self.curr_pos, value)

    def reset(self):
        '''Resets the position back to the head'''
        self.curr_pos = 0

if __name__ == "__main__":
    test_list = LinkedList(['test1', 'test2', 'test5'])

    # Test basics
    print(test_list.pos)
    print(test_list.get())
    test_list.forward()

    print(test_list.pos)
    print(test_list.get())
    test_list.forward()

    # Test insertion
    print('===============')
    test_list.ins('test3')
    print(test_list.pos)
    print(test_list.get())
    test_list.forward()

    # Test editing
    print('===============')
    print(test_list.pos)
    print(test_list.get())

    test_list.edit('test4')
    print(test_list.pos)
    print(test_list.get())

    # Test exceptions
    print('===============')
    test_list.forward()
    print(test_list.pos)
    print(test_list.get())
    try:
        test_list.edit('test5')
    except OutOfRangeException:
        print('Task failed successfully')
    try:
        test_list.forward()
    except OutOfRangeException:
        print('Task failed successfully')

    #Test resetting
    print('===============')
    test_list.reset()
    print(test_list.get())
    print(test_list.size)

    input('Press any key')
'''
Program: BinarySearchTreeParsons.py
Author: Bobby Parsons

Description: Implements a binary search tree and uses it on the most popular
baby names in the United States

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or 
unmodified. I have not given other fellow student(s) access to
my program.   
'''

import random

class Node:
    '''Node within a Binary Search Tree.

    :param s_data: String data (sorting is based on this)
    :param i_data: Accompanying integer
    '''
    def __init__(self, s_data, i_data):
        self._s_data = s_data
        self._i_data = i_data
        self._left = None
        self._right = None

    def insert(self, s_data, i_data):
        '''Recursive function for inserting

        :param s_data: String to insert (sorting is based on this)
        :param i_data: Accompanying integer
        '''
        if s_data < self._s_data:
            if self._left == None:
                self._left = Node(s_data, i_data)
            else:
                self._left.insert(s_data, i_data)
        else:
            if self._right == None:
                self._right = Node(s_data, i_data)
            else:
                self._right.insert(s_data, i_data)

    def search(self, s_data):
        '''Recursive function for searching

        :param s_data: String to find
        '''
        if s_data < self._s_data:
            if self._left == None:
                return None
            else:
                return self._left.search(s_data)
        elif s_data > self._s_data:
            if self._right == None:
                return None
            else:
                return self._right.search(s_data)
        else:
            return (self._s_data, self._i_data)

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node


class BST:
    '''Simple Binary Search Tree'''
    def __init__(self):
        self._root_node = None

    def insert(self, s_data, i_data):
        '''Inserts a new string into the tree

        :param s_data: String to insert (sorting is based on this)
        :param i_data: Accompanying integer
        '''
        if self._root_node == None:
            self._root_node = Node(s_data, i_data)
        else:
            self._root_node.insert(s_data, i_data)

    def search(self, s_data):
        '''Searches for a string in the tree

        :param s_data: String to find
        '''
        if self._root_node == None:
            return None
        else:
            return self._root_node.search(s_data)


if __name__ == "__main__":
    boy_array = ['Noah', 'Liam', 'Mason', 'Jacob', 'William',
                 'Ethan', 'James', 'Alexander', 'Michael', 'Benjamin']
    girl_array = ['Emma', 'Olivia', 'Sophia', 'Ava', 'Isabella',
                  'Mia', 'Abigail', 'Emily', 'Charlotte', 'Harper']

    boy_tree = BST()
    girl_tree = BST()

    boy_tree.insert(0, 0)

    for i in range(0, 1000000):
        boy_tree.insert(random.randint(-100000, 100000), i+1)

    # for name in boy_array:
    #     print(boy_tree.search(name))

    print('=======================')

    print(boy_tree.search(120))

    input('Press any key')

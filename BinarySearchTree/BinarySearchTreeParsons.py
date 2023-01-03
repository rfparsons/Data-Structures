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

from queue import Queue
from collections import deque

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

    def __str__(self):
        return '(' + self._s_data + ', ' + str(self._i_data) + ')'


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

    def bfs_traversal(self):
        '''A BFS (Breadth-first search) traversal starts at the root and then
        goes through each node on each layer from left to right.
        '''
        node_queue = Queue()
        level_queue = Queue()
        output_str = ''
        all_none = False

        if self._root_node == None:
            return None
        else:
            level_queue.put(self._root_node)
        
        while not all_none:
            all_none = True
            old_level_queue = level_queue
            level_queue = Queue()
            while not old_level_queue.empty():
                curr_node = old_level_queue.get()
                node_queue.put(curr_node)
                if curr_node.left != None:
                    level_queue.put(curr_node.left)
                    all_none = False
                if curr_node.right != None:
                    level_queue.put(curr_node.right)
                    all_none = False

        while not node_queue.empty():
            curr_node = node_queue.get()
            output_str = output_str + str(curr_node) + ' '

        return output_str
    
    def dfs_traversal(self):
        '''A DFS (Depth-first search) traversal traverses a tree starting 
        with every node on the left side down from the root, and it works its 
        way right after reaching the bottom.

        I was unable to get this function working properly.
        '''

        node_stack = deque()
        visited_nodes = []
        output_str = ''

        if self._root_node == None:
            return None
        else:
            node_stack.append(self._root_node)

        while len(node_stack) > 0:
            curr_node = node_stack[-1]

            if curr_node.left != None and not curr_node.left in visited_nodes:
                node_stack.append(curr_node.left)
            else:
                node_stack.pop()
                if curr_node.right != None:
                    node_stack.append(curr_node.right)

            if curr_node in visited_nodes:
                node_stack.pop()
                if curr_node.right != None:
                    node_stack.append(curr_node.right)
            else:
                output_str = output_str + str(curr_node) + ' '
                visited_nodes.append(curr_node)

        return output_str

if __name__ == "__main__":
    boy_array = ['Noah', 'Liam', 'Mason', 'Jacob', 'William',
                 'Ethan', 'James', 'Alexander', 'Michael', 'Benjamin']
    girl_array = ['Emma', 'Olivia', 'Sophia', 'Ava', 'Isabella',
                  'Mia', 'Abigail', 'Emily', 'Charlotte', 'Harper']

    boy_tree = BST()
    girl_tree = BST()

    for i in range(0, 10):
        boy_tree.insert(boy_array[i], i+1)
        girl_tree.insert(girl_array[i], i+1)

    # for name in boy_array:
    #     print(boy_tree.search(name))

    # print('=======================')

    # for name in girl_array:
    #     print(girl_tree.search(name))

    # print('=======================')

    # print(boy_tree.search("name"))
    # print(boy_tree.search("Bobby"))

    print(boy_tree.bfs_traversal())
    print(girl_tree.dfs_traversal())

    input('Press any key')

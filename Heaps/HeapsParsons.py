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

# Adaped from C++ sample code from https://www.geeksforgeeks.org/binary-heap/
class MinHeap:
    def __init__(self):
        self.arr = []

    def get_min(self):
        return self.arr[0]

    def pop_min(self):
        if len(self.arr) == 0:
            return None
        
        min = self.arr[0]
        self.arr.pop(0)
        self.minHeapify(0)
        return min

    def decrease_key(self, i, val):
        if val > self.arr[i]:
            raise ValueError

        self.arr[i] = val
        while i != 0 and self.arr[self.parent(i)] > self.arr[i]:
            pass


    def insert(self, val):
        pass

    def delete(self, index):
        pass

    def parent(self, i):
        return (i-1)/2

    def left(self, i):
        return (2*i)+1

    def right(self, i):
        return (2*i)+2

    def minHeapify(self, i):
        pass

    def __getitem__(self, i):
        return self.arr[i]

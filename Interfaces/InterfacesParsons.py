'''
Program: InterfacesParsons.py
Author: Bobby Parsons

Description: Uses an interface to declare standard measurements for shapes

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or 
unmodified. I have not given other fellow student(s) access to
my program.   
'''

from abc import ABC, abstractmethod
import math

class Measurements(ABC):
    '''Interface for measurements of a shape'''
    @abstractmethod
    def perimeter(self):
        '''Perimeter of the shape'''
        pass

    @abstractmethod
    def area(self):
        '''Area of the shape'''
        pass

class Rectangle(Measurements):
    '''Class defining a rectangle

    :param length: length of the rectangle
    :param width: width of the rectangle
    '''
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def perimeter(self):
        '''Perimeter of the rectangle'''
        return 2 * (self._length + self._width)

    def area(self):
        '''Area of the rectangle'''
        return self._length * self._width

class Square(Measurements):
    '''Class defining a square

    :param side_length: Length of each side
    '''
    def __init__(self, side_length):
        self._side_length = side_length

    def perimeter(self):
        '''Perimeter of the square'''
        return self._side_length * 4

    def area(self):
        '''Area of the square'''
        return math.pow(self._side_length, 2)

if __name__ == "__main__":
    # Big-O: O(1)
    
    test_rectangle = Rectangle(2, 4)
    test_square = Square(3)

    print(test_rectangle.perimeter())
    print(test_rectangle.area())
    print('-----------------')
    print(test_square.perimeter())
    print(test_square.area())

    input('Press any key')
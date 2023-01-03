'''
Program: DerivedClothingParsons.py
Author: Bobby Parsons

Description: Has classes for pieces of clothing

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or 
unmodified. I have not given other fellow student(s) access to
my program.   
'''


class Clothing():
    '''Class describing a piece of clothing
    
    :param size: Size of the clothing
    :param color: Color of the clothing
    '''

    def __init__(self, size=None, color=None):
        self._size = size
        self._color = color

    def get_size(self):
        '''Returns the size of the clothing'''
        return self._size

    def set_size(self, size):
        '''Sets the size of the clothing
        
        :param size: Size of the clothing
        '''
        self._size = size

    def get_color(self):
        '''Returns the color of the clothing'''
        return self._color

    def set_color(self, color):
        '''Sets the color of the clothing
        
        :param color: Color of the clothing
        '''
        self._color = color

    def __str__(self):
        '''Prints all information about the clothing'''
        return 'clothing [Size=' + str(self._size) + ', Color=' + str(self._color) + ']'

    def wash(self):
        '''Returns instructions on how to wash the clothing'''
        return "Wash in cold water"

    def pack(self):
        '''Returns instructions on how to fold the clothing'''
        return "Fold sleeves in and fold in half"

class Pants(Clothing):
    '''Class describing a pair of pants
    
    :param size: Size of the clothing
    :param color: Color of the clothing
    '''
    def __init__(self, size=None, color=None):
        self._size = size
        self._color = color
        
    def wash(self):
        '''Returns instructions on how to wash the pants'''
        return "Dry clean only"

    def hang(self):
        '''Hangs up the pants'''
        print("Hung up your pants!")

    def __str__(self):
        '''Prints all information about the clothing'''
        return 'pants [Size=' + str(self._size) + ', Color=' + str(self._color) + ']'

class Shirt(Clothing):
    '''Class describing a shirt
    
    :param size: Size of the shirt (can only be 'S', 'M', or 'L')
    :param color: Color of the shirt
    :param sleeves: Length of the sleeves (can only be "short", "long", or "none")
    '''
    def __init__(self, size=None, color=None, sleeves=None):
        if (size == 'S' or size == 'M' or size == 'L' or size == None):
            self._size = size
        else:
            raise ValueError

        self._color = color

        if (sleeves == 'short' or sleeves == 'long' or sleeves == 'none' or sleeves == None):
            self._sleeves = sleeves
        else:
            raise ValueError

    def set_size(self, size):
        '''Sets the size of the clothing
        
        :param size: Size of the clothing
        '''
        if (size == 'S' or size == 'M' or size == 'L'):
            self._size = size
        else:
            raise ValueError

    def get_sleeves(self):
        '''Returns the length of the sleeves'''
        return self._sleeves

    def set_sleeves(self, sleeves):
        '''Sets the length of the sleeves
        
        :param sleeves: Length of the sleeves (can only be "short", "long", or "none")
        '''
        if (sleeves == 'short' or sleeves == 'long' or sleeves == 'none'): 
            self._sleeves = sleeves
        else:
            raise ValueError

    def wash(self):
        '''Returns instructions on how to wash the shirt'''
        return "Dry clean only"

    def hang(self):
        '''Hangs up the shirt'''
        print("Hung up your shirt!")

    def __str__(self):
        '''Prints all information about the clothing'''
        return 'shirt [Size=' + str(self._size) + ', Color=' + str(self._color) + ', Sleeves=' + str(self._sleeves) + ']'


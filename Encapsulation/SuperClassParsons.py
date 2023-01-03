'''
Program: SuperClassParsons.py
Author: Bobby Parsons

Description: Has a class for a piece of clothing and a driver

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

    def wash(self):
        '''Returns instructions on how to wash the clothing'''
        return "Wash in cold water"

    def pack(self):
        '''Returns instructions on how to fold the clothing'''
        return "Fold sleeves in and fold in half"

    def __str__(self):
        '''Prints all information about the clothing'''
        return 'clothing [Size=' + str(self._size) + ', Color=' + str(self._color) + ']'


if __name__ == "__main__":
    # Big-O: O(1) (Would be N if data wasn't hard-coded)

    clothes = []

    clothes.append(Clothing())
    clothes.append(Clothing('medium', 'blue'))
    clothes.append(Clothing('L', 'Black'))

    i = 0
    for clothing in clothes:
        i = i + 1
        print('Clothing ' + str(i) + ': ' + str(clothing))
        print(clothing.wash())
        print(clothing.pack())

    input('Press Any Key')


'''
Program: AbstractParsons.py
Author: Bobby Parsons

Description: Uses an abstract base class to help describe a bicycle

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or 
unmodified. I have not given other fellow student(s) access to
my program.   
'''

from abc import ABC, abstractmethod
import random

class FlatTireException(Exception):
    pass

class Cycle(ABC):
    '''Class describing a cycle of some kind'''

    @abstractmethod
    def __init__(self):
        self._number_of_tires = None
        self._number_of_flats = None

    @abstractmethod
    def ride(self):
        '''Rides the cycle'''
        pass

    @abstractmethod
    def stop(self):
        '''Stops riding the cycle'''
        pass

class Bicycle(Cycle):
    '''Class describing a bicycle'''
    def __init__(self):
        self._number_of_tires = 2
        self._number_of_flats = 0

    def ride(self):
        '''Rides the bicycle'''
        if self._number_of_flats > 0:
            print('Could not ride, you have ' + str(self._number_of_flats) + ' flat tire(s)!')
            raise FlatTireException
        else:
            print('Riding bike!')
    
    def stop(self):
        '''Stops riding the bicycle'''
        print('Stopped riding!')
        flatchance = random.randint(0,5) #probably should invest in new tires if they're flat 1/5 of the time
        if flatchance == 4 and self._number_of_flats < self._number_of_tires:
            self._number_of_flats = self._number_of_flats + 1
            print('Looks like you got a flat tire!')


if __name__ == "__main__":
    # Big-O: O(1)

    bike = Bicycle()
    
    has_flat = False

    while not has_flat:
        try:
            bike.ride()
            bike.stop()
        except FlatTireException:
            has_flat = True

    input('Press any key')
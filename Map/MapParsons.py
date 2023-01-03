'''
Program: MapParsons.py
Author: Bobby Parsons

Description: Implements a map class using a dictionary.

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or 
unmodified. I have not given other fellow student(s) access to
my program.   
'''


class KeyDoesNotExistError(Exception):
    pass


class KeyExistsError(Exception):
    pass


class Map:
    '''Implements a map that can store data in key/value pairs'''
    def __init__(self):
        self._dict = {}

    def has_key(self, key):
        '''Checks to see is a key is in the map

        :param key: Key to check
        '''
        return key in self._dict

    def find_key_value(self, key):
        '''Finds the value associated with a key

        :param key: Key to find
        '''
        if key in self._dict:
            return self._dict[key]
        else:
            raise KeyDoesNotExistError

    def insert_key(self, key, value):
        '''Inserts a new key/value pair into the map

        :param key: Key to insert
        :param value: Value to insert
        '''
        if key in self._dict:
            raise KeyExistsError
        else:
            self._dict[key] = value

    def remove_key(self, key):
        '''Remove key/value pair from the map

        :param key: Key to remove
        '''
        if key in self._dict:
            del self._dict[key]
        else:
            raise KeyDoesNotExistError


if __name__ == "__main__":
    test_map = Map()

    test_map.insert_key('bobbysq@gmail.com', 'Bobby Parsons')
    test_map.insert_key('coolcars1996@hotmail.com', 'Carson Johnson')
    # couldn't think of another fake name and email so here's the new york times
    test_map.insert_key('nytimes@e.newyorktimes.com', 'The New York Times')

    print(test_map.find_key_value('nytimes@e.newyorktimes.com'))
    print(test_map.find_key_value('coolcars1996@hotmail.com'))

    test_map.remove_key('bobbysq@gmail.com')
    test_map.remove_key('coolcars1996@hotmail.com')
    test_map.remove_key('nytimes@e.newyorktimes.com')

    input('Press any key')

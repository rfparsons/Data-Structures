'''
Program: ClothingTests.py
Author: Bobby Parsons

Description: Test driver class for DerivedClothing

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or 
unmodified. I have not given other fellow student(s) access to
my program.   
'''

import DerivedClothingParsons as dc

if __name__ == "__main__":
    # Big-O: O(1)

    test_pants_1 = dc.Pants('large', 'tan')
    test_pants_1.hang()
    print('Test Pants 1: ' + str(test_pants_1))

    print('-----------------------')

    test_pants_2 = dc.Pants()
    test_pants_2.set_color('black')
    test_pants_2.set_size('32')
    print(test_pants_2.get_color())
    print(test_pants_2.get_size())
    print(str(test_pants_2))

    print('-----------------------')

    test_shirt_1 = dc.Shirt('L', 'blue', 'short')
    test_shirt_1.hang()
    print('Test Shirt 1: ' + str(test_shirt_1))

    print('-----------------------')

    test_shirt_2 = dc.Shirt()
    try:
        test_shirt_2.set_size('large')
    except ValueError:
        print('Operation successfully failed')

    try:
        test_shirt_2.set_sleeves('large')
    except ValueError:
        print('Operation successfully failed')

    test_shirt_2.set_size('L')
    test_shirt_2.set_color('gray')
    test_shirt_2.set_sleeves('short')
    print(test_shirt_2.get_color())
    print(test_shirt_2.get_size())
    print(test_shirt_2.get_sleeves())
    print('Test Shirt 2: ' + str(test_shirt_2))

    #input('Press Any Key')

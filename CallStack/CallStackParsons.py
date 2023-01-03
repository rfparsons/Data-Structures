'''
Program: CallStackParsons.py
Author: Bobby Parsons

Description: Uses four methods to demonstrate the call stack

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or 
unmodified. I have not given other fellow student(s) access to
my program.   
'''

def method1():
    print('In method 1')
    method2()
    print('Exiting method 1')

def method2():
    print('In method 2')
    method3()
    print('Exiting method 2')

def method3():
    print('In method 3')
    method4()
    print('Exiting method 3')

def method4():
    print('In method 4')
    method1()
    print('Exiting method 4')

if __name__ == "__main__":
    print('In main method')
    method1()
    print('Exiting main method')
"""
Program: IteratorsParsons.py
Author: Bobby Parsons

Program that creates a list of 10 random numbers and prints them out
"""
import random

ARRAY_SIZE = 10
MIN = 5
MAX = 25

if __name__ == "__main__":
    array = [] # Set up array

    for i in range(0, ARRAY_SIZE): # Fill it with random numbers
        number_to_add = random.randint(MIN, MAX)
        array.append(number_to_add)
    
    for num in array: # Print numbers
        print(num)
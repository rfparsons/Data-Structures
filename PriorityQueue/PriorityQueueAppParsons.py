'''
Program: PriorityQueueAppParsons.py
Author: Bobby Parsons

Description: Uses a priority queue to go through a list of customers

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or 
unmodified. I have not given other fellow student(s) access to
my program.   
'''

import queue
from random import randint

if __name__ == "__main__":
    CUSTOMERS = 10

    customer_list = []
    customer_priorities = queue.Queue()

    customer_queue = queue.PriorityQueue()

    for i in range(0, CUSTOMERS):
        customer_list.append('Customer No. ' + str(i + 1))
        customer_priorities.put(randint(0, 5)) # use queue to make queue

    for customer in customer_list:
        priority = customer_priorities.get()
        customer_queue.put((priority, customer))

    print('Unprioritized list:')

    for customer in customer_list:
        print(customer)

    print('Prioritized queue:')

    while not customer_queue.empty():
        print(customer_queue.get())

    input('Press any key')
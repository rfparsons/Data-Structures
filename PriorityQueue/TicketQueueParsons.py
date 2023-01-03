'''
Program: TicketQueueParsons.py
Author: Bobby Parsons

Description: Uses a queue to simulate a literal queue of customers purchasing tickets

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or 
unmodified. I have not given other fellow student(s) access to
my program.   
'''

from random import randint
from queue import Queue


def generate_customer_queue(customers):
    '''Generates the queue of customers lining up to buy between 1 and 4 tickets

    :param customers: Number of customers in the queue
    '''
    customer_queue = Queue(maxsize=customers)

    for i in range(0, customers):
        tickets = randint(1, 4)
        customer_queue.put(tickets)

    return customer_queue


def run_round(tickets):
    '''Runs a round of the simulation.

    :param tickets: Number of tickets available
    '''
    customers = randint(1, 1000)
    customer_queue = generate_customer_queue(customers)
    available_tickets = tickets

    for i in range(0, customers):
        available_tickets = available_tickets - customer_queue.get()
        if available_tickets < 0:
            print('Ran out of all ' + str(tickets) +
                  ' tickets with ' + str(customers) + ' customers.')
            print(str(i) + ' customers managed to get tickets.')
            break

    if available_tickets > 0:
        print('Went through all ' + str(customers) + ' customers with ' +
              str(available_tickets) + ' tickets remaining.')


if __name__ == "__main__":
    run_round(10)
    run_round(100)
    run_round(1000)

    input('Press any key')

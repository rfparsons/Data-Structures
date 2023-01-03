'''
Program: PriorityQueueParsons.py
Author: Bobby Parsons

Description: Implements a priority queue

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or 
unmodified. I have not given other fellow student(s) access to
my program.   
'''

from queue import Queue


class QueueEmptyException(Exception):
    pass


class Node:
    '''Node storing a job number and priority.

    :param job: 4-digit job number
    :param priority: Job priority
    '''
    VALID_PRIORITIES = 'ABCD'

    def __init__(self, job, priority):
        if 9999 >= job >= 1:
            self._job = job
        else:
            raise ValueError

        # if priority == 'A' or priority == 'B' or priority == 'C' or priority == 'D':
        if len(priority) == 1 and priority in self.VALID_PRIORITIES:
            self._priority = priority
        else:
            raise ValueError

    @property
    def job(self):
        return self._job

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, new_priority):
        if len(new_priority) == 1 and new_priority in self.VALID_PRIORITIES:
            self._priority = new_priority
        else:
            raise ValueError


class PriorityQueue:
    '''A priority queue.'''
    def __init__(self):
        self._internal_queue = Queue()

    def add_job(self, job, priority):
        '''Adds a job to the queue. Valid priorities are letters A-D, with A
        being the highest priority.

        :param job: 4-digit job number
        :param priority: Job priority
        '''
        new_node = Node(job, priority)
        self._internal_queue.put(new_node)

    def get_job(self):
        '''Returns the highest priority job number found'''
        # very slow way of doing this
        reserve = []
        curr_node = None
        highest = None
        highest_pos = None
        highest_priority = None
        q_len = self._internal_queue.qsize()

        if q_len == 0:
            raise QueueEmptyException

        # scan every item until we find an A
        # if we don't find an A, return the first item of the highest priority in the list
        for i in range(0, q_len):
            curr_node = self._internal_queue.get()
            # save the item we popped and store in the reserve
            reserve.append(curr_node)
            # no switch statement in python :(
            if curr_node.priority == 'A':
                highest = curr_node
                highest_pos = i
                break

            elif curr_node.priority == 'B':
                if highest_priority != 'B' and highest_priority != 'A':
                    highest = curr_node
                    highest_pos = i
                    highest_priority = 'B'

            elif curr_node.priority == 'C':
                if highest_priority != 'C' and not highest_priority in 'AB':
                    highest = curr_node
                    highest_pos = i
                    highest_priority = 'C'

            elif curr_node.priority == 'D':
                if highest_priority != 'D' and not highest_priority in 'ABC':
                    highest = curr_node
                    highest_pos = i
                    highest_priority = 'D'

        reserve.pop(highest_pos)

        # put items back from reserve
        for item in reserve:
            self._internal_queue.put(item)

        return highest.job

    def __str__(self):
        reserve = []
        curr_node = None
        q_len = self._internal_queue.qsize()
        output = ''

        if q_len == 0:
            return 'Queue is empty!'

        for i in range(0, q_len):
            curr_node = self._internal_queue.get()
            # save the item we popped and store in the reserve
            reserve.append(curr_node)
            output += str(i) + ': ' + str(curr_node.job) + \
                ', ' + str(curr_node.priority) + '\n'

        # put items back from reserve
        for item in reserve:
            self._internal_queue.put(item)

        return output


if __name__ == "__main__":
    test_queue = PriorityQueue()

    test_queue.add_job(1000, 'B')
    test_queue.add_job(1001, 'B')
    test_queue.add_job(1002, 'B')

    test_queue.add_job(2000, 'D')
    test_queue.add_job(2001, 'D')
    test_queue.add_job(2002, 'D')
    test_queue.add_job(2003, 'D')

    test_queue.add_job(3000, 'A')
    test_queue.add_job(3001, 'A')

    # Uncomment the following lines to test getting jobs
    # print(test_queue.get_job())
    # print(test_queue.get_job())
    # print(test_queue.get_job())

    print(test_queue)

    input('Press any key')

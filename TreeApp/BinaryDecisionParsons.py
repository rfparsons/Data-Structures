'''
Program: BinaryDecisionParsons.py
Author: Bobby Parsons

Description: Runs through a decision tree on whether to take a class or not

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or 
unmodified. I have not given other fellow student(s) access to
my program.   
'''


class Node:
    '''Node within a Binary Search Tree.

    :param s_data: Question to ask when this node is reached (or statement
    to make at the end of the path)
    :param path: Path to decision, as a string of 'y' and 'n'
    '''

    def __init__(self, s_data, path):
        self._s_data = s_data
        self._path = path
        self._no = None
        self._yes = None

    def insert(self, s_data, path):
        '''Recursive function for inserting

        :param s_data: Question to ask when this node is reached (or statement
        to make at the end of the path)
        :param path: Path to decision, as a string of 'y' and 'n'
        '''
        if path[0].lower() == 'n':
            if self._no == None:
                self._no = Node(s_data, path[1:])
            else:
                self._no.insert(s_data, path[1:])
        elif path[0].lower() == 'y':
            if self._yes == None:
                self._yes = Node(s_data, path[1:])
            else:
                self._yes.insert(s_data, path[1:])
        else:
            raise ValueError

    # def search(self, s_data):
    #     '''Recursive function for searching

    #     :param s_data: String to find
    #     '''
    #     if s_data < self._s_data:
    #         if self._no == None:
    #             return None
    #         else:
    #             return self._no.search(s_data)
    #     elif s_data > self._s_data:
    #         if self._yes == None:
    #             return None
    #         else:
    #             return self._yes.search(s_data)
    #     else:
    #         return (self._s_data)

    @property
    def no(self):
        return self._no

    @no.setter
    def no(self, node):
        self._no = node

    @property
    def yes(self):
        return self._yes

    @yes.setter
    def yes(self, node):
        self._yes = node

    @property
    def s_data(self):
        return self._s_data

    def __str__(self):
        return '(' + self._s_data + ', ' + str(self._path) + ')'


class BDT:
    '''Simple Binary Decision Tree

    :param top_question: Overarching question the tree aims to answer
    '''

    def __init__(self, top_question):
        self._root_node = None
        self._top_question = top_question

    def insert(self, s_data, path):
        '''Inserts a new string into the tree

        :param s_data: Question to ask when this node is reached (or statement
        to make at the end of the path)
        :param path: Path to decision, as a string of 'y' and 'n'
        '''
        if self._root_node == None:
            self._root_node = Node(s_data, path)
        else:
            self._root_node.insert(s_data, path)

    def ask_questions(self):
        '''Runs through the decision tree and asks the questions'''
        curr_node = self._root_node
        ended = False

        print(self._top_question)
        while not ended:
            print(curr_node.s_data, end=' ')
            if curr_node.yes != None and curr_node.no != None:
                valid = False
                while not valid:
                    choice = input('[y/n] ').lower()
                    if choice == 'y' or choice == 'n':
                        valid = True

                if choice == 'y':
                    curr_node = curr_node.yes
                else:  # already validated above
                    curr_node = curr_node.no
            else:
                ended = True
                print()  # provide the final \n

    # def search(self, s_data):
    #     '''Searches for a string in the tree

    #     :param s_data: String to find
    #     '''
    #     if self._root_node == None:
    #         return None
    #     else:
    #         return self._root_node.search(s_data)


if __name__ == "__main__":
    take_class = BDT('Should I take this class?')

    take_class.insert('Is it required?', '')
    take_class.insert('Take it!', 'y')
    take_class.insert('Am I interested in the subject?', 'n')
    take_class.insert('Do I have room in my schedule?', 'ny')
    take_class.insert('Don\'t take it!', 'nn')
    take_class.insert('Take it!', 'nyy')
    take_class.insert('Don\'t take it!', 'nyn')

    take_class.ask_questions()

    input('Press any key ')

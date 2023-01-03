'''
Program: EncapsulationParsons.py
Author: Bobby Parsons

Description: Has a class for a can that can contain several things
'''


class Can():
    '''Class describing a canned good
    
    :param company: Company that makes the canned good
    :param content: Contents of the can
    :param size: Weight of the can
    :param price: Price of each can
    '''

    def __init__(self, company='', content='', size=0.0, price=0.0):
        self._company = company
        self._content = content
        self._size = size
        self._price = price

    def get_company(self):
        '''Returns the company that makes the canned good'''
        return self._company

    def set_company(self, company):
        '''Sets the company that makes the canned good
        
        :param company: Company that makes the canned good
        '''
        self._company = company

    def get_content(self):
        '''Returns the contents of the can'''
        return self._content

    def set_content(self, content):
        '''Sets the contents of the can
        
        :param company: Contents of the can
        '''
        self._content = content

    def get_size(self):
        '''Returns the weight of the can'''
        return self._size

    def set_size(self, size):
        '''Sets the weight of the can
        
        :param company: Weight of the can
        '''
        self._size = size

    def get_price(self):
        '''Returns the price of the can'''
        return self._price

    def set_price(self, price):
        '''Sets the price of the can
        
        :param company: Price of the can
        '''
        self._price = price

    def print_can(self):
        '''Prints all information about the can'''
        print('Can [Company=' + self._company + ', Content=' + self._content +
              ', Size=' + str(self._size) + ', Price=' + str(self._price) + ']')


if __name__ == "__main__":
    # Big-O: O(1) (Would be N if data wasn't hard-coded)

    cans = []

    cans.append(Can('Field Day', 'Black Beans', 13.0, 0.99))
    cans.append(Can('S&W', "Peaches", 12.0, 2.39))
    cans.append(Can('Green Giant', 'Green Beans', 11.9, 1.79))
    cans.append(Can('Del Monte', 'Creamed Corn', 13.4, 2.49))

    i = 0
    for can in cans:
        i = i + 1
        print('Can ' + str(i) + ': ', end='')
        can.print_can()


'''
Can 1: Can [Company=Field Day, Content=Black Beans, Size=13.0, Price=0.99] 
Can 2: Can [Company=S&W, Content=Peaches, Size=12.0, Price=2.39]
Can 3: Can [Company=Green Giant, Content=Green Beans, Size=11.9, Price=1.79]
Can 4: Can [Company=Del Monte, Content=Creamed Corn, Size=13.4, Price=2.49]
'''

#!/usr/bin/python3
'''
class that inherits from list
'''


class MyList(list):
    '''
    function: class
    '''

    def print_sorted(self):
        '''fucntion: print_sorted(self)
        returns sorted list
        '''
        print(sorted(self))

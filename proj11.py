import itertools

class Matrix(object):
    '''Add your docstring here.'''
    
    def __init__(self):  # no modification is needed for this method, but you may modify it if you wish to
        '''Create and initialize your class attributes.'''
        self._matrix = []
        self._rooms = 0
        
    def read_file(self,fp):  #fp is a file pointer
        '''Build an adjacency matrix that you read from a file fp.'''
        pass # replace with your code
            
    def __str__(self):
        '''Return the matrix as a string.'''
        s = ''
        pass  # build a string that represents the matrix for printing
        return s  #__str__ always returns a string

    def __repr__(self):  # no modification need of this method
        '''Call __str__() to return a string for displaying in the shell'''
        return self.__str__()  
        
    def adjacent(self,index):
        '''Return the set of connecting rooms to room specified by index'''
        # Hint: only one line, return something, is needed
        pass # replace with your code

    def rooms(self):
        '''Return the number of rooms'''
        # Hint: only one line, return something, is needed
        pass # replace with your code
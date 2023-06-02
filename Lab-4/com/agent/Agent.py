from abc import abstractmethod

class Agent(object):
    ''' classdocs'''
    @abstractmethod 
    def __init__(self): 
        pass

    @abstractmethod 
    def sense(self,environment): 
        pass

    @abstractmethod 
    def act(self): 
        pass
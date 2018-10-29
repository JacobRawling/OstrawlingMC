"""
Authors: Jacob Rawling & Kiran Ostrolenk

@Brief: General class to save generated events to various output files as specified
by the user. 
"""
import logging

def abstractmethod(method):
    """
    An @abstractmethod member fn decorator.
    """
    def default_abstract_method(*args, **kwargs):
        raise NotImplementedError('call to abstract method ' 
                                  + repr(method))
    default_abstract_method.__name__ = method.__name__    
    return default_abstract_method

class Saver:
    def __init__(self, output_file):
        self.output_file = output_file
        logging.info('Saving event to %s'%output_file)
        self.open_file()
        
    def __del__(self):
        self.close_file()
        
    @abstractmethod
    def open_file(self):
        pass

    def close_file(self):
        pass

    @abstractmethod
    def save_event(self, event):
        pass


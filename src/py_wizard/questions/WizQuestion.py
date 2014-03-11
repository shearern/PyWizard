'''
Created on Mar 25, 2013

@author: nate
'''
import re
from abc import ABCMeta, abstractmethod

class WizQuestion(object):
    '''A question to the user.  Like a form Field'''
    __metaclass__ = ABCMeta
    
    DIRS = dict()
    
    def __init__(self, name, default=None, optional=False):
        self.__name = name
        self.__optional = False
        
        self.default = default      # Default from question definition
        
        # Previously saved answer (as output by answer_to_save())
        self.previous_answer = None
        self.__answer = None
        
    
    @property
    def answer(self):
        return self.get_answer()
        
    def get_answer(self):
        return self.__answer
    
    def set_answer(self, answer, validate_answer=True):
        if validate_answer:
            if not self.answer_validates(answer):
                msg = "Cannot store answer as it does not validate: "
                msg += self.get_validation_error(answer)
        self.__answer = answer            


    @property
    def answer_to_save(self):
        return self.encode_answer_for_save()
    
    @property
    def is_answered(self):
        return self.__answer is not None
        
    @property
    def name(self):
        return self.__name

    @property
    def is_optional(self):
        return self.__optional


    def answer_validates(self, answer):
        return self.get_validation_error(answer) is None


    @abstractmethod
    def get_validation_error(self, answer):
        '''Validate a potential answer for this question'''
        cname = self.__class__.__name__
        msg = "Subclass %s needs to implement %s()"
        raise Exception(msg % (cname, 'get_validation_errors'))
    
    
    def encode_answer_for_save(self):
        '''Return answers formatted to save in answer dictionary'''
        return self.__answer
    
    
    def calc_default_answer(self):
        '''Calc answer to use as default'''
        if self.previous_answer is not None:
            return self.previous_answer
        if self.default is not None:
            return self.default
        return None
    

    # -- Fluid Interface Options ---------------------------------------------
    
    def set_default(self, default_value):
        '''Set default value'''
        self.default = default_value
        return self
        
        
    def optional(self, is_optional=True):
        '''Mark the value as optional'''
        self.__optional = is_optional
        return self
    
    
    # -- Tk -------------------------------------------------------------------
    
#    def build_tk_input(self, frame):
#        '''Build TK interface for asking this question
#        
#        @return dict: Wizard objects created to pass back to
#            validate_tk_input() and save_tk_input()
#        '''
#        cname = self.__class__.__name__
#        msg = "Subclass %s needs to implement %s()"
#        raise Exception(msg % (cname, 'build_tk_input'))
#    
#    
#    def save_tk_input(self, widgets):
#        '''Save input from tk widgets to .user_answer
#        
#        @param widgets: Dictionary of widgets returned from build_tk_input()
#        '''
#        cname = self.__class__.__name__
#        msg = "Subclass %s needs to implement %s()"
#        raise Exception(msg % (cname, 'save_tk_input'))
        
        

'''
Created on Mar 26, 2013

@author: nate
'''
import re

from SimpleQuestion import SimpleQuestion

class SelectQuestion(SimpleQuestion):
    '''A question where the user must select from a list of options
    
    Stored value and saved value are the actual option value, not the position
    '''
    
    def __init__(self, name, question, options, default=None):
        super(SelectQuestion, self).__init__(name, question, default)
        self.__options = options
        self.__only_if_many = False  # Only prompt if there are many options
        
        
    @property
    def options(self):
        # Have question autoload options if it does that
        if len(self.__options) == 0:
            self.autoload_options()
            
        # Return options
        return self.__options[:]
    
    
    def only_ask_if_many(self):
        '''Mark question to be presented only if there is more than 1 option'''
        self.__only_if_many = True
        
        
    @property
    def only_if_many(self):
        return self.__only_if_many
    
    
    def get_option_by_pos(self, pos):
        '''Return option based on it's numeric position in the list'''
        return self.__options[pos-1]
    
    
    def get_simple_question_child_error(self, answer):
        
        if answer is not None:
            
            # Allow user to type in one of the options
            if answer in self.__options:
                return None
            
            # Allow user to be by position
            try:
                selected = int(answer)
                self.get_option_by_pos(selected)
                return None
            except IndexError:
                pass
                
            return "Not one of the options"
    
    
    def add_option(self, option):
        self.__options.append(option)
        
        
    def autoload_options(self):
        '''Optional hook for child to generate options'''
        pass
        
        
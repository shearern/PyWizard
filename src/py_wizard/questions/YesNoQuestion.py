'''
Created on Mar 25, 2013

@author: nate
'''
from .SimpleQuestion import SimpleQuestion

class YesNoQuestion(SimpleQuestion):
    '''A question where the answer is either yes or no'''
    
    def __init__(self, name, question, default=None):
        super(YesNoQuestion, self).__init__(name, question, default)
        
    
    def get_simple_question_child_error(self, answer):
        '''Validate a potential answer for this question'''
        
        if answer is True or answer is False or answer is None:
            return None
        
        return "Answer must be True, False, or None"
    
    

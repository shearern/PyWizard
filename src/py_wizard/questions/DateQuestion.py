'''
Created on Mar 25, 2013

@author: nate
'''
from datetime import datetime

from SimpleQuestion import SimpleQuestion

class DateQuestion(SimpleQuestion):
    '''A question where the answer is a date'''
    
    def __init__(self, name, question, format='%Y-%m-%d', default=None):
        self.__format = format
        super(DateQuestion, self).__init__(name, question, default)
        
    @property
    def date_format(self):
        return self.__format
    
    
    def get_simple_question_child_error(self, answer):
        if answer is not None:
            if answer.__class__ is not datetime:
                return "Not a date"

    

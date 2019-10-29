'''
Created on Mar 26, 2013

@author: nate
'''
from .WizQuestion import WizQuestion

class ParagraphQuestion(WizQuestion):
    '''A question that takes multiple lines of text as an answer'''
    
    def __init__(self, name, question, defaults=None):
        super(ParagraphQuestion, self).__init__(name, defaults)
        self.__question_txt = question
        
    @property
    def question_txt(self):
        return self.__question_txt
        
        
    def get_validation_error(self, answer):
        if answer is None:
            if not self.is_optional:
                return "Answer is required"
        elif answer.__class__ is not str:
            return "Answer must be a string"
    
    
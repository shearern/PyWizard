'''
Created on Mar 25, 2013

@author: nate
'''
from .SimpleQuestion import SimpleQuestion

class CurrencyQuestion(SimpleQuestion):
    '''A question where the answer is a dollar amount.
    
    Value is stored as number of cents
    '''
    
    def __init__(self, name, question, default=None):
        super(CurrencyQuestion, self).__init__(name, question, default)
        
    
    def get_simple_question_child_error(self, answer):
        
        if answer is not None:
            
            # Make sure it's an int
            try:
                int(answer)
            except ValueError:
                return "Answer is not a int"
            
            # Limit to two decimal places
            parts = str(answer).strip('0').split(".")
            if len(parts) == 2:
                if len(parts[1]) > 2:
                    return "Currency values are limited to two decimal places"
        
        return None
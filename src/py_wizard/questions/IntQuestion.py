'''
Created on Mar 25, 2013

@author: nate
'''
from SimpleQuestion import SimpleQuestion

class IntQuestion(SimpleQuestion):
    '''A question where the answer is an integer'''
    
    def __init__(self, name, question, default=None):
        super(IntQuestion, self).__init__(name, question, default)
        
    
    def get_simple_question_child_error(self, answer):
        
        if answer is not None:
            try:
                int(answer)
            except ValueError:
                return "Answer is not an integer"
        
        return None
    
    

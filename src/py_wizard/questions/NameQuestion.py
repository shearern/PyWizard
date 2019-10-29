'''
Created on Mar 26, 2013

@author: nate
'''
import re

from .SimpleQuestion import SimpleQuestion

class NameQuestion(SimpleQuestion):
    '''A question where the result needs to be a variable name'''
    
    PAT=re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]+$')
    
    def get_simple_question_child_error(self, answer):
        if answer is not None:
            if not self.PAT.match(answer):
                return "Answer contains invalid characters for a name"


'''
Created on May 8, 2013

@author: nshearer
'''
from YesNoQuestion import YesNoQuestion

class ActionPrompt(YesNoQuestion):
    '''This prompts the user to perform an action

    Answer just indicates if the process was performed'''
    
    def __init__(self, name, prompt):
        question = "%s\nAction Completed?" % (prompt)
        super(ActionPrompt, self).__init__(name, question, default=True)
        

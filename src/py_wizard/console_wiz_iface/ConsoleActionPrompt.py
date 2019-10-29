'''
Created on Sep 20, 2013

@author: nshearer
'''
from .ConsoleYesNoQuestion import ConsoleYesNoQuestion


class ConsoleActionPrompt(ConsoleYesNoQuestion):
    '''Present an action prompt on the console'''
    
#    def __init__(self, question):
#        super(ConsoleActionPrompt, self).__init__(question)
    
    def present_question(self):
        print("")
        print("-- ACTION --")
        super(ConsoleActionPrompt, self).present_question()
        if self.question.previous_answer is True:
            print("* This task has already been completed *")


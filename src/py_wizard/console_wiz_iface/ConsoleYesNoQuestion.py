'''
Created on Jul 10, 2013

@author: nshearer
'''
from .ConsoleSimpleQuestion import ConsoleSimpleQuestion, UserAnswerValidationError


class ConsoleYesNoQuestion(ConsoleSimpleQuestion):
    
    def __init__(self, question):
        super(ConsoleYesNoQuestion, self).__init__(question)


    def present_question(self, format_help=None):
        super(ConsoleYesNoQuestion, self).present_question(format_help='yes/no')
        

    def encode_answer_to_native(self, user_answer=None):
        if user_answer is None:
            user_answer = self.user_answer
        if user_answer.lower() in ['yes', 'y', '1', 'on', 'true']:
            return True
        elif user_answer.lower() in ['no', 'n', '0', 'off', 'false']:
            return False
        elif len(user_answer.strip()) == 0:
            return None
        raise UserAnswerValidationError("Answer not recognized")
    
    
    def decode_answer_to_text(self, answer):
        '''Given a previous or default answer, convert it to a text value'''
        if answer is True:
            return 'yes'
        elif answer is False:
            return 'no'
        return None
        
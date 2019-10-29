'''
Created on Jul 10, 2013

@author: nshearer
'''
from .ConsoleSimpleQuestion import ConsoleSimpleQuestion
from .ConsoleSimpleQuestion import UserAnswerValidationError

class ConsoleIntQuestion(ConsoleSimpleQuestion):
    
    def __init__(self, question):
        super(ConsoleIntQuestion, self).__init__(question)


    def encode_answer_to_native(self, user_answer=None):
        if user_answer is None or len(user_answer.strip()) == 0:
            return None
        try:
            return int(user_answer)
        except ValueError:
            raise UserAnswerValidationError("Answer is not an integer")
    
    
    def decode_answer_to_text(self, answer):
        '''Given a previous or default answer, convert it to a text value'''
        return str(answer)
        
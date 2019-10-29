'''
Created on Sep 20, 2013

@author: nshearer
'''
from datetime import datetime

from .ConsoleSimpleQuestion import ConsoleSimpleQuestion
from .ConsoleSimpleQuestion import UserAnswerValidationError


class ConsoleDateQuestion(ConsoleSimpleQuestion):
    
    def __init__(self, question):
        super(ConsoleDateQuestion, self).__init__(question)

    
    def present_question(self, format_help=None):
        fmt_help = datetime.now().strftime(self.question.date_format)
        super(ConsoleDateQuestion, self).present_question(format_help=fmt_help)

    
    def encode_answer_to_native(self, user_answer):
        '''Get value as a datetime'''
        if user_answer is None or len(user_answer) == 0:
            return None
        
        try:
            return datetime.strptime(user_answer.strip(),
                                     self.question.date_format)
        except ValueError:
            msg = "Does not match format: %s" % (self.question.date_format)
            raise UserAnswerValidationError(msg)


    def decode_answer_to_text(self, answer):
        '''Given a previous or default answer, convert it to a text value'''
        if answer is None or len(str(answer).strip()) == 0:
            return None
        return answer.strftime(self.question.date_format)
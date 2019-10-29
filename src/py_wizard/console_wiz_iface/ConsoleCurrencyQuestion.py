'''
Created on Sep 20, 2013

@author: nshearer
'''
from .ConsoleSimpleQuestion import ConsoleSimpleQuestion
from .ConsoleSimpleQuestion import UserAnswerValidationError


class ConsoleCurrencyQuestion(ConsoleSimpleQuestion):
    
    def __init__(self, question):
        super(ConsoleCurrencyQuestion, self).__init__(question)
    

#    def _format_default_displayed(self, default_answer):
#        return " [%.02f]" % (default_answer / 100.0)
        
        
    def encode_answer_to_native(self, user_answer):
        '''Return answers formatted to save in answer object'''
        if user_answer is None or len(str(user_answer)) == 0:
            return None
        try:
            parts = user_answer.split('.')
            if len(parts) > 2:
                raise UserAnswerValidationError("More than one decimal point?")
            
            cents = 100 * int(parts[0])
            if len(parts) == 2:
                if len(parts[1]) > 2:
                    raise UserAnswerValidationError("Cents must be less than 100")
                cents += int(parts[1])
                
            return cents
        except ValueError:
            raise UserAnswerValidationError("Value not a decimal")


    def decode_answer_to_text(self, answer):
        '''Given a previous or default answer, convert it to a text value'''
        if answer is None or len(str(answer).strip()) == 0:
            return None
        
        dollars = answer / 100  # Int division truncates
        cents = answer % 100
        
        return '%d.%02d' % (dollars, cents)
            
        

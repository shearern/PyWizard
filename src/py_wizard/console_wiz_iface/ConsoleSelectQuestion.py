'''
Created on Sep 20, 2013

@author: nshearer
'''
from .ConsoleSimpleQuestion import ConsoleSimpleQuestion
from .ConsoleSimpleQuestion import UserAnswerValidationError

class ConsoleSelectQuestion(ConsoleSimpleQuestion):
    
    def __init__(self, question):
        super(ConsoleSelectQuestion, self).__init__(question)
    
    
    def get_input_line(self):
        '''Get answer from the user'''
        # Skip if only one answer
        if self.question.only_if_many:
            options = self.question.options
            if len(options) == 1:
                print(">", options[0], "(only option)")
                return options[0]
        
        # Else, ask user
        return super(ConsoleSelectQuestion, self).get_input_line()        

    
    def present_question(self):
        super(ConsoleSelectQuestion, self).present_question()
        print("Options:")
        for i, option in enumerate(self.question.options):
            print(" %02d)  %s" % (i+1, option))
        
        
    def encode_answer_to_native(self, user_answer):
        '''Return answers formatted to save in answer object'''

        if user_answer is None or len(str(user_answer)) == 0:
            return None
            
        # Try to use list position first, then use as actual option
        try:
            selected = int(user_answer)
            return self.question.get_option_by_pos(selected)
        except IndexError:
            if user_answer in self.question.options:
                return user_answer
        except ValueError:
            if user_answer in self.question.options:
                return user_answer
        
        msg = "Answer not one of the defined options"
        raise UserAnswerValidationError(msg)
            
            
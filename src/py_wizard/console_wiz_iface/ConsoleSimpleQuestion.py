'''
Created on Jul 9, 2013

@author: nshearer
'''
from .ConsoleQuestionPresenter import ConsoleQuestionPresenter

class UserAnswerValidationError(Exception): pass

class ConsoleSimpleQuestion(ConsoleQuestionPresenter):
    
    def __init__(self, question):
        super(ConsoleSimpleQuestion, self).__init__(question)
        
        
    def present_question(self, format_help=None):
        question = self.question.question_txt
        
        if format_help is not None:
            question += ' (ex: %s)' % (format_help)
        
        default_answer = self._calc_default_answer_to_present_to_user()
            
        if default_answer is not None:
            question += " [%s]" % (default_answer)
            # If you need to customize the display of the default value,
            # then override decode_answer_to_text() 
            
        print(question)
        
        
    def get_validation_error_for_user_answer(self, user_answer):
        '''See if user anwer validates.
        
        Default implementation is to encode to native and pass to native
        answer validator.
        '''
        try:
            answer = self.encode_answer_to_native(user_answer)
            return self.question.get_validation_error(answer)
        except UserAnswerValidationError as e:
            return str(e)
        return None

    
    def decode_answer_to_text(self, answer):
        '''Given a previous or default answer, convert it to a text value'''
        if answer is None or len(str(answer).strip()) == 0:
            return None
        return answer
    
    
    def _calc_default_answer_to_present_to_user(self):
        '''Get the default answer to present to the user'''
        answer = self._calc_default_answer()
        if answer is None:
            return None
        return self.decode_answer_to_text(answer)
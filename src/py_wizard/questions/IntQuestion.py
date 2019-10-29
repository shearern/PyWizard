'''
Created on Mar 25, 2013

@author: nate
'''
from .SimpleQuestion import SimpleQuestion

class IntQuestion(SimpleQuestion):
    '''A question where the answer is an integer'''

    def __init__(self, name, question, default=None, min_value=None, max_value=None):
        self.__min_value = min_value
        self.__max_value = max_value
        super(IntQuestion, self).__init__(name, question, default)


    def get_simple_question_child_error(self, answer):

        if answer is not None:
            try:
                int(answer)
            except ValueError:
                return "Answer is not an integer"
            
            value = int(answer)
            if self.__min_value is not None and value < self.__min_value:
                return "Answer must be >= %d" % (self.__min_value)
            if self.__max_value is not None and value > self.__max_value:
                return "Answer must be <= %d" % (self.__max_value)

        return None



'''
Created on Mar 25, 2013

@author: nate
'''
from .WizQuestion import WizQuestion

class ListQuestion(WizQuestion):
    '''A question that takes a list of answers and creates an array'''


    def __init__(self, name, question, default=None, options=None):
        if default is None:
            default = list()
        super(ListQuestion, self).__init__(name, default)
        self.__options = options
        self.question_txt = question
        self.set_answer(list(), False)


    def get_validation_error(self, answer):
        if answer.__class__ is not list:
            return "Answer must be a list"
        if self.__options is not None:
            for value in answer:
                if value not in self.__options:
                    msg = "Value '%s' is not valid.  " % (value)
                    msg += "Must be one of: " + ', '.join(self.__options[:8])
                    if len(self.__options) > 8:
                        msg += ', ...'
                    return msg
        if len(answer) == 0:
            if not self.is_optional:
                return "Must include at least one item"


    def calc_default_answer(self):
        '''Calc answer to use as default'''
        value = super(ListQuestion, self).calc_default_answer()
        if value is None:
            return list()
        return value


    def set_answer(self, answer, validate_answer=True):
        if answer is None:
            super(ListQuestion, self).set_answer(list(), validate_answer)
        else:
            super(ListQuestion, self).set_answer(answer, validate_answer)


    def get_answer(self):
        answers = super(ListQuestion, self).get_answer()
        return answers[:]



#    def present_question(self, default=None):
#        print self.__question
#        if default is not None and len(default) > 0:
#            print "-- Default Value: --"
#            for i, item in enumerate(default):
#                print " [%02d] %s" % (i, item)
#            print "--------------------"
#
#        print " - Enter Items one per line"
#        print " - Enter a blank item to end the list"
#        if default is not None and len(default) > 0:
#            print " - If you enter no values, the default list will be used"
#            print " - Specify [empty] to force an empty list"
#
#
#    def get_input_line(self):
#        '''Get answer from the user'''
#        return raw_input("[%02d] " % (len(self.answer))).rstrip()
#
#
#    def list_commands(self):
#        commands = super(ListQuestion, self).list_commands()
#        commands['[empty]'] = "Specify that the list should be empty"
#
#
#    def handle_command(self, command):
#        '''Handle a command
#
#        @return bool: Request more input from user?
#        '''
#        if command == '[empty]':
#            self.answer = list()
#            return False
#        else:
#            return super(ListQuestion, self).handle_command(command)
#
#
#    def handle_answer_line(self, line):
#        '''Process user answer
#
#        Default behaviour is to set as answre
#
#        @return bool: Request more input from user?
#        '''
#        self.answer.append(line)
#        return True
#
#
#    def handle_blank_line(self):
#        if len(self.answer) == 0:
#            if self.asked_default is not None and len(self.asked_default) > 0:
#                print "Using default"
#                self.answer = self.asked_default
#        return False
#
#
#    def validate_answer(self):
#        if len(self.answer) == 0:
#            if not self.is_optional:
#                return "Must include at least one item"
#
#    def handle_validation_error(self):
#        self.answer = list()
#


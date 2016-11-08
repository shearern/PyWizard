'''
Created on Jul 9, 2013

@author: nshearer
'''
import re
from abc import ABCMeta, abstractmethod
import gflags

from py_wizard.questions.QuestionPresenter import QuestionPresenter


class QtQuestionPresenter(QuestionPresenter):
    '''Question presenter base class for console interface'''
    __metaclass__ = ABCMeta

    
    def __init__(self, question):
        super(QtQuestionPresenter, self).__init__(question)

    
    @abstractmethod
    def build_question_widget(self, root, parent_frame):
        '''Construct widget to ask user the question

        Gets processed in GuiTaskrunner._msg_received_from_wizard_thread()
        '''


    @abstractmethod
    def build_answer_log_widget(self, root, parent_frame):
        '''Construct widget to record question answer in the log

        Gets processed in GuiTaskrunner._msg_received_from_wizard_thread()\
        '''


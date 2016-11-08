from QtQuestionPresenter import QtQuestionPresenter
from QtSimpleWidget import QtSimpleWidget
from AnsweredQuestionWidget import AnsweredQuestionWidget

class QtSimpleQuestion(QtQuestionPresenter):
    
    def __init__(self, question):
        super(QtSimpleQuestion, self).__init__(question)


    def build_question_widget(self, root, parent_frame):
        '''Construct widget to ask user the question'''

        widget = QtSimpleWidget(parent=parent_frame, presenter=self)

        return widget


    def build_answer_log_widget(self, root, parent_frame):
        '''Construct widget to record question answer in the log

        Gets processed in GuiTaskrunner._msg_received_from_wizard_thread()\
        '''
        return AnsweredQuestionWidget(
            parent=parent_frame,
            question_txt=self.question.question_txt,
            answer_txt = self.question.answer)

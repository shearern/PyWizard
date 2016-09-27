'''Messages passed between Wizard and UI threads'''



class AskQuestionMsg(object):
    TYPE='ask'
    def __init__(self, question_presenter):
        self.q_presenter = question_presenter


class QuestionAnsweredMsg(object):
    TYPE='answer'
    def __init__(self, question_presenter):
        self.q_presenter = question_presenter


class LogQuestionAnswer(object):
    TYPE='log_answer'
    def __init__(self, question_presenter):
        self.q_presenter = question_presenter


class InformUser(object):
    TYPE='inform'
    def __init__(self, text):
        self.text = text

class InformUserAction(object):
    TYPE='inform_action'
    def __init__(self, text):
        self.text = text


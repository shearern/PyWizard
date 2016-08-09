'''Interface to run wizard in a GUI using Qt (pyside)'''
import sys
from threading import Thread
from Queue import Queue

from .GuiTaskRunner import GuiTaskRunner
from py_wizard.WizardUserInterface import WizardUserInterface

from .ui_msgs import AskQuestionMsg, InformUser, LogQuestionAnswer

from .QtQuestionPresenter import QtQuestionPresenter

from ..questions.SimpleQuestion import SimpleQuestion
from .QtSimpleQuestion import QtSimpleQuestion

from ..questions.YesNoQuestion import YesNoQuestion
from .QtYesNoQuestion import QtYesNoQuestion

from PySide.QtGui import QApplication

class QtInterface(WizardUserInterface):
    '''Interface optimized for interacting via the console'''

    def __init__(self):
        super(QtInterface, self).__init__()
        self.ui_queue = Queue()
        self.resp_queue = Queue()
        self.wizard_thread = None


    def start_wizard_execution(self, execute_cb):
        '''Give interface a chance to interact with the starting of the wizard execution

        GUI Wizards take over the main thread, and we want the wizard
        execution to happen in a sub-thread.

        The end result is that execute_cb() gets called (wizard.run_wizard())
        '''

        # Start the execution of the wizard logic in a sub-thread
        self.wizard_thread = Thread(target=execute_cb, name='wizard.execute()')
        self.wizard_thread.start()

        # For main thread, Run Qt main loop
        app = QApplication(sys.argv)
        root_win = GuiTaskRunner(self.ui_queue, self.resp_queue)
        root_win.show()
        app.exec_()


        # # Add log samples
        # root.scrollAreaWidgetContents.setLayout(QVBoxLayout())
        # for i in range(6):
        #     sample = LogSample(root.log_frame)
        #     root.scrollAreaWidgetContents.layout().addWidget(sample)


    def build_standard_q_presenter(self, question):
        '''Wrap a question in a question presenter for this interface'''

        # if isinstance(question, NameQuestion):
        #     return ConsoleNameQuestion(question)
        #
        # if isinstance(question, ActionPrompt):
        #     return ConsoleActionPrompt(question)
        #
        if isinstance(question, YesNoQuestion):
            return QtYesNoQuestion(question)
        #
        # if isinstance(question, IntQuestion):
        #     return ConsoleIntQuestion(question)
        #
        # if isinstance(question, CurrencyQuestion):
        #     return ConsoleCurrencyQuestion(question)
        #
        # if isinstance(question, DateQuestion):
        #     return ConsoleDateQuestion(question)
        #
        # if isinstance(question, ParagraphQuestion):
        #     return ConsoleParagraphQuestion(question)
        #
        # if isinstance(question, ListQuestion):
        #     return ConsoleListQuestion(question)
        #
        # if isinstance(question, SelectQuestion):
        #     return ConsoleSelectQuestion(question)

        if isinstance(question, SimpleQuestion):
            return QtSimpleQuestion(question)

        return None


    def present_question(self, wrapper):
        '''Present question (wrapped in a question presenter class) to user'''

        # Pass the question to the UI thread to process
        # See GuiTaskrunner._msg_received_from_wizard_thread()
        self.ui_queue.put(AskQuestionMsg(wrapper))

        # Wait for response
        # See GuiTaskrunner._question_finished()
        resp = self.resp_queue.get()
        if resp.TYPE != 'answer':
            raise Exception("Expected answer msg, but got %s" % (resp.TYPE))

        # Record question answer in log
        # See GuiTaskrunner._msg_received_from_wizard_thread()
        self.ui_queue.put(LogQuestionAnswer(wrapper))


    def _validate_currect_presenter_class(self, presenter_class):
        '''Make sure the presenter class is appropriate for this interface'''
        if not isinstance(presenter_class, QtQuestionPresenter):
            msg = "Question presenter %s needs to be inherited from %s"
            msg % (presenter_class.__name__, 'QtQuestionPresenter')
            raise Exception(msg)


    def inform_user(self, description):
        '''Inform the user of anything.

        Typically this will be akin to a print'''
        self.ui_queue.put(InformUser(description))


    def inform_user_of_action(self, description):
        '''Inform the user of an action being performed'''
        self.ui_queue.put(InformUser(description))





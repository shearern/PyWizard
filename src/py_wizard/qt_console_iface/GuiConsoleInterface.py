import os, sys
from threading import Thread
from Queue import Queue

from PySide.QtGui import *

from ..console_wiz_iface.ConsoleInterface import ConsoleInterface

from GuiConsoleMainWindow import GuiConsoleMainWindow
from . import qt_console_msgs

class GuiConsoleInterface(ConsoleInterface):
    '''
    Interface to run wizard designed for console in a GUI using Qt (pyside)

    This is intended to serve as a method to encapsulate console wizards
    into a GUI that can execute the wizard, without having to rely on a
    Python IDE.
    '''

    def __init__(self):
        super(GuiConsoleInterface, self).__init__()
        self.ui_queue = Queue()
        self.resp_queue = Queue()
        self.wizard_thread = None # Thread where wizard logic is run


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

        # Set app Icon
        # TODO: Make this a normal Qt Resource file
        app.setWindowIcon(QIcon(":/assets/wizard_256.png"))

        # Tell Windows our APP ID
        #http://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
        try:
            import ctypes
            myappid = 'py_wizard.shearern.net' # arbitrary string
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except:
            pass

        # Setup Root window
        root_win = GuiConsoleMainWindow(self.ui_queue, self.resp_queue)
        root_win.show()

        # Start Qt Main Loop
        app.exec_()

        # Tell wizard we've exited (maybe early)
        self.resp_queue.put(qt_console_msgs.AppExit())


    def present_question(self, wrapper):
        '''Present question (wrapped in a question presenter class) to user'''

        # Pass the question to the UI thread to process
        # See GuiTaskrunner._msg_received_from_wizard_thread()
        self.ui_queue.put(qt_console_msgs.AskQuestionMsg(wrapper))

        # Wait for response
        # See GuiTaskrunner._question_finished()
        resp = self.resp_queue.get()
        if resp.TYPE == 'exit':
            print "GUI Exited"
            sys.exit(2)
        elif resp.TYPE != 'answer':
            raise Exception("Expected answer msg, but got %s" % (resp.TYPE))

        # Record question answer in log
        # See GuiTaskrunner._msg_received_from_wizard_thread()
        self.ui_queue.put(qt_console_msgs.LogQuestionAnswer(wrapper))


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






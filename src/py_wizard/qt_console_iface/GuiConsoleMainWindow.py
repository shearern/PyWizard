from Queue import Empty

import sys
from PySide.QtCore import *
from PySide.QtGui import *

from GuiConsoleMainWindow_UI import Ui_GuiConsoleMainWindow

from .qt_console_msgs import QuestionAnsweredMsg, InformUser

class GuiConsoleMainWindow(QMainWindow, Ui_GuiConsoleMainWindow):
    '''Qt MainWindow widget to interface with user'''

    def __init__(self, rcv_queue, snd_queue):
        '''
        :param rcv_queue: Queue for messages being sent to the UI from QtInterface
        :param snd_queue: Queue to send messages to QtInterface from UI
        '''
        super(GuiConsoleMainWindow, self).__init__()
        self.snd_queue = snd_queue
        self.rcv_queue = rcv_queue
        self.cur_question_presenter = None

        self.setupUi(self)

        # Setup timer to monitor message queue
        self.queue_check_timer = QTimer(self)
        self.connect(self.queue_check_timer, SIGNAL("timeout()"), self._check_queue)
        self.queue_check_timer.start(0.2 * 1000)


    def _check_queue(self):
        while True:
            try:
                msg = self.rcv_queue.get(block=False)
                self._msg_received_from_wizard_thread(msg)
            except Empty:
                return


    def _msg_received_from_wizard_thread(self, msg):

        if msg.TYPE == 'ask':

            self.cur_question_presenter = msg.q_presenter

            # Turn on input


            # Populate task widget with question
            self.question_widget = msg.q_presenter.build_question_widget(self, self.question_frame)
            self.question_frame.layout().addWidget(self.question_widget)
            self.question_widget.question_finished.connect(self._question_finished)

        elif msg.TYPE == 'log_answer':
            self._add_log_seperator()
            item = msg.q_presenter.build_answer_log_widget(self, self.question_frame)
            self.scrollAreaWidgetContents.layout().insertWidget(0, item)

        elif msg.TYPE == 'inform':
            self._add_log_seperator()
            item = LogItemWidget(parent=self.log_frame, text=msg.text)
            self.scrollAreaWidgetContents.layout().insertWidget(0, item)

        else:
            raise Exception("Unknown message type: " + msg.TYPE)





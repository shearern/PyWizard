# Import PySide classes
from Queue import Empty

import sys
from PySide.QtCore import *
from PySide.QtGui import *

from GuiTaskRunner_UI import Ui_GuiTaskRunner

from .ui_msgs import QuestionAnsweredMsg, InformUser

from .LogItemWidget import LogItemWidget

class GuiTaskRunner(QMainWindow, Ui_GuiTaskRunner):
    '''Qt MainWindow widget to interface with user'''

    def __init__(self, rcv_queue, snd_queue):
        '''
        :param rcv_queue: Queue for messages being sent to the UI from QtInterface
        :param snd_queue: Queue to send messages to QtInterface from UI
        '''
        super(GuiTaskRunner, self).__init__()
        self.snd_queue = snd_queue
        self.rcv_queue = rcv_queue
        self.cur_question_presenter = None

        self.setupUi(self)

        self.scrollAreaWidgetContents.setLayout(QVBoxLayout())
        self.scrollAreaWidgetContents.layout().addStretch(0)
        self.first_log_item = True

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

            # Remove current question widget
            self.question_widget.deleteLater()

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


    def _add_log_seperator(self):
        if self.first_log_item:
            self.first_log_item = False
        else:
            line = QFrame(parent=self)
            line.setObjectName("line")
            line.setGeometry(QRect(320, 150, 118, 3))
            line.setFrameShape(QFrame.HLine)
            line.setFrameShadow(QFrame.Sunken)

            self.scrollAreaWidgetContents.layout().insertWidget(0, line)


    def _question_finished(self):

        # Remove question widget
        self.question_widget.deleteLater()
        self.question_widget = QWidget(parent=self.question_frame)

        # Notify wizard question is answered
        self.snd_queue.put(QuestionAnsweredMsg(self.cur_question_presenter))
        self.cur_question_presenter = None



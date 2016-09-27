# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *

from MainWindowDesignerTest import Ui_MainWindow

class MainWindowDesignerTest(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowDesignerTest, self).__init__()
        self.setupUi(self)


from log_sample import Ui_LogSample

class LogSample(QWidget, Ui_LogSample):
    def __init__(self, parent):
        super(LogSample, self).__init__(parent)
        self.setupUi(self)


class ManualGuiWizard(QWidget):

    def __init__(self):
        super(ManualGuiWizard, self).__init__()
        self.initUI()

    def initUI(self):

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.task_frame = QWidget(self)
        layout.addWidget(self.task_frame)
        self.task_frame.setStyleSheet("background-color: #FAC8BF;")
        task_frame_layout = QVBoxLayout()
        self.task_frame.setLayout(task_frame_layout)

        lbl = QLabel("Task", self.task_frame)
        task_frame_layout.addWidget(lbl)

        self.log_frame = QWidget(self)
        self.log_frame.setStyleSheet("background-color:lightblue;")
        log_frame_layout = QVBoxLayout()
        self.log_frame.setLayout(log_frame_layout)
        layout.addWidget(self.log_frame)

        lbl = QLabel("Log", self.log_frame)
        log_frame_layout.addWidget(lbl)

        layout.addStretch()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    root = MainWindowDesignerTest()

    # Add log samples
    root.log_item_container.setLayout(QVBoxLayout())
    for i in range(6):
        sample = LogSample(root.log_frame)
        root.scrollAreaWidgetContents.layout().addWidget(sample)

    root.show()

    app.exec_()
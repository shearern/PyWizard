import os
import sys
import subprocess

# == Setup builders ==========================================================

python = sys.executable

uic = Builder(action = 'c:\Python27\Scripts\pyside-uic.exe $SOURCE -o $TARGET')
qrc = Builder(action = 'c:\Python27\Lib\site-packages\PySide\pyside-rcc.exe $SOURCE -o $TARGET')
py2exe_builder = Builder(action = python + ' setup.py py2exe')

env = Environment(
    BUILDERS = {
        'UiClass' : uic,
        'QtResources': qrc,
        'Exe': py2exe_builder,
    },
    )


# == Utiltities ==============================================================

def list_files_in(root, extensions=None):
    for filename in os.listdir(root):
        path = os.path.join(root, filename)
        if os.path.isfile(path):
            if extensions is None:
                yield path
            else:
                for ext in extensions:
                    if path.lower().endswith(ext.lower()):
                        yield path
        elif os.path.isdir(path):
            for sub_path in list_files_in(path, extensions):
                yield sub_path



# == Builds ==================================================================

built_source_files = list()

# Convert .ui files to .py
env.UiClass('src/py_wizard/qt_console_iface/GuiConsoleMainWindow_UI.py', 'src/py_wizard/qt_console_iface/GuiConsoleMainWindow_UI.ui')
env.UiClass('src/py_wizard/qt_console_iface/ConsoleMessageWidget_UI.py', 'src/py_wizard/qt_console_iface/ConsoleMessageWidget_UI.ui')

'''
Created on Jul 30, 2013

@author: nshearer
'''
from .PyMainWizard import PyMainWizard

class PyWizardForUnitTests(PyMainWizard):
    '''Wizard class to support unit tests'''
    
    def __init__(self):
        super(PyWizardForUnitTests, self).__init__()
        self.enable_answer_saving = True
        self.enable_load_prev_answers = True
        
    
    def _calc_autosave_path(self):
        raise NotImplementedError()
    
    def ask_questions_and_process(self):
        raise NotImplementedError()
    
    
    
    
    def execute(self):
        pass
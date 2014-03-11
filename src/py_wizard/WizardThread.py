'''
Created on Jul 9, 2013

@author: nshearer
'''
from threading import Thread

class WizardThread(Thread):
    '''Encapsulate the wizard logic in a thread'''
    
    def __init__(self, wizard):
        self.__wizard = wizard
        super(WizardThread, self).__init__(name='WizardLogic')
        
        
    @property
    def wizard(self):
        return self.__wizard
    
    
    def run(self):
        self.__wizard.run_wizard()
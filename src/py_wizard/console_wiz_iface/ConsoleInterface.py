'''
Created on Jul 9, 2013

@author: nshearer
'''
from py_wizard.WizardUserInterface import WizardUserInterface

from ConsoleQuestionPresenter import ConsoleQuestionPresenter

from py_wizard.questions.SimpleQuestion import SimpleQuestion
from ConsoleSimpleQuestion import ConsoleSimpleQuestion

from py_wizard.questions.NameQuestion import NameQuestion
from ConsoleNameQuestion import ConsoleNameQuestion

from py_wizard.questions.YesNoQuestion import YesNoQuestion
from ConsoleYesNoQuestion import ConsoleYesNoQuestion

from py_wizard.questions.IntQuestion import IntQuestion
from ConsoleIntQuestion import ConsoleIntQuestion

from py_wizard.questions.CurrencyQuestion import CurrencyQuestion
from ConsoleCurrencyQuestion import ConsoleCurrencyQuestion

from py_wizard.questions.DateQuestion import DateQuestion
from ConsoleDateQuestion import ConsoleDateQuestion

from py_wizard.questions.ActionPrompt import ActionPrompt
from ConsoleActionPrompt import ConsoleActionPrompt

from py_wizard.questions.ParagraphQuestion import ParagraphQuestion
from ConsoleParagraphQuestion import ConsoleParagraphQuestion

from py_wizard.questions.ListQuestion import ListQuestion
from ConsoleListQuestion import ConsoleListQuestion

from py_wizard.questions.SelectQuestion import SelectQuestion
from ConsoleSelectQuestion import ConsoleSelectQuestion

class ConsoleInterface(WizardUserInterface):
    '''Interface optimized for interacting via the console'''
    
    
    def __init__(self):
        super(ConsoleInterface, self).__init__()


    def start_wizard_execution(self, execute_cb):
        '''Give interface a chance to interact with the starting of the wizard execution

        GUI Wizards take over the main thread, and we want the wizard
        execution to happen in a sub-thread.

        The end result is that execute_cb() gets called (wizard.run_wizard())
        '''
        execute_cb()


    def build_standard_q_presenter(self, question):
        '''Wrap a question in a question presenter for this interface'''
        if isinstance(question, NameQuestion):
            return ConsoleNameQuestion(question)
        
        if isinstance(question, ActionPrompt):
            return ConsoleActionPrompt(question)
        
        if isinstance(question, YesNoQuestion):
            return ConsoleYesNoQuestion(question)
        
        if isinstance(question, IntQuestion):
            return ConsoleIntQuestion(question)
        
        if isinstance(question, CurrencyQuestion):
            return ConsoleCurrencyQuestion(question)
        
        if isinstance(question, DateQuestion):
            return ConsoleDateQuestion(question)
        
        if isinstance(question, ParagraphQuestion):
            return ConsoleParagraphQuestion(question)
        
        if isinstance(question, ListQuestion):
            return ConsoleListQuestion(question)
        
        if isinstance(question, SelectQuestion):
            return ConsoleSelectQuestion(question)
        
        if isinstance(question, SimpleQuestion):
            return ConsoleSimpleQuestion(question)
        
        return None
    

    def _validate_currect_presenter_class(self, presenter_class):
        '''Make sure the presenter class is appropriate for this interface'''
        if not isinstance(presenter_class, ConsoleQuestionPresenter):
            msg = "Question presenter %s needs to be inherited from %s"
            msg % (presenter_class.__name__, 'ConsoleQuestionPresenter')
            raise Exception(msg)
        
        
    def present_question(self, wrapper):
        '''Present question (wrapped in a question presenter class) to user'''
        wrapper.ask()
        
        
    def inform_user(self, description):
        '''Inform the user of anything.
        
        Typically this will be akin to a print'''
        print description
    
    
    def inform_user_of_action(self, description):
        '''Inform the user of an action being performed'''
        print description
        
        
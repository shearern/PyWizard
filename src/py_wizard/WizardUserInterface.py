'''
Created on Jul 9, 2013

@author: nshearer
'''
from abc import ABCMeta, abstractmethod, abstractproperty

class WizardUserInterface(object):
    '''Class to encapsulate Wizard interaction with user'''
    __metaclass__ = ABCMeta
    
    def __init__(self):
        self.__addtl_question_presenters = list()
    
    
#    @abstractmethod
#    def run(self):
#        '''Begin interfacing wizard with user'''
#        cname = self.__class__.__name__
#        msg = "Interface class %s must implement %s()"
#        raise NotImplementedError(msg % (cname, 'run'))


    def ask_question(self, question):
        '''Present a question to the end user and wait for an answer'''
        
        # Wrap question in a question presentation object
        wrapper = self.build_question_presenter(question)
        if wrapper is None:
            msg = "Interface %s does not have a question presenter for %s"
            msg = msg % (self.__class__.__name__, question.__class__.__name__)
            raise NotImplementedError(msg)
        
        # Present question to user
        self.present_question(wrapper)
        
        # Return question answer
        return question.answer
    
    
    def build_question_presenter(self, question):
        '''Wrap a question in a question presenter for this interface'''
        # Check for additional presenters that have been registered
        # with register_addtl_question_type()
        presenter = self._check_for_addtl_q_type(question)
        if presenter is None:
            # Check for all the standard question presenters
            presenter = self.build_standard_q_presenter(question)
        return presenter
    
    
    @abstractmethod
    def build_standard_q_presenter(self, question):
        '''Wrap a question in a question presenter for this interface
        
        This hook is for the interface sub-class to implement the standard
        question presenters.
        
        @param question: Question we need to ask (WizQuestion)
        '''
        pass
    
    
    @abstractmethod
    def present_question(self, wrapper):
        '''Present question (wrapped in a question presenter class) to user'''
        cname = self.__class__.__name__
        msg = "Interface class %s must implement %s()"
        raise NotImplementedError(msg % (cname, 'present_question'))
    
    
    @abstractmethod
    def inform_user(self, description):
        '''Inform the user of anything.
        
        Typically this will be akin to a print'''
    
    
    @abstractmethod
    def inform_user_of_action(self, description):
        '''Inform the user of an action being performed'''


    @abstractmethod
    def start_wizard_execution(self, execute_cb):
        '''Give interface a chance to interact with the starting of the wizard execution

        GUI Wizards take over the main thread, and we want the wizard
        execution to happen in a sub-thread.

        The end result is that execute_cb() gets called (wizard.run_wizard())
        '''

        
        
    # -- Allow simple registration of new question types ----------------------
        
    def register_addtl_question_type(self, question_class, presenter_class):
        '''Specify the presenter/wrapper for a question class'''
        item = (question_class, presenter_class)
        self.__addtl_question_presenters.append(item)
        

    @abstractmethod
    def _validate_currect_presenter_class(self, presenter_class):
        '''Make sure the presenter class is appropriate for this interface'''
    
        
    def _check_for_addtl_q_type(self, question):
        '''See if there's a presenter registered for this question'''
        for qclass, pclass in self.__addtl_question_presenters:
            if isinstance(question, qclass):
                return pclass(question)
    
    
    
    
    
        
#!/usr/bin/python

from .PyWizardBase import PyWizardBase
from abc import ABCMeta, abstractmethod

class PySubWizard(PyWizardBase, metaclass=ABCMeta):
    '''A sub wizard base.
    
    Sub wizards are intended to be attached to parent wizards (either other
    sub wizards, or to the main wizard) to modularize the wizard logic.
    '''
    
    def __init__(self):
        super(PySubWizard, self).__init__()
        
        self.parent_wizard = None
        
        # Answer caches
        self.parent_answers = None
        self.sibling_answers = None
        
        self.warn_if_execute_phase_missing = True
        
        
    # -- Wizard ID ------------------------------------------------------------
    
    @property
    def wiz_id(self):
        '''Sub-wizard unique ID'''
        return self._calc_wiz_id()
    
    def _calc_wiz_id(self):
        '''Determine a ID for this sub-wizard.
        
        Used primarily for keying saved answers
        '''
        return self.__class__.__name__
        
        
    # -- Executing ------------------------------------------------------------
    
    def execute_sub_wizard(self, parent, phase=None):
        '''Execute this sub wizard.
        
        Sub wizards are executed whenever their parent wizard calls
        execute_sub_wizards()
        
        To support allowing the sub wizard to inject behavior at different
        times during the main (parent) wizard, we use the phase parameter.
        If no phase is specified by the parent, then this will call
        execute().  If a phase is specified, then this will call
        execute_<phase>()
        
        @param parent: Reference to parent wizard (-> self.parent_wizard)
            This object will hold a reference to the parent wizard just
            for the duration of this method call.
        @param phase: The name of the phase, or None
        '''
        
        # Prep wizard state with parent info
        self.parent_wizard = parent
        self.iface = self.parent_wizard.iface
        
        # Clear answer caches since parent/sibling answers will have changed
        self.parent_answers = None
        self.sibling_answers = None
        
        # Find execute method
        method = None
        method_name = 'execute'
        if phase is not None:
            method_name += '_' + phase
        try:
            method = getattr(self, method_name)
        except AttributeError:
            if self.warn_if_execute_phase_missing:
                msg = "WARNING: SubWizard %s does not implement %s()"
                msg = msg % (self.__class__.__name__, method_name)
                self.inform_user(msg)
                
        # Call execute method for this phase
        if method:
            method()
        
        # Remove circular link to parent
        self.parent_wizard = None
        
        
    # -- Parent and Sibling Answers -------------------------------------------
    
    def get_parent_answer(self, name, default=None):
        '''Get an answer from the parent'''
        
        # Request answers from parent wizard
        if self.parent_answers is None:
            if self.parent_wizard is not None:
                answers = self.parent_wizard.collect_all_parent_answers()
                self.parent_answers = answers
        
        # Get requested answer
        if self.parent_answers is not None:
            if name in self.parent_answers:
                return self.parent_answers[name]
        return default
        

    
    def get_sibling_answer(self, name, default=None):
        '''Get an answer from the parent'''
        
        # Request answers from parent wizard
        if self.sibling_answers is None:
            if self.parent_wizard is not None:
                answers = self.parent_wizard.collect_child_answers()
                self.sibling_answers = answers
        
        # Get requested answer
        if self.sibling_answers is not None:
            if name in self.sibling_answers:
                return self.sibling_answers[name]
        return default
        


    # -- Answer Handling -----------------------------------------------------
    
    def collect_all_parent_answers(self):
        '''Assemble answers from self and all parents'''
        answers = dict()
        
        # Get answers from parent
        if self.parent_wizard is not None:
            answers = self.parent_wizard.collect_all_parent_answers()
            
        # Add/overlay answers from this wizard
        for name in self.answers:
            answers[name] = self.answers[name]

        return answers

    
    # -- Answer Saving -------------------------------------------------------

    def _load_previous_answer_for_q(self, question, child_id=None):
        '''Load saved answer back into question
        
        @param question: Question to load any saved answers to
        @param child_id: ID of child Wizard question is going to be asked in 
        '''
        # Pass question up to parent
        if child_id is None:
            child_id = str(self.wiz_id)
        else:
            child_id = "%s.%s" % (child_id, self.wiz_id)
        self.parent_wizard._load_previous_answer_for_q(question, child_id)


    def _save_question_answser_for_future_run(self, question, child_id=None):
        '''Save question's answer for future runs
        
        @param question: Question to collect answer from
        @param child_id: ID of child Wizard if question was answered there
        '''
        # Pass answer up to parent
        if child_id is None:
            child_id = str(self.wiz_id)
        else:
            child_id = "%s.%s" % (child_id, self.wiz_id)
        self.parent_wizard._save_question_answser_for_future_run(question,
                                                                 child_id)
            
        
    
    # -- Cross-Wizard Value Passing ------------------------------------------
    
    def register_global(self, name, value):
        '''Save a value to be accessed by all wizards/sub wizards
        
        Value is saved only for this session
        
        @param name: Variable name
        @param value: Value to save
        '''
        self.parent_wizard.register_global(name, value)
        
        
    def get_global(self, name, required=True, default=None):
        '''Retrieve a value to be accessed by all wizards/sub wizards
        
        @param name: Variable name
        @param required: Will raise exception if value not registered
        @param default: Default value to return if not registered
        '''
        return self.parent_wizard.get_global(name, required, default)
                
        

    
    
        
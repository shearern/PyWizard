#!/usr/bin/python

import os
from pickle import dump, load
from abc import ABCMeta, abstractmethod

from .PyWizardBase import PyWizardBase
from py_wizard.questions.YesNoQuestion import YesNoQuestion


class PyMainWizard(PyWizardBase, metaclass=ABCMeta):
    '''The main/root wizard.
    
    This class represents the entire wizard, but may have sub-wizards attached
    to split up the wizard logic.
    '''
    
    
    def __init__(self):
        super(PyMainWizard, self).__init__()
        
        self.enable_answer_saving = False
        self.enable_autosave_answers = False
        self.enable_load_prev_answers = False
        
        self.__autosave_path = None
        self.__saved_answers = dict()
        self.__saved_answers_for_sub_wizards = dict()
        
        # Cross-Wizard Registry
        self._cross_wizard_reg = dict()
                
    
    @property
    def autosave_path(self):
        return self.__autosave_path


    # -- Main Execution ------------------------------------------------------
    
    def run_wizard(self):
        self.enable_answer_saving = False
        self.ask_presave_questions()
        self.configure_answer_saving()
        self.execute()
        self.ask_to_save()
        self.say_goodbye()
        
        
    @abstractmethod
    def execute(self):
        '''Hook for wizard to perform it's logic'''
        
    
    def say_goodbye(self):
        print("Wizard Finished")
    
    # -- Main Question Hooks -------------------------------------------------
    
    def ask_presave_questions(self):
        '''Hook to ask questions prior to saving answers'''
        pass
    
    
    # -- Answer Saving -------------------------------------------------------

    def _calc_autosave_path(self):
        '''Determine path for auto saving answers'''
        
        
    def _load_previous_answer_for_q(self, question, child_id=None):
        '''Load saved answer back into question
        
        @param question: Question to load any saved answers to
        @param child_id: ID of child Wizard question is going to be asked in 
        '''
        if self.enable_load_prev_answers:
            saved_answer = self._peak_saved_answer(question.name, child_id)
            if saved_answer is not None:
                question.previous_answer = saved_answer

                
    def _save_question_answser_for_future_run(self, question, child_id=None):
        '''Save question's answer for future runs
        
        @param question: Question to collect answer from
        @param child_id: ID of child Wizard if question was answered there
        '''
        if self.enable_answer_saving:
            answer_to_save = question.encode_answer_for_save()
            self._inject_saved_answer(question.name, answer_to_save, child_id)


    def configure_answer_saving(self):
        '''Setup answer saving for this run of the wizard'''
        
        # Determine path for loading/saving previous answers
        self.__autosave_path = self._calc_autosave_path()
        if self.__autosave_path is None:
            return
        path = os.path.abspath(self.__autosave_path)
        
        # Load Previous Saved Answers
        if os.path.exists(self.__autosave_path):
            msg = "Load previous answers from %s for defaults?"
            q = YesNoQuestion('load_saved', msg % (path), default=True)
            if self.ask_question(q):
                with open(path, "rb") as fh:
                    sa = load(fh)
                    self.__saved_answers = sa['self']
                    self.__saved_answers_for_sub_wizards = sa['subwizards']
                    self.enable_load_prev_answers = True
                    
        # Ask if we want to save after every answer
        msg = "Save answers back to %s after every question?"
        q = YesNoQuestion('autosave', msg % (path), default=True)
        self.enable_autosave_answers = self.ask_question(q)
        
        self.enable_answer_saving = True
                                

    def save_answers(self):
        '''Save answers to file'''
        if self.__autosave_path is not None:
            answers = {'self': self.__saved_answers,
                       'subwizards': self.__saved_answers_for_sub_wizards,
                       }
            with open(self.__autosave_path, "wb") as fh:
                dump(answers, fh)
        
                
    def ask_to_save(self):
        '''Ask user to save answers after the wizard has run'''
        
        # Skip if no path to save to
        if self.__autosave_path is None:
            return
        
        # Just save if we've been autosaving anyway
        if self.enable_autosave_answers:
            self.save_answers()
            return
        
        # Ask the user
        was = self.enable_answer_saving
        self.enable_answer_saving = False
        
        msg = None
        path = os.path.abspath(self.__autosave_path)
        if os.path.exists(path): 
            msg = "Overwrite %s and save these answers for next run?"
        else:
            msg = "Save these answers to %s to default for next run?"
        q = YesNoQuestion('save_answers_after_wizard', msg % (path),
                          default='yes')
        if q.self.ask_question(q):
            self.save_answers()
    
        self.enable_answer_saving = was
        
    
    def _inject_saved_answer(self, name, saved_value, child_id=None):
        '''Inject a saved answer into the internal dict
        
        @param name: Name of the question
        @param saved_value: Saved value.  Needs to be same type as question's
            encode_answer_for_save()
        @param child_id: ID of child wizard if saved for sub-wizard
        '''
        if child_id is None:
            self.__saved_answers[name] = saved_value
        else:
            key = (child_id, name)
            self.__saved_answers_for_sub_wizards[key] = saved_value
            
        if self.enable_autosave_answers:
            self.save_answers()
            
            
    def _peak_saved_answer(self, name, child_id=None):
        '''See value stored for saving for a question
        
        @param name: Name of the question
        @param child_id: ID of child wizard if saved for sub-wizard
        '''
        if child_id is None:
            if name in self.__saved_answers:
                return self.__saved_answers[name]
        else:
            key = (child_id, name)
            if key in self.__saved_answers_for_sub_wizards:
                return self.__saved_answers_for_sub_wizards[key]
            
    
    
    # -- Answer Handling ------------------------------------------------------
    
    def collect_all_parent_answers(self):
        '''Assemble answers from self and all parents'''
        return self.answers.copy()
    
    
    def debug_answers(self):
        '''Print out answers object'''
        for name in sorted(self.answers.keys()):
            print("%-20s => %s" % (name, self.answers[name]))
        
        
    # -- Cross-Wizard Value Passing ------------------------------------------
    
    def register_global(self, name, value):
        '''Save a value to be accessed by all wizards/sub wizards
        
        Value is saved only for this session
        
        @param name: Variable name
        @param value: Value to save
        '''
        self._cross_wizard_reg[name] = value
        
        
    def get_global(self, name, required=True, default=None):
        '''Retrieve a value to be accessed by all wizards/sub wizards
        
        @param name: Variable name
        @param required: Will raise exception if value not registered
        @param default: Default value to return if not registered
        '''
        if name in self._cross_wizard_reg:
            return self._cross_wizard_reg[name]
        elif required:
            raise IndexError("Global var not registered: '%s'" % (name))
        else:
            return default
                
        

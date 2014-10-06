#!/usr/bin/python

from abc import ABCMeta, abstractmethod

from py_wizard.questions.SimpleQuestion import  SimpleQuestion
from py_wizard.questions.IntQuestion import IntQuestion
from py_wizard.questions.YesNoQuestion import YesNoQuestion
from py_wizard.questions.CurrencyQuestion import CurrencyQuestion
from py_wizard.questions.NameQuestion import NameQuestion
from py_wizard.questions.DateQuestion import DateQuestion
from py_wizard.questions.ParagraphQuestion import ParagraphQuestion
from py_wizard.questions.SelectQuestion import SelectQuestion
from py_wizard.questions.ListQuestion import ListQuestion
from py_wizard.questions.ActionPrompt import ActionPrompt


class PyWizardBase(object):
    '''Base class for leading user through a set of questions'''
    __metaclass__ = ABCMeta

    def __init__(self):
        self.answers = dict()

        self._sub_wizards = dict()
        self._sub_wizard_order = list()

        # User Interface
        self.iface = None


    # -- Ask a question -------------------------------------------------------

    def ask_question(self, question):
        '''Ask a single question and then update wizard'''

        if self.iface is None:
            raise Exception("wizard.iface wasn't set")

        self._load_previous_answer_for_q(question)
        answer = self.iface.ask_question(question)
        self._update_wizard_after_question(question)
        self.print_question_separator()
        return answer


    def _update_wizard_after_question(self, question):
        '''Perform any wizard updates that should happen after a q is answered

        1) Collect answer into answers dict for quick access
        2) Save answer for future runs
        '''
        self._collect_question_answer(question)
        self._save_question_answser_for_future_run(question)


    def _collect_question_answer(self, question):
        # Save answer value for processing
        self.answers[question.name] = question.answer


    def print_question_separator(self):
        print ""


    def get_answer(self, question_name, default=None, required=False):
        '''Get the answer to a question already asked'''
        if not self.answers.has_key(question_name):
            if required:
                raise IndexError("Question not answer yet:" + question_name)
            else:
                return default
        return self.answers[question_name]


    # -- Interface -----------------------------------------------------------

    def inform_user(self, description):
        '''Inform the user of anything.

        Typically this will be akin to a print'''
        self.iface.inform_user(description)


    def inform_user_of_action(self, description):
        '''Inform the user of an action being performed'''
        self.iface.inform_user_of_action(description)



    # -- Sub Wizard Handling --------------------------------------------------

    def register_sub_wizard(self, wizard):
        '''Add a sub-wizard to run along side this wizard.

        This supports the breaking of a very large wizards into a set of
        sub-wizards.  Sub wizards are invoked by calling execute_sub_wizards().
        '''
        # Ensure Wizard ID is valid


        if self._sub_wizards.has_key(wizard.wiz_id):
            msg = "Sub Wizard with id %s already exists"
            raise IndexError(msg % (wizard.wiz_id))

        # Add sub-wizard
        self._sub_wizards[wizard.wiz_id] = wizard
        self._sub_wizard_order.append(wizard.wiz_id)


    def execute_sub_wizards(self, phase=None, wiz_filter=None):
        '''Call sub wizards to let them do their work

        If phase is None, then this will call execute() on all sub-wizards in
        the order that they were registered.  If phase is specified, then this
        will call execute_<phase>() on all sub-wizards

        @param parent: Reference to parent wizard (-> self.parent_wizard)
            This object will hold a reference to the parent wizard just
            for the duration of this method call.
        @param phase: The name of the phase, or None
        @param wiz_filter: Function to filter which sub-wizards to run
        '''
        parent = self

        # Default filter accepts all
        if wiz_filter is None:
            wiz_filter = lambda w: True

        # Execute wizard
        for wid in self._sub_wizard_order:
            wizard = self._sub_wizards[wid]
            if wiz_filter(wizard):
                wizard.execute_sub_wizard(parent, phase)


    # -- Cross-Wizard Value Passing ------------------------------------------

    @abstractmethod
    def register_global(self, name, value):
        '''Save a value to be accessed by all wizards/sub wizards

        Value is saved only for this session

        @param name: Variable name
        @param value: Value to save
        '''


    @abstractmethod
    def get_global(self, name, required=True, default=None):
        '''Retrieve a value to be accessed by all wizards/sub wizards

        @param name: Variable name
        @param required: Will raise exception if value not registered
        @param default: Default value to return if not registered
        '''


    # -- Answer handling -----------------------------------------------------

    @abstractmethod
    def collect_all_parent_answers(self):
        '''Assemble answers from self and all parents'''


    def collect_child_answers(self):
        '''Assemble answers from all children (recursive)'''
        answers = dict()
        for wiz in self._sub_wizards.values():
            for name, value in wiz.answers.items():
                answers[name] = value
            for name, value in wiz.collect_child_answers():
                answers[name] = value
        return answers


    # -- Answer Saving -------------------------------------------------------

    @abstractmethod
    def _load_previous_answer_for_q(self, question, child_id=None):
        '''Load saved answer back into question

        @param question: Question to load any saved answers to
        @param child_id: ID of child Wizard question is going to be asked in
        '''

    @abstractmethod
    def _save_question_answser_for_future_run(self, question, child_id=None):
        '''Save question's answer for future runs

        @param question: Question to collect answer from
        @param child_id: ID of child Wizard if question was answered there
        '''


    def load_saved_answers(self, autosaved_answers):
        '''Load answers back after that have been saved by

        The previous answers become defaults
        '''
        if autosaved_answers.has_key('self'):
            self.saved_answers = autosaved_answers['self']
        if autosaved_answers.has_key('subwizards'):
            self._saved_answers_for_sub_wizards = autosaved_answers['subwizards']


    # -- Question Helpers -----------------------------------------------------

    def ask_simple(self, name, question, default=None, optional=False, max_len=None):
        q = SimpleQuestion(name, question, default, max_len=max_len)
        if optional:
            q.optional(True)
        return self.ask_question(q)


    def ask_name(self, name, question, default=None, optional=False):
        q = NameQuestion(name, question, default)
        if optional:
            q.optional(True)
        return self.ask_question(q)


    def ask_int(self, name, question, default=None, optional=False,
                min_value=None, max_value=None):
        q = IntQuestion(name, question, default, min_value=min_value,
                        max_value=max_value)
        if optional:
            q.optional(True)
        return self.ask_question(q)


    def ask_yes_no(self, name, question, default=None, optional=False):
        q = YesNoQuestion(name, question, default)
        if optional:
            q.optional(True)
        return self.ask_question(q)


    def ask_date(self, name, question, format='%Y-%m-%d', default=None,
                 optional=False):
        q = DateQuestion(name, question, format, default)
        if optional:
            q.optional(True)
        return self.ask_question(q)


    def ask_currency(self, name, question, default=None, optional=False):
        q = CurrencyQuestion(name, question, default)
        if optional:
            q.optional(True)
        return self.ask_question(q)


    def ask_paragraph(self, name, question, default=None, optional=False):
        q = ParagraphQuestion(name, question, default)
        if optional:
            q.optional(True)
        return self.ask_question(q)


    def ask_select(self, name, question, options, default=None, optional=False,
                   if_many = False):
        q = SelectQuestion(name, question, options, default)

        if if_many:
            q.only_ask_if_many()

        if optional:
            q.optional(True)
        return self.ask_question(q)


    def ask_list(self, name, question, default=None, optional=False,
                 options=None):
        q = ListQuestion(name, question, default, options=options)
        if optional:
            q.optional(True)
        return self.ask_question(q)


    def ask_action(self, name, prompt):
        q = ActionPrompt(name, prompt)
        return self.ask_question(q)
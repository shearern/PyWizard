'''
Created on Mar 25, 2013

@author: nate
'''
from WizQuestion import WizQuestion

class SimpleQuestion(WizQuestion):
    '''A question that takes a single line of text as an answer'''
    
    def __init__(self, name, question, default=None, max_len=None):
        super(SimpleQuestion, self).__init__(name, default)
        self.__question_txt = question
        self.__max_len = max_len
        
    
    @property
    def question_txt(self):
        return self.__question_txt
#        
#        
#    # -- Common --------------------------------------------------------------
#        
#    def __calc_default_value(self):
#        if self.previous_answer is not None:
#            self.default = str(self.previous_answer)
#        
#        
    def get_validation_error(self, answer):
        if answer is None and not self.is_optional:
            return "Answer is required"
        if self.__max_len is not None:
            if len(answer) > self.__max_len:
                return "Answer must be less than %d chars" % (self.__max_len)
        return self.get_simple_question_child_error(answer)
    
    
    def get_simple_question_child_error(self, answer):
        '''Validate the 'native' answer for SimpleQuestion derived questions'''
        if self.__class__ is not SimpleQuestion:
            cname = self.__class__.__name__
            msg = "Child class %s needs to override %s()"
            raise NotImplementedError(msg % (cname,
                                             'get_simple_question_child_error'))
    
    
#    # -- Tk -------------------------------------------------------------------
#    
#    def build_tk_input(self, frame):
#        '''Build TK interface for asking this question
#        
#        @return dict: Wizard objects created to pass back to
#            validate_tk_input() and save_tk_input()
#        '''
#        widgets = dict()
#        
#        self.__calc_default_value()
#        
#        # Question Prompt
#        ttk.Label(frame, text=self.__question).grid(column=0, row=0)
#        
#        # Question Input
#        widgets['user_input'] = ttk.Entry(frame)
#        widgets['user_input'].grid(column=0, row=1)
#        if self.default is not None:
#            widgets['user_input'].insert(0, str(self.default))
#        
#        return widgets
#    
#    
#    def save_tk_input(self, widgets):
#        '''Save input from tk widgets to .user_answer
#        
#        @param widgets: Dictionary of widgets returned from build_tk_input()
#        '''
#        self.user_answer = widgets['user_input'].get()

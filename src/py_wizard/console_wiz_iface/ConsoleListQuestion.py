'''
Created on Sep 20, 2013

@author: nshearer
'''
from .ConsoleQuestionPresenter import ConsoleQuestionPresenter


class ConsoleListQuestion(ConsoleQuestionPresenter):
    
    def __init__(self, question):
        super(ConsoleListQuestion, self).__init__(question)
        self.user_answer = list()
    
    
    def _calc_default_answer_to_present_to_user(self):
        '''Get the default answer to present to the user'''
        default = self.question.calc_default_answer()
        
        # Format answer as a string:
        if default is not None:
            return self.decode_answer_to_text(default)
        
        else:
            return None
        

    def use_default_value(self):
        '''Specify that the default value should be used'''
        default = self.question.calc_default_answer()
        if default is None:
            default = list()
        self.user_answer = default
        
        
    def decode_answer_to_text(self, answer):
        '''Given a previous or default answer, convert it to a text value'''
        if answer is None or len(answer) == 0:
            return None
        return ', '.join(answer)      
        
        
    # -- Question Presenter ---------------------------------------------------
    
    def present_question(self):
        
        question_txt = self.question.question_txt
            
        print(question_txt)
        
        default_answer = self.question.calc_default_answer()
        if default_answer is not None:
            if len(default_answer) > 0:
                print("-- Default Value: --")
                for item in default_answer:
                    print(" -", item)
                print("--------------------")
            
        print("Enter Items one per line")
        print("Enter blank line to end the list. ", end=' ')
        print("Enter [blank] to answer with a blank list")
        print("")
        
        
    def get_validation_error_for_user_answer(self, user_answer):
        '''See if user answer validates.
        
        List items are any string, so they always validate
        '''
        return None
    
    def handle_validation_error(self):
        self.user_answer = list()
        

    # -- Input handling -------------------------------------------------------
    
    
    def handle_blank_line(self):
        '''Respond to a blank line of input from the user.
        
        For lists, this ends the list input
        
        @return bool: Request more input from user?
        '''
        # If no items given, use default value
        if self.user_answer is None or len(self.user_answer) == 0:
            print("Using default")
            self.use_default_value()
            
        return False
        
    
    def handle_answer_line(self, line):
        '''Process user answer
        
        Keep accepting input lines.  Input is terminated by [end] command.
        
        @return bool: Request more input from user?
        '''
        self.user_answer.append(line.strip())
        return True
        

    def list_commands(self):
        commands = super(ConsoleListQuestion, self).list_commands()
        commands['[blank]'] = "Use an empty list"

        
    def handle_command(self, command):
        '''Handle a command
        
        For list, use [blank] to specify an empty list
        
        @return bool: Request more input from user?
        '''
        if command == '[blank]':
            print("Using a blank list")
            self.user_answer = list()
            return False
        
        else:
            return super(ConsoleListQuestion, self).handle_command(command)
        
        
    

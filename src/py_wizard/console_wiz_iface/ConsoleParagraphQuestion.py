'''
Created on Sep 20, 2013

@author: nshearer
'''
from ConsoleQuestionPresenter import ConsoleQuestionPresenter

class ConsoleParagraphQuestion(ConsoleQuestionPresenter):
    

    def _calc_default_answer_to_present_to_user(self):
        '''Get the default answer to present to the user'''
        return self.question.calc_default_answer()
        
    
    def present_question(self):
        question_txt = self.question.question_txt
        
        default_answer = self._calc_default_answer_to_present_to_user()
            
        print question_txt
        
        if default_answer is not None:
            print "-- Default Value: --"
            print default_answer
            print "--------------------"
            
        print "Enter [end] when finished"
        
        
    def get_validation_error_for_user_answer(self, user_answer):
        '''See if user answer validates.
        
        Paragraphs are any string, so they always validate
        '''
        return None        
        
        
    # -- Input handling -------------------------------------------------------
    
    
    def handle_blank_line(self):
        '''Respond to a blank line of input from the user.
        
        For paragraphs, use default if very first line is blank, else parse
        normally
        
        @return bool: Request more input from user?
        '''
        
        # Use special actions if first line is blank
        default_answer = self._calc_default_answer_to_present_to_user()
        if self.user_answer is None or len(self.user_answer.strip()) == 0:
            
            # Use default if exists
            if default_answer is not None:
                print "Using default"
                self.use_default_value()
                return False
            
            # Else, make value blank
            self.user_answer = ""
            return False
        
        # Else, handle as paragraph input
        else:
            return self.handle_answer_line('')
        
            
        
    def handle_answer_line(self, line):
        '''Process user answer
        
        Keep accepting input lines.  Input is terminated by [end] command.
        
        @return bool: Request more input from user?
        '''
        if self.user_answer is None:
            self.user_answer = line
        else:
            self.user_answer += "\n" + line
        
        return True


    def list_commands(self):
        commands = super(ConsoleParagraphQuestion, self).list_commands()
        commands['[end]'] = "End input"


    def handle_command(self, command):
        '''Handle a command
        
        @return bool: Request more input from user?
        '''
        if command == '[end]':
            return False
        else:
            return super(ConsoleParagraphQuestion, self).handle_command(command)

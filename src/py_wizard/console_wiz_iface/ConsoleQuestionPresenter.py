'''
Created on Jul 9, 2013

@author: nshearer
'''
import re
from abc import ABCMeta, abstractmethod
import gflags

from py_wizard.questions.QuestionPresenter import QuestionPresenter


gflags.DEFINE_boolean('auto_accept_defaults',
    short_name = 'D',
    help = "Accept default values without prompting",
    default = False)

gflags.DEFINE_boolean('auto_accept_prev',
    short_name = 'P',
    help = "Accept previous values without prompting",
    default = False)


class ConsoleQuestionPresenter(QuestionPresenter):
    '''Question presenter base class for console interface'''
    __metaclass__ = ABCMeta
    
    BLANK_LINE='line'
    ANSWER_LINE='answer'
    COMMAND_LINE='cmd'
    
    def __init__(self, question):
        super(ConsoleQuestionPresenter, self).__init__(question)
        self.user_answer = None     # Answer in text from user

    
    def ask(self):
        '''Ask the question of the user (and perform validation)'''
        
        # Keep asking until answer validates successfully
        answer = None
        answer_validates = False
        while not answer_validates:
            
            # Present Question
            self.present_question()
            
            # Get User Input
            request_more_input=True
            while request_more_input:
                
                line = None
                
                # Auto-accept previous answer
                if gflags.FLAGS.auto_accept_prev:
                    if self.question.previous_answer is not None:
                        msg ="Auto accepting default because of "
                        print msg + " --auto_accept_prev"
                        line = ""
                
                # Auto-accept default if requested
                if gflags.FLAGS.auto_accept_defaults:
                    user_default = self._calc_default_answer_to_present_to_user()
                    if user_default is not None:
                        msg ="Auto accepting default because of "
                        print msg + " --auto_accept_defaults"
                        line = ""
                        
                # Else, get input from the user
                if line is None:
                    line = self.get_input_line()
                
                line_type = self.determine_input_line_type(line)
                if line_type == self.COMMAND_LINE:
                    request_more_input = self.handle_command(line)
                elif line_type == self.BLANK_LINE:
                    request_more_input = self.handle_blank_line()
                elif line_type == self.ANSWER_LINE:
                    request_more_input = self.handle_answer_line(line)
                else:
                    raise Exception("Unknown line type: '%s'" % (line_type))
                
            # Validate User Input
            answer = self.user_answer
            validate_error = self.get_validation_error_for_user_answer(answer)
            if validate_error is not None:
                self.present_validation_error(validate_error)
                self.handle_validation_error()
                answer = None
                answer_validates = False
                continue
                
            # Validate Native Answer (example, after "yes" becomes True)
            answer = self.encode_answer_to_native(self.user_answer)
            validate_error = self.question.get_validation_error(answer)
            if validate_error is not None:
                self.present_validation_error(validate_error)
                self.handle_validation_error()
                answer = None
                answer_validates = False
                continue
            else:
                answer_validates = True
            
        # Save answer
        if answer is not None:
            self.question.set_answer(answer)
            
            
        
    
    
    # -- Common Subclass Overrides --------------------------------------------

    
    @abstractmethod
    def present_question(self):
        '''Get answer from the user and return user'''
        cname = self.__class__.__name__
        msg = "Subclass %s needs to implement %s()"
        raise Exception(msg % (cname, 'present_question'))

        
    def get_input_line(self):
        '''Get answer from the user'''
        return raw_input("> ").rstrip()


    CMD_PAT = re.compile(r'^\[.*\]$')
    def determine_input_line_type(self, line):
        '''Determine what kind of input the user supplied'''
        if len(line) == 0:
            return self.BLANK_LINE
        elif self.CMD_PAT.match(line):
            return self.COMMAND_LINE
        else:
            return self.ANSWER_LINE
        
    
    def handle_command(self, command):
        '''Handle a command
        
        @return bool: Request more input from user?
        '''
        if command == '[help]':
            # Print Commands
            commands = self.list_commands()
            if commands is None:
                commands = dict()
            
            # Determine Padding for commands
            command_pad = 0
            for cmd in sorted(commands.keys()):
                command_pad = max(command_pad, len(cmd))
                
            # Print Commands
            print "Available commands for this question:"
            msg_pat = "%%-%ds %%s" % (command_pad)
            for cmd in sorted(commands.keys()):
                print msg_pat % (cmd, commands[cmd])
                
            return True
                
        elif command == '[blank]':
            print "Clearing answer"
            self.answer = None
            
            return True
            
        elif command == '[default]':
            default_answer = self._calc_default_answer_to_present_to_user()
            print "Using default answer: %s" % (default_answer)
            self.use_default_value()
            
            return False
        
        
    def handle_blank_line(self):
        '''Respond to a blank line of input from the user.
        
        Default behaviour is to use the default value
        
        @return bool: Request more input from user?
        '''
        default_answer = self._calc_default_answer_to_present_to_user()
        if default_answer is not None:
            print "Using default:", default_answer
            self.use_default_value()
            return False
        else:
            return self.handle_answer_line('')
        
        
        
    def handle_answer_line(self, line):
        '''Process user answer
        
        Default behaviour is to set as the user answer
        
        @return bool: Request more input from user?
        '''
        self.user_answer = line
        return False
    
    
    @abstractmethod
    def _calc_default_answer_to_present_to_user(self):
        '''Get the default answer to present to the user
        
        Should be a string in the format that can be input directly
        '''


    def _calc_default_answer(self):
        '''Default that should be used if no answer is given'''
        return self.question.calc_default_answer()
            

    def use_default_value(self):
        '''Specify that the default value should be used'''
        self.user_answer = self._calc_default_answer_to_present_to_user()
        
            
            
    def list_commands(self):
        return {'[help]': "Display commands that can be used",
                '[blank]': "Blank the answer to start over",
                '[default]': "Use the default value"
                }
        
        
    @abstractmethod
    def get_validation_error_for_user_answer(self, user_answer):
        '''Like get_validation_error(), but before encode_answer_to_native()'''
        cname = self.__class__.__name__
        msg = "Subclass %s needs to implement %s()"
        raise Exception(msg % (cname, 'get_validation_error_for_user_answer'))


    def present_validation_error(self, error):
        print "!! Answer failed validation:", error
        

    def handle_validation_error(self):
        self.user_answer = None


    def encode_answer_to_native(self, user_answer):
        '''Return answers formatted to save in answer object'''
        if user_answer is None or len(str(user_answer)) == 0:
            return None
        return user_answer



'''
Created on Jul 9, 2013

@author: nshearer
'''

class QuestionPresenter(object):
    '''Contains code to interact with user to answer a question'''
    
    def __init__(self, question):
        self.__question = question
        
        
    @property
    def question(self):
        return self.__question
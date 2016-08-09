'''
Created on Jul 9, 2013

@author: nshearer
'''
from py_wizard.console_wiz_iface.ConsoleInterface import ConsoleInterface

def run_wizard(wizard, iface=None):
    
    # Default to Console interface
    if iface is not None:
        wizard.iface = iface
    if wizard.iface is None:
        wizard.iface = ConsoleInterface()
    
    wizard.run_wizard()


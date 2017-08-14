'''The module docstring appears at the top of the file

PEP 257 defines the details of the docstring
'''

class DocumentMe():
    '''The class docstring follows the same rules'''

    def __init__(self):
        '''Method docstring can also be used'''
        self.text = '''triple quoted string can also be
used to hold formatted
dtring'''

def funk():
    '''Normal functions should have docstrings too.'''
    pass

'''Docstrings can be used as long comments as well.'''
print('The module docstring:',__doc__)
print('The class docstring:',DocumentMe.__doc__)
print('A method docstring:',DocumentMe.__init__.__doc__)
print('A function docstring:',funk.__doc__)
print('Docstring are used by python\'s help function:')
help(__name__)
help(DocumentMe)
help(funk)

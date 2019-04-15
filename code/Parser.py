from tkinter import messagebox
#import UserInterface

class Parser:
    def __init__(self, text = None):
        self._args = []
        self._text = text
        self._letters = None
        self._caution = False
        self._string = True
        self._substring = None
        
    def testForString(self):
        if '<*' and '*>' or '<\\' and '/>' in self._text:
            saveSubstring = self._text[:self._text.index('<*')]
            self._substring = self._text[self._text.index('*>')+2:] + saveSubstring
            self._letters = self._text[self._text.index('<*')+2:self._text.index('*>')]
        print(self._text)
        print(self._letters)
        print(self._substring)
        
Parser('test<*string*>test1<*string1*>').testForString()

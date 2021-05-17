# built using python 3.8.5
import os
import re
from pathlib import Path
#from warnings import resetwarnings
#import sys

class Spellchecker():

    def __init__(self, wordFile: str=''):
        self._path = None
        self._words = None
        self._wordList = None
        self.wordList = wordFile
        self.create_wordList()

    # setter method for word list
    def open_wordFile(self, wordFile):
        self._path = Path(os.path.dirname(__file__)).parent
        wordfiles_path = self._path / 'wordfiles'
        file = wordfiles_path / wordFile
        if not file.is_file():
            raise WordFileNotFoundException("Word file " + wordFile + " can not be found")
        self._words = open(file).read()
    
    # create word list from file object
    def create_wordList(self):
        #words_string = self._words.read()
        #self._wordList = words_string.splitlines()
        self._wordList = self._words.splitlines()

    # getter of word list
    def view_wordList(self):
        return self._wordList
    
    wordList = property(view_wordList, open_wordFile)

    def checkWord(self, wordToCheck: 'str') -> 'str':
        
        if wordToCheck in self._wordList:
            return wordToCheck
        
        if wordToCheck.lower() in self._wordList:
            return wordToCheck.lower()
        
        proper_noun = wordToCheck[0].upper() + wordToCheck[1:].lower()
        if proper_noun in self._wordList:
            return proper_noun

        possible_dups = self.checkDupChars(wordToCheck)
        if possible_dups[0]:
            return self.checkWord(possible_dups[1])

        return "No Correction Found"

    def checkDupChars(self, charsToCheck: 'str') -> 'tuple[bool, str]':
        prefix = r''
        dups = False
        for c in charsToCheck:
            test_prefix = prefix + c
            match_results = re.findall(test_prefix + r'.*', self._words)
            if len(match_results) == 0:
                if prefix[-1] == c:
                    dups = True
                continue
            prefix = test_prefix[:]
        return (dups, prefix)
    
class WordFileNotFoundException(Exception):
        ''' Exception raised when spellchecker can not find supplied word list '''
# Copyright 2021, James Morren, All rights reserved
# built using python 3.8.5
import os, re
from pathlib import Path

class Spellchecker():
    '''
    This class creates a Spellchecker object
    Object takes an optional string value representing the name of a word file.
    The word files are expected to be located in a folder 'wordfiles' adjacent
    to the working directory of the spellchecker module.
    '''

    def __init__(self, wordFile: str=''):
        self._path = None
        self._wordList = None
        self.wordList = wordFile

    # Setter method for word list
    def open_wordFile(self, wordFile):
        self._path = Path(os.path.dirname(__file__)).parent
        wordfiles_path = self._path / 'wordfiles'
        file = wordfiles_path / wordFile
        if not file.is_file():
            raise WordFileNotFoundException("Word file " + wordFile + " can not be found")
        self._wordList = open(file).read()

    # Getter method for word list
    def view_wordList(self):
        return self._wordList
    
    # Word list property
    wordList = property(view_wordList, open_wordFile)

    # checkWord function
    def checkWord(self, wordToCheck: 'str') -> 'str':
        # Checking cases involving capitalization
        if self.wordLookup(wordToCheck):
            return wordToCheck
        if self.wordLookup(wordToCheck.lower()):
            return wordToCheck.lower()
        if self.wordLookup(wordToCheck.lower().title()):
            return wordToCheck.lower().title()
        # Checking cases involving additioal characters
        possible_dups = self.checkDupChars(wordToCheck)
        if possible_dups[0]:
            return self.checkWord(possible_dups[1])
        # Word has failed all cases
        return "No Correction Found"
    
    # Look up word in word list using Regular Expressions
    def wordLookup(self, wordToCheck: 'str') -> 'bool':
        raw_word = r'\b' + wordToCheck + r'\b'
        match_results = re.findall(raw_word, self.wordList)
        return len(match_results) == 1

    # Checking for duplicate characters in word using Regular Expressions
    def checkDupChars(self, charsToCheck: 'str') -> 'tuple[bool, str]':
        prefix = r''
        dups = False
        # Builds a word character at a time an monitor Reg Exp result and
        # determines extra characters if no results return and prunes character.
        # Flags if duplicate characters are found to check new word, word will
        # be deemed to have no correction if no duplicates are found.
        for c in charsToCheck:
            test_prefix = prefix + c
            match_results = re.findall(test_prefix + r'.*', self.wordList)
            if len(match_results) == 0:
                if prefix[-1] == c:
                    dups = True
                continue
            prefix = test_prefix[:]
        return (dups, prefix)
    
class WordFileNotFoundException(Exception):
        ''' Exception raised when spellchecker can not find supplied word list '''
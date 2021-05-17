# built using python 3.8.5
import os
from pathlib import Path
from warnings import resetwarnings
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
        self._words = open(file)
    
    # create word list from file object
    def create_wordList(self):
        words_string = self._words.read()
        self._wordList = words_string.splitlines()

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
            for w in possible_dups[1]:
                result = self.checkWord(w)
                if result != "No Correction Found":
                    return result

        return "No Correction Found"
    
    def checkDupChars(self, charsToCheck: 'str') -> 'tuple[bool, list[str]]':
        seen = dict()
        # counting the number of 
        last_char = ''
        dups = False
        for c in charsToCheck:
            if c == last_char:
                chars_seen = seen.keys()
                if c in chars_seen:
                    seen.update({c: seen.get(c) + 1})
                    continue
                seen.update({c: 2})
            last_char = c
        
        possible_fixes = list()
        chars_seen = seen.keys()
        for k in chars_seen:
            if seen.get(k) > 1:
                dups = True
                remove_char = charsToCheck.partition(k)
                possible_fixes.append(remove_char[0] + remove_char[2])

        return (dups, possible_fixes)
        
    
class WordFileNotFoundException(Exception):
        ''' Exception raised when spellchecker can not find supplied word list '''
                



''' Prototyping checkWord function '''
# dev_wrd_lst_short = ['hello', 'goodbye', 'world', 'sea', 'moon', 'universe', 'Elvis']

# wrd_lst = dev_wrd_lst_short

# wrd_lst.sort()

# def checkWord_prototype(wordToCheck: str) -> str:
#     result = ''
#     #lowerCase = wordToCheck.lower()
#     if wordToCheck in wrd_lst:
#         return wordToCheck
#     if wordToCheck.lower() in wrd_lst:
#         return wordToCheck.lower()
#     proper_noun = wordToCheck[0].upper() + wordToCheck[1:].lower()
#     if proper_noun in wrd_lst:
#         return proper_noun
#     else:
#         return "No Correction Found"
# built using python 3.8.5
import os
from pathlib import Path
#import sys

class Spellchecker():

    def __init__(self, word_dict: str):
        self.word_dict = word_dict
        self.path = Path.cwd()
        self.words = None
        self.find_dictFile()

    # look for word dictionary
    def find_dictFile(self):
        #search current dir
        file = self.path / self.word_dict
        if self.path.exists:
            if not file.is_file():
                raise WordFileNotFoundException("Word file " + self.word_dict + " can not be found")
            self.words = open(file)
            # try:
            #     # if self.path.exists and file.is_file():
            #     #     return open(file)
            #     #subDir = self.path.
            #     open(file)
            # except FileNotFoundError as err:
            #     print('Error: ', err)
    
class WordFileNotFoundException(Exception):
        ''' Exception raised when spellchecker can not find supplied word list '''
                




dev_wrd_lst_short = ['hello', 'goodbye', 'world', 'sea', 'moon', 'universe', 'Elvis']

wrd_lst = dev_wrd_lst_short

wrd_lst.sort()

def checkWord(wordToCheck: str) -> str:
    result = ''
    #lowerCase = wordToCheck.lower()
    if wordToCheck in wrd_lst:
        return wordToCheck
    if wordToCheck.lower() in wrd_lst:
        return wordToCheck.lower()
    proper_noun = wordToCheck[0].upper() + wordToCheck[1:].lower()
    if proper_noun in wrd_lst:
        return proper_noun
    else:
        return "No Correction Found"
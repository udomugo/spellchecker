import importlib
import os
from pathlib import Path

utils = importlib.import_module('.spellchecker', package='utils')
sc = utils.Spellchecker('words')
userInput = ''
print("Welcome to CLI spellchecker.")
while userInput != 'quit!':
    userInput = input("Enter word to check: ")
    if userInput == 'quit!':
        continue
    result = sc.checkWord(userInput)
    if result == userInput:
        print("Word is correct")
        continue
    print(result)

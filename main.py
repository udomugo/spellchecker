import importlib
from pathlib import Path

def main_cli():
    utils = importlib.import_module('.spellchecker', package='utils')
    sc = utils.Spellchecker('words')
    userInput = ''
    print("Welcome to CLI spellchecker.")
    while userInput != 'quit!':
        
        userInput = input("Enter word to check or enter 'quit!' to exit:\n")
        if userInput == 'quit!':
            continue
        result = sc.checkWord(userInput)
        if result == userInput:
            print("Word is correct\n")
            continue
        print("Corrected word to: " + result + '\n')

if __name__ == '__main__':
    main_cli()

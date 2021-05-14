import importlib

try:
    utils = importlib.import_module('.spellchecker', package='utils')
except ImportError as err:
    print('Error: ', err)

def test_correct_spelling():
    assert utils.checkWord("hello") == "hello"
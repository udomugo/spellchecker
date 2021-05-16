import importlib
import pytest

try:
    utils = importlib.import_module('.spellchecker', package='utils')
except ImportError as err:
    print('Error: ', err)

@pytest.fixture
def spam_wrds():
    spam_wrds = open('spam.txt')
    return spam_wrds.read()

# Testing pytest fixtures
def test_spam_wrds(spam_wrds):
    assert spam_wrds == 'Hello, world!\naaa\nbbb\nadd\n'

''' Testing the creation of the spellchecker object '''
def test_create_spellchecker_badFile():
    with pytest.raises(utils.WordFileNotFoundException) as e_info:
        utils.Spellchecker('fileDoesNotExist.txt')
    assert "Word file fileDoesNotExist.txt can not be found"
    assert e_info.type == utils.WordFileNotFoundException

def test_create_spellchecker_fileExists():
    try:
        utils.Spellchecker('spam.txt')
    except Exception as e_info:
        assert False, f"'utils.Spellchecker' raised an exception {e_info}"

def test_read_spellchecker_wordFile(spam_wrds):
    spcheck = utils.Spellchecker('spam.txt')
    assert spcheck.words.read() == spam_wrds


# Testing checkWord function
def test_correct_spelling():
    assert utils.checkWord("hello") == "hello"

def test_corrected_capitalization():
    assert utils.checkWord("Hello") == "hello"

def test_uppercase_chars():
    assert utils.checkWord("heLLo") == "hello"

def test_properNoun():
    assert utils.checkWord("Elvis") == "Elvis"

def test_no_corrections():
    assert utils.checkWord("Jello") == "No Correction Found"

# def test_extra_chars():
#     assert utils.checkWord("helllo") == "hello"


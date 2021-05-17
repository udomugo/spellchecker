import importlib
import pytest

try:
    utils = importlib.import_module('.spellchecker', package='utils')
except ImportError as err:
    print('Error: ', err)

@pytest.fixture
def spamList():
    spamList = open('wordfiles/spam.txt')
    return spamList.read().splitlines()

@pytest.fixture
def wordsList():
    wordsList = open('wordfiles/words')
    return wordsList.read().splitlines()

@pytest.fixture
def spam_spellcheck():
    spam_spellcheck = utils.Spellchecker('spam.txt')
    return spam_spellcheck

@pytest.fixture
def words_spellcheck():
    words_spellcheck = utils.Spellchecker('words')
    return words_spellcheck

# Testing pytest fixtures
def test_spam_spellcheck(spam_spellcheck, spamList):
    assert spam_spellcheck.wordList == spamList

def test_words_spellcheck(words_spellcheck, wordsList):
    assert words_spellcheck.wordList == wordsList


# Testing the creation of the spellchecker object
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

def test_read_spellchecker_wordFile(spamList):
    spcheck = utils.Spellchecker('spam.txt')
    assert spcheck.wordList == spamList


# Testing checkWord function
def test_correct_spelling(words_spellcheck):
    assert words_spellcheck.checkWord("hello") == "hello"

def test_corrected_capitalization(words_spellcheck):
    assert words_spellcheck.checkWord("Hello") == "hello"

def test_uppercase_chars(words_spellcheck):
    assert words_spellcheck.checkWord("heLLo") == "hello"

def test_properNoun(words_spellcheck):
    assert words_spellcheck.checkWord("Elvis") == "Elvis"

def test_no_corrections(words_spellcheck):
    assert words_spellcheck.checkWord("Jello") == "No Correction Found"

def test_extra_chars(words_spellcheck):
    assert words_spellcheck.checkWord("helllo") == "hello"

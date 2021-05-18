# built using pytest-4.6.9, py-1.8.1
# pytest fixtures require that word list 'words' exist in '/projectRoot/wordfiles'
import importlib, pytest, os

from pathlib import Path

try:
    utils = importlib.import_module('.spellchecker', package='utils')
except ImportError as err:
    print('Error: ', err)

projectRoot = Path(os.path.dirname(__file__)).parent

@pytest.fixture
def spamList():
    spamList = open(projectRoot / 'wordfiles' / 'spam.txt')
    return spamList.read()

@pytest.fixture
def wordsList():
    wordsList = open(projectRoot / 'wordfiles' / 'words')
    return wordsList.read()

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

def test_checkDupChars(words_spellcheck):
    assert words_spellcheck.checkDupChars("helllo")[0] == True

def test_extra_chars_helllo(words_spellcheck):
    assert words_spellcheck.checkWord("helllo") == "hello"

def test_noExtra_chars_parallel(words_spellcheck):
    assert words_spellcheck.checkWord("parallel") == "parallel"

def test_noExtra_chars_MS(words_spellcheck):
    assert words_spellcheck.checkWord("Mississippi") == "Mississippi"

def test_noExtra_chars_simple(words_spellcheck):
    assert words_spellcheck.checkWord("I") == "I"

def test_extra_chars_simple(words_spellcheck):
    assert words_spellcheck.checkWord("II") == "I"

# Stress testing duplicate character detection
def test_extra_chars_MS1(words_spellcheck):
    assert words_spellcheck.checkWord("Miississippi") == "Mississippi"

def test_extra_chars_MS2(words_spellcheck):
    assert words_spellcheck.checkWord("Miissiissippi") == "Mississippi"

def test_extra_chars_MS3(words_spellcheck):
    assert words_spellcheck.checkWord("Miissiissiippi") == "Mississippi"

def test_extra_chars_MS4(words_spellcheck):
    assert words_spellcheck.checkWord("Miissiissiippii") == "Mississippi"

def test_extra_chars_MS5(words_spellcheck):
    assert words_spellcheck.checkWord("Miisssiissiippii") == "Mississippi"

def test_extra_chars_MS6(words_spellcheck):
    assert words_spellcheck.checkWord("Miisssiisssiippii") == "Mississippi"

def test_extra_chars_MS7(words_spellcheck):
    assert words_spellcheck.checkWord("Miisssiisssiipppii") == "Mississippi"

def test_extra_chars_MS8(words_spellcheck):
    assert words_spellcheck.checkWord("Mmiisssiisssiipppii") == "Mississippi"

def test_extra_chars_MS9(words_spellcheck):
    assert words_spellcheck.checkWord("MMiisssiisssiipppii") == "Mississippi"

def test_garbage_input(words_spellcheck):
    assert words_spellcheck.checkWord("kas;djkhfaw;osuihjklsdh;flish;fgjkha;sojdhfblskjfhl;as") == "No Correction Found"
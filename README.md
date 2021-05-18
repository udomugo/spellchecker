James Morren - Application Homework Submission

Spec:
# Ripl Spell-checker

To complete the new Ripl spell-checking software, we need you to create its brain. The requirements for this version are listed below. If you have any questions about any part of the task, please let us know.

### Requirements

Using a language of your choice, write a function that implements the following pseudo-code signature:

`String checkWord( String wordToCheck )`

The function should behave as follows:
* It will correct two kinds of errors on the incoming word and then return the corrected word:
    * It fixes bad casing.
        * “wetumpka” → “Wetumpka”
        * “paRNAssus” → “Parnassus”
    * It removes invalid repeating characters.
        * “tabble” → “table”
        * “rrreally” → “really”
* If the incoming word is already correct, the function should return the original word.
* If the incoming word is not correct and no correction can be found, the function should return the string “No Correction Found”.

The list of correct word spellings are in the dictionary file that is in this repo. (Uncompress the file before using it.) You don't need to perform corrections on any words not in this dictionary.

If you have any questions, please let us know.

### Packaging and Delivery

Please send the source code in a ZIP file, or similar format. If you use any libraries, please ensure we can get the exact versions you used. Please tell us anything that you think we should know about compiling or using your code.


## Planning:
### Cases to cover:
* When to Capitalize the first letter
* How to decide there are additional characters

### What to return (rough flow control):
* Correctly spelled words
* Correctly spelled words, incorrect capitalization
	* First char needs to be capitalized
	* Any char following the first char needs to be lower case
	* The following two cases are both true
* Incorrectly spelled words:
	* Missing chars need to be added
	* Additional chars need to be removed
	* The following two cases are both true

### Setting up project
Project was built with python 3.8.5 but should work for any version of python > 3.7
The following commands can be run all together if running in a fresh python environment:
> :~/projects$ git clone https://github.com/udomugo/spellchecker.git && cd spellchecker && mkdir wordfiles && gzip -dc words.gz > ./wordfiles/words && pip install -U pytest

Clone github repo:
> :~/projects$ git clone https://github.com/udomugo/spellchecker.git

Change to project directory and wordfiles directory:
> :~/projects$ cd spellchecker<br>
> :~/projects/spellchecker$ mkdir wordfiles

Unzip compressed word list:
> :~/projects/spellchecker$ gzip -dc words.gz > ./wordfiles/words

Install pytest:
> :~/projects/spellchecker$ pip install -U pytest

### Running test suite
At project root directory run command:
> :~/projects/spellchecker$ pytest-3 -v

### Running the CLI
At project root directory run command:
> :~/projects/spellchecker$ python3 main.py

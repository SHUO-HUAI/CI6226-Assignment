# Linguistic Modules
# perform two simple linguistic transformations on tokens: removing all punctuation symbols and lowercasing and stemming
# Input: list of pairs < token , document id >
# Output: list of pairs < modified token , document id >

from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from Directory_Listing import listFiles
from File_Reading import getFileContents
from Tokenization import generateTokens
from CONST import *
import re

portStemmer = PorterStemmer()
snowStemmer = SnowballStemmer("english")


def remove_punctuation_symbols(tokenPair):
    """
        remove the !@#$%^&*()-_=+'`~ ":;|/.,?[]{}<> symbols
    """
    for item in tokenPair:
        temp_item = str(item[0])
        item[0] = temp_item.lower()
        item[0] = re.sub(r'[\^\[\]\-\\!@#$%&*()_=+`~":;|/.,?{}<>\']', '', item[0])


def PortStem(tokenPair):
    return [(portStemmer.stem(token), docID) for token, docID in tokenPair]


def SnowStem(tokenPair):
    return [(snowStemmer.stem(token), docID) for token, docID in tokenPair]


if __name__ == "__main__":
    # Standalone test
    fileList = listFiles(rootDir)
    fileContent = getFileContents(fileList[0])
    tokenPair = generateTokens(fileContent, fileList[0])

    remove_punctuation_symbols(tokenPair)
    print(tokenPair)

    portStemTokenPair = PortStem(tokenPair)
    print(portStemTokenPair)

    snowStemTokenPair = SnowStem(tokenPair)
    print(snowStemTokenPair)

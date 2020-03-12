# Linguistic Modules
# perform two simple linguistic transformations on tokens: removing all punctuation symbols and lowercasing and stemming
# Input: list of pairs < token , document id >
# Output: list of pairs < modified token , document id >

from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from Directory_Listing import ListFiles
from File_Reading import GetFileContents
from Tokenization import GenerateTokens
from CONST import *
import re

portStemmer = PorterStemmer()
snowStemmer = SnowballStemmer("english")


def RemovePuncSymls(tokenPair):
    """
        remove the !@#$%^&*()-_=+'`~ ":;|/.,?[]{}<> symbols
    """
    for item in tokenPair:
        str_tmp = str(item[0])
        item[0] = str_tmp.lower()
        item[0] = re.sub(r'[\^\[\]\-\\!@#$%&*()_=+`~":;|/.,?{}<>\']', '', item[0])


def PortStem(tokenPair):
    return [(portStemmer.stem(token), docID) for token, docID in tokenPair]


def SnowStem(tokenPair):
    return [(snowStemmer.stem(token), docID) for token, docID in tokenPair]


def LingStr(token):
    tmp = re.sub(r'[\^\[\]\-\\!@#$%&*()_=+`~":;|/.,?{}<>\']', '', str(token).lower())
    tmp = portStemmer.stem(str(tmp))
    tmp = snowStemmer.stem(str(tmp))
    return tmp


def LingModule(tokenPair):
    return [(LingStr(token), docID) for token, docID in tokenPair]


if __name__ == "__main__":
    # Standalone test
    fileList = ListFiles(rootDir)
    fileContent = GetFileContents(fileList[0])
    tokenPair = GenerateTokens(fileContent, fileList[0])

    #RemovePuncSymls(tokenPair)
    #print(tokenPair)

    #portStemTokenPair = PortStem(tokenPair)
    #print(portStemTokenPair)

    #snowStemTokenPair = SnowStem(portStemTokenPair)
    #print(snowStemTokenPair)

    outputPair = LingModule(tokenPair)
    print(outputPair)
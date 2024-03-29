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


def LingStr(token):
    tmp = re.sub(r'[\^\[\]\-\\!@#$%&*()_=+`~":;|/.,?{}<>\']', '', str(token).lower())
    tmp = portStemmer.stem(str(tmp))
    tmp = snowStemmer.stem(str(tmp))
    return tmp


def LingModule(tokenPair):
    pairList = []
    for token, docID in tokenPair:
        tmp = LingStr(token)
        if tmp != "":
            pairList.append((tmp,docID))

    return pairList


if __name__ == "__main__":
    # Standalone test
    fileList = ListFiles(rootDir)
    fileContent = GetFileContents(fileList[0])
    tokenPair = GenerateTokens(fileContent, fileList[0])

    outputPair = LingModule(tokenPair)
    print(outputPair)

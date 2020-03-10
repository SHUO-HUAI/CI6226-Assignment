# Tokenization
# Input: text (file contents), string (document id = path to file)
# Output: list of pairs < string (token) , string (document id) >

from CONST import *
import re
import itertools
from File_Reading import getFileContents
def generateTokens(contents, filePath):

    tokens = re.sub(r"^\s+", "", contents).split()
    print(tokens)

    return list(zip(tokens, itertools.repeat(filePath)))

if __name__ == '__main__':
    # Standalone Test
    filePath = rootDir + "1.txt"
    contents = getFileContents(filePath)
    tokens = generateTokens(contents, filePath)
    print(contents)
    print(tokens)

# Tokenization
# Input: text (file contents), string (document id = path to file)
# Output: list of pairs < string (token) , string (document id) >
import itertools

from CONST import *
from File_Reading import GetFileContents
import re


def GenerateTokens(contents, filePath):
    tokens = contents.split()
    return list(zip(tokens, itertools.repeat(filePath)))


if __name__ == '__main__':
    # Standalone Test
    filePath = rootDir + "1.txt"
    contents = GetFileContents(filePath)
    tokens = GenerateTokens(contents, filePath)
    print(contents)
    print("tokens")
    print(tokens)

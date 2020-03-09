# Sorting the Tokens
# Perform sorting of the token list: first by tokens (alphabetical order), and then by document ids
# Input to this component will be a concatenated list of tokens from all documents.
# Input: list of pairs < token , document id >
# Output: sorted list of pairs < token , document id >

from CONST import *
from Directory_Listing import listFiles
from File_Reading import getFileContents
from Tokenization import generateTokens
from Linguistic_Modules import PortStem, SnowStem

def sortTokens(token_pairs_list):
    sortedTokens = sorted(token_pairs_list, key=lambda element: (element[0], element[1]))

    return sortedTokens

if __name__ == "__main__":
    # Standalone Test
    fileList = listFiles(rootDir)
    fileContent_1 = getFileContents(fileList[0])
    tokenPair_1 = generateTokens(fileContent_1, fileList[0])
    fileContent_2 = getFileContents(fileList[1])
    tokenPair_2 = generateTokens(fileContent_2, fileList[1])

    tokenPair = tokenPair_1 + tokenPair_2
    original_list = SnowStem(tokenPair)
    print(original_list)
    sorted_list = sortTokens(original_list)
    print(sorted_list)
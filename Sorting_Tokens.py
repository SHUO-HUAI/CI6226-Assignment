# Sorting the Tokens
# Perform sorting of the token list: first by tokens (alphabetical order), and then by document ids
# Input to this component will be a concatenated list of tokens from all documents.
# Input: list of pairs < token , document id >
# Output: sorted list of pairs < token , document id >

from CONST import *
from Directory_Listing import ListFiles
from File_Reading import GetFileContents
from Tokenization import GenerateTokens
from Linguistic_Modules import LingModule


def SortTokens(token_pairs_list):
    sortedTokens = sorted(token_pairs_list, key=lambda element: (element[0], element[1]))

    return sortedTokens


if __name__ == "__main__":
    # Standalone Test
    fileList = ListFiles(rootDir)
    fileContent_1 = GetFileContents(fileList[0])
    tokenPair_1 = GenerateTokens(fileContent_1, fileList[0])
    fileContent_2 = GetFileContents(fileList[1])
    tokenPair_2 = GenerateTokens(fileContent_2, fileList[1])

    tokenPair = tokenPair_1 + tokenPair_2
    original_list = LingModule(tokenPair)
    print(original_list)
    sorted_list = SortTokens(original_list)
    print(sorted_list)
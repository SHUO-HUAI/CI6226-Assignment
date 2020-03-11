# Transformation into Postings
# Performs transformation into the final index. Identical tokens are collapsed together,
# and their document ids are converted into postings lists.
# Input: sorted list of pairs < token , document id >
# Output: inverted index

from CONST import *
from Directory_Listing import listFiles
from File_Reading import getFileContents
from Tokenization import generateTokens
from Linguistic_Modules import PortStem, SnowStem
from Sorting_Tokens import sortTokens


def transformation_into_postings(sorted_token_pairs):  
    # Used dictionary data structure (Hash table)
    dictionary_ = {}

    for a, b in sorted_token_pairs:
        dictionary_.setdefault(a, []).append(b)

    for key in dictionary_:
        value = dictionary_[key]
        posting = list(sorted(set(value)))
        dictionary_[key] = (len(posting), posting)

    return dictionary_


if __name__ == "__main__":
    # Standalone Test
    fileList = listFiles(rootDir)
    for i in range(2):
        tokenPair = generateTokens(getFileContents(fileList[i]), fileList[i])
    
    original_list = SnowStem(tokenPair)
    sorted_list = sortTokens(original_list)
    print(sorted_list)
    transformed_postings = transformation_into_postings(sorted_list)
    print(transformed_postings)
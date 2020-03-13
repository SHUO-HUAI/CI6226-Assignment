# Transformation into Postings
# Performs transformation into the final index. Identical tokens are collapsed together,
# and their document ids are converted into postings lists.
# Input: sorted list of pairs < token , document id >
# Output: inverted index

from CONST import *
from Directory_Listing import ListFiles
from File_Reading import GetFileContents
from Tokenization import GenerateTokens
from Linguistic_Modules import LingModule
from Sorting_Tokens import SortTokens
from collections import OrderedDict


def TransformationIntoPostings(sorted_token_pairs):
    # Used dictionary data structure (Hash table)
    dictionary_ = OrderedDict()

    previous_key = ''
    for key, value in sorted_token_pairs:

        if previous_key != key:
            previous_key = key
            dictionary_[previous_key] = [value]
        else:
            if value not in dictionary_[previous_key]:
                dictionary_[previous_key].append(value)
    for key in dictionary_:
        value = dictionary_[key]
        dictionary_[key] = (len(value), value)

    return dictionary_


if __name__ == "__main__":
    # Standalone Test
    fileList = ListFiles(rootDir)
    tokenPair = []
    for i in range(2):
        tokenPair = tokenPair + GenerateTokens(GetFileContents(fileList[i]), fileList[i])

    original_list = LingModule(tokenPair)
    sorted_list = SortTokens(original_list)
    # print(sorted_list)
    transformed_postings = TransformationIntoPostings(sorted_list)
    print(transformed_postings)

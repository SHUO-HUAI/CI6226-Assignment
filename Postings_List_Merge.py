# Postings List Merge Component
# Implement postings lists merging algorithm
# Input: list of postings lists
# Output: merged postings list

from CONST import *
from Directory_Listing import ListFiles
from File_Reading import GetFileContents
from Tokenization import GenerateTokens
from Linguistic_Modules import LingModule
from Sorting_Tokens import SortTokens
from Transformation_Postings import TransformationIntoPostings


def postings_list_merge(postings_lists):
    # Intersect the postings lists in increasing order of length

    first_len, first_list = postings_lists.pop()
    merged_list = []

    while postings_lists:
        second_len, second_list = postings_lists.pop()

        p1 = 0
        p2 = 0
        length = 0
        while p1 < first_len and p2 < second_len:
            if first_list[p1] == second_list[p2]:
                merged_list.append(first_list[p1])
                p1 += 1
                p2 += 1
                length += 1
            elif first_list[p1] < second_list[p2]:
                p1 += 1
            else:
                p2 += 1
        first_list = merged_list
        first_len = length

    return list(set(merged_list))


if __name__ == "__main__":
    # Standalone Test
    token_list = []
    fileList = ListFiles(rootDir)
    for i in range(2):
        tokenPair = GenerateTokens(GetFileContents(fileList[i]), fileList[i])
        modifed_tokenPair = LingModule(tokenPair)
        token_list = token_list + modifed_tokenPair

    sorted_list = SortTokens(token_list)
    transformed_postings = TransformationIntoPostings(sorted_list)
    merged_list = postings_list_merge([transformed_postings['zone'], transformed_postings['us'], transformed_postings['tie'], transformed_postings['state']])
    print(merged_list)

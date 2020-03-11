# Postings List Merge Component
# Implement postings lists merging algorithm
# Input: list of postings lists
# Output: merged postings list

from CONST import *
from Directory_Listing import listFiles
from File_Reading import getFileContents
from Tokenization import generateTokens
from Linguistic_Modules import PortStem, SnowStem
from Sorting_Tokens import sortTokens
from Transformation_Postings import transformation_into_postings

def postings_list_merge(postings_lists):   
    # Intersect the postings lists in increasing order of length   
    sorted_postings_lists = sorted(postings_lists, key=lambda l : l[0], reverse= True)
    first_len, first_list = sorted_postings_lists.pop()
    merged_list = []
    
    while sorted_postings_lists:
        second_len, second_list = sorted_postings_lists.pop()

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

    return merged_list


if __name__ == "__main__":
    # Standalone Test
    token_list = []
    fileList = listFiles(rootDir)
    for i in range(5):
        tokenPair = generateTokens(getFileContents(fileList[i]), fileList[i])
        modifed_tokenPair = SnowStem(tokenPair)
        token_list += modifed_tokenPair
        
    sorted_list = sortTokens(token_list)
    transformed_postings = transformation_into_postings(sorted_list)
    merged_list = postings_list_merge([transformed_postings['movement'], transformed_postings['need']])
    print(merged_list)

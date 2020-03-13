# A program that  indexes the supplied corpus of documents and then iteratively asks for
# search queries and provides results (as a list of file paths). If the search query contains
# more than one word, consider this to be a Boolean AND query.

from CONST import *
from Directory_Listing import ListFiles
from File_Reading import GetFileContents
from Tokenization import GenerateTokens
from Linguistic_Modules import LingModule, LingStr
from Sorting_Tokens import SortTokens
from Transformation_Postings import TransformationIntoPostings
from Postings_List_Merge import PostingListMerge
import time
import sys

if __name__ == "__main__":

    start = time.time()

    # Directory Listing
    all_files = ListFiles(rootDir)
    all_token_pairs = []

    for file in all_files:
        # File Reading
        file_text = GetFileContents(file)
        # Tokenization
        token_pairs = GenerateTokens(file_text, file)
        # Linguistic Modules
        modified_token_pairs = LingModule(token_pairs)
        all_token_pairs += modified_token_pairs

    del file_text
    del token_pairs
    del modified_token_pairs
    # Sorting the Tokens
    sorted_tokens = SortTokens(all_token_pairs)
    del all_token_pairs
    # Transformation into Postings
    posting_list = TransformationIntoPostings(sorted_tokens)
    del sorted_tokens

    time_index = (time.time() - start)*1000
    print("Time for creating index:\t", time_index, "ms")

    while True:
        query = input()
        q_start = time.time()
        queries = query.split()
        queries = [LingStr(item) for item in queries]
        try:
            if len(queries) < 2:
                length, fileList = posting_list[LingStr(query)]
                print(fileList)
            else:
                print(PostingListMerge([posting_list[item] for item in queries]))
        except BaseException:
            print([])
        q_time = (time.time() - q_start)*1000
        print("Time for this query:\t", q_time, "ms")

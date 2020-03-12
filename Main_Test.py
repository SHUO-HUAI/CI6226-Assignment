# Test for all components 0-5

from CONST import *
from Directory_Listing import ListFiles
from File_Reading import GetFileContents
from Tokenization import GenerateTokens
from Linguistic_Modules import LingModule
from Sorting_Tokens import SortTokens
from Transformation_Postings import TransformationIntoPostings
from Postings_List_Merge import PostingListMerge

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

# Sorting the Tokens
sorted_tokens = SortTokens(all_token_pairs)
#print(sorted_tokens)

# Transformation into Postings
posting_list = TransformationIntoPostings(sorted_tokens)
#print(posting_list)

# Postings List Merge Component
merged_positions = PostingListMerge([posting_list['mail'], posting_list['phone'], posting_list['clinton']])
print(merged_positions)

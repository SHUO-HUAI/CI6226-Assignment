# Test for all components 0-5

from CONST import *
from Directory_Listing import listFiles
from File_Reading import getFileContents
from Tokenization import generateTokens
from Linguistic_Modules import PortStem, SnowStem
from Sorting_Tokens import sortTokens
from Transformation_Postings import transformation_into_postings
from Postings_List_Merge import postings_list_merge

# Directory Listing
all_files = listFiles(rootDir)
all_token_pairs = []

for file in all_files:
    # File Reading
    file_text = getFileContents(file)
    # Tokenization
    token_pairs = generateTokens(file_text, file)
    # Linguistic Modules
    modified_token_pairs = SnowStem(PortStem(token_pairs))
    all_token_pairs += modified_token_pairs

# Sorting the Tokens
sorted_tokens = sortTokens(all_token_pairs)
print(sorted_tokens)

# Transformation into Postings
posting_list = transformation_into_postings(sorted_tokens)
#print(posting_list)

# Postings List Merge Component
merged_positions = postings_list_merge([posting_list['mail'], posting_list['phone'], posting_list['clinton']])
print(merged_positions)

# Optimization using Dictionary tree

from Directory_Listing import ListFiles
from File_Reading import GetFileContents
from Linguistic_Modules import LingStr
from Postings_List_Merge import PostingListMerge
import time
from CONST import *
from bisect import insort


class Dic_Tree:
    def __init__(self):
        self.nodes = dict()
        self.docIds = []

    def insert(self, word: str, docId: str):
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = Dic_Tree()
            curr = curr.nodes[char]
        if docId not in curr.docIds:
            insort(curr.docIds,docId)

    def insert_many(self, words: [str], docId: str):
        for word in words:
            self.insert(word, docId)

    def search(self, word: str):
        curr = self
        for char in word:
            if char not in curr.nodes:
                return []
            curr = curr.nodes[char]
        return curr.docIds


if __name__ == "__main__":
    start = time.time()

    # Directory Listing
    all_files = ListFiles(rootDir)
    dic_tree = Dic_Tree()

    for file in all_files:
        # File Reading
        file_text = GetFileContents(file)
        tokens = file_text.split()
        dic_tree.insert_many([LingStr(item) for item in tokens], file)

    del tokens
    del file_text
    time_index = (time.time() - start) * 1000
    print("Time for creating index:\t", time_index, "ms")

    while True:
        query = input()
        q_start = time.time()
        queries = query.split()
        queries = [LingStr(item) for item in queries]
        try:
            if len(queries) < 2:
                file_list = dic_tree.search(queries[0])
                print(file_list)
            else:
                file_list_for_merge = []
                for q_item in queries:
                    doc_list = dic_tree.search(q_item)

                    file_list_for_merge.append((len(doc_list), doc_list))

                print(PostingListMerge(file_list_for_merge))
        except BaseException:
            print("error")
            print([])
        q_time = (time.time() - q_start) * 1000
        print("Time for this query:\t", q_time, "ms")

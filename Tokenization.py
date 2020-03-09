# Tokenization
# Input: text (file contents), string (document id = path to file)
# Output: list of pairs < string (token) , string (document id) >

from CONST import *
import re
import itertools
from File_Reading import getFileContents

def generateTokens(contents, filePath):

	tokens = re.sub(r"[^a-zA-Z0-9\s]|[\x00-\x08\x0b-\x1f\x7f-\xff]+",'',contents)
	tokens = re.sub(r"\b\w{,1}\b",'', tokens).lower().split()

	return list(zip(tokens, itertools.repeat(filePath)))

if __name__ == '__main__':
	# Standalone test
	filePath = rootDir + "10.txt"
	contents = getFileContents(filePath)
	tokens = generateTokens(contents, filePath)
	print(contents)
	print(tokens)

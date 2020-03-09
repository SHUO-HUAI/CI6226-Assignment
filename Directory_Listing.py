# Directory Listing
# Input: string (path to directory)
# Output: list of strings (full paths to files in the directory)

from CONST import *
from os import listdir
from os.path import isfile, join

def listFiles(dir):
	onlyfiles = [join(dir, f) for f in listdir(dir) if isfile(join(dir, f))]

	return onlyfiles

if __name__ == '__main__':
	# Standalone Test
	listedFiles = listFiles(rootDir)
	print(listedFiles)
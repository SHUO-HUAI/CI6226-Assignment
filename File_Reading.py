# File Reading
# Input: string (full path to file)
#Output: string/text (full contents of a file)

from CONST import *


def GetFileContents(filePath):

	f = open(filePath, encoding='utf-8')
	lines = f.readlines()
	contents = ''.join(lines)

	return contents	


if __name__ == '__main__':
	# Standalone Test
	filePath = rootDir + '1.txt'
	contents = GetFileContents(filePath)
	print(contents)
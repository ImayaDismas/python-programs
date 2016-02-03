#!/usr/bin/python3

# read the lines from the file
# fh = open('lines.txt')
# for index, line in enumerate(fh.readlines()):
# 	print(index, line)
def main():
	s = 'this is a string'
	for i, c in enumerate(s):
		# print(i, c)
		if c == 's':print('index {} is an s'.format(i))



if __name__ == "__main__": main()
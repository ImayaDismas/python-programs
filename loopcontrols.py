#!/usr/bin/python3

# read the lines from the file
# fh = open('lines.txt')
# for index, line in enumerate(fh.readlines()):
# 	print(index, line)
def main():

	s = 'this is a string'
	for c in s:
		print(c)#each character at a time

	s = 'this is a string'
	for c in s:
		if c == 's': continue #shortcuts the loop. Goes back to the loop and gets another iteration
		print(c)#each character at a time

	s = 'this is a string'
	for c in s:
		if c == 's': break#jumps out of the loop entirely
		print(c)#each character at a time

	s = 'this is a string'
	for c in s:
		print(c)#each character at a time
	else:
		print('else')


	s = 'this is a string'
	i = 0
	while(i < len(s)):
		print(s[i])#each character at a time
		i += 1
	else:
		print('else')


if __name__ == "__main__": main()
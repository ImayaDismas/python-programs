#!/usr/bin/python3

# read the lines from the file
# fh = open('lines.txt')
# for index, line in enumerate(fh.readlines()):
# 	print(index, line)
def main():
	L = [1, 2, 3, 4, 5, 6, 7, 8]
	print("Reversed  Array")
	print([8-i for i, num in enumerate(L)])

	for i, num in enumerate(L):
		print([8-i, num])

	s = 'this is a string'
	for i, c in enumerate(s):
		print(15-i, c)#reverses the index 
		# if c == 's':print('index {} is an s'.format(i))



if __name__ == "__main__": main()
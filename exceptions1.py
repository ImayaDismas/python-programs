#!/usr/bin/python3

#Exceptions is the key method of handling errors in Python

def main():
 	try:
		fh = open('lines.txt')
		for line in fh.readlines():
			print(line.strip())


	except IOError as e:
		print('could not open the file:', e)

if __name__ == '__main__':
 	main()
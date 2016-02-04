#!/usr/bin/python3

#regular expressions are powerful methods of matching patterns in text
import re

def main():
	fh = open('lines.txt')
	pattern = re.compile('1line')
	for line in fh:
		if re.search(pattern, line):
			# print(line)
			print(pattern.sub('####', line))

if __name__ == "__main__": main()
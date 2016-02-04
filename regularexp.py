#!/usr/bin/python3

#regular expressions are powerful methods of matching patterns in text
import re

def main():
	fh = open('lines.txt')
	for line in fh:
		match = re.search('1line', line)
		if match:
			print(line.replace(match.group(), '####'))

if __name__ == "__main__": main()
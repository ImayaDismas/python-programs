#!/usr/bin/python3

def main():
	f = open('lines.txt', 'r')
	for line in f.readlines():
		print(line)
if __name__ == "__main__":main() 
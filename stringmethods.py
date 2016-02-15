#!/usr/bin/python3

def main():
	s = 'This is a string of words'
	print(s.split())

	print(s.split('i'))

	words = s.split()
	print(words)

	for w in words: print(w)

	new = ':'.join(words)
	print(new)
	new1 = ','.join(words)
	print(new1)
if __name__ == "__main__":main() 
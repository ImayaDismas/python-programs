#!/usr/bin/python3

def main():
	a, b = 0, 1
	v = 'this is true' if a < b else 'this is not true'
	print(v)
	if a < b: 
		v = 'this is true'
	else:
		v = 'this is not true'

	print(v)

if __name__ == "__main__": main()

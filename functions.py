#!/usr/bin/python3
def main():
	testfunc(45)

def testfunc(number, another = None, anomore = 75):
	if another is None:
		another = 112
	print('this is a test function', number, another, anomore)



if __name__ == "__main__": main()
#!/usr/bin/python3
def main():
	testfunc(5, 6, 7, 8, 9, 10, one = 1,two = 2,four = 42)

def testfunc(this, that, other, *args, **kwargs):
	# 
	print(this, that, other, args, kwargs['one'], kwargs['two'], kwargs['four'])
	for k in kwargs:print (k, kwargs[k])
	for n in args:print (n) #to print the tuple


if __name__ == "__main__": main()

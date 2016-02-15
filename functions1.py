#!/usr/bin/python3
def main():
	testfunc(1,2,3,42,43,45,46)

def testfunc(this , that, other, *args):
	print(this , that, other, args)
	for n in args:print (n) 


if __name__ == "__main__": main()



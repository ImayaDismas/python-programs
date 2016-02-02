#!/usr/bin/python3
#/usr/bin/python3 path to the python3 interpreter
def main():
	a, b = 1, 1
	if a < b:
		print("a is less than b")
	elif a > b:
		print("a is graeter than b")
	else:
		print("a is equal to b")

	s = "less than" if a < b else "not less than"
	print(s)

if __name__ == "__main__": main()

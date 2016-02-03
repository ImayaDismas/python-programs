#!/usr/bin/python3
# types of numbers
# integers and floating point numbers
def main():
	x = 42
	print(x)
	num = round(x/9)
	print(type(num), num)

	mod = x % 9
	print(mod)

	y = int(42.9)
	print(y)

	f = float(42)
	print(f)

if __name__ == "__main__": main()

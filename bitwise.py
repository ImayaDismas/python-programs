#!/usr/bin/python3

def main():
	num = 5
	print(num)

	bit = 0b0101#binary number 5
	print(bit)

	b(5)#calling the function
	x, y = 0x55, 0xaa
	b(x)#calls the function to print the binary values of the values of y and x
	b(y)


def b(n):
	print('{:08b}'.format(n))#prints the binary to 8 places



if __name__ == "__main__":main()

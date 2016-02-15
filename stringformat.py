#!/usr/bin/python3

def main():
	a, b = 5, 42
	print(a, b)
	print('this is {} , that is {}'.format(a, b))

	s = 'this is {} , that is {}'
	print(s.format(a, b))
	print(id(s.format(a, b)))

	s1 = 'this is {1} , that is {0}'
	print(s1.format(a, b))

	s2 = 'this is {} , that is {}'
	print(s2.format(b, a))
if __name__ == "__main__":main() 

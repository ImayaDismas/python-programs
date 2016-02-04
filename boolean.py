#!/usr/bin/python3

def main():
	boo = (5 ==  5)
	print(boo)
	print(type(boo))


	print('logical operator AND')
	#logical operator AND
	a = (True and True)
	print(a)

	b = (True and False)
	print(b)

	c = (False and True)
	print(c)

	d = (False and False)
	print(d)

	print('logical operator OR')
	#logical operator OR
	a = (True or True)
	print(a)

	b = (True or False)
	print(b)

	c = (False or True)
	print(c)

	d = (False or False)
	print(d)


	print('different part')
	a, b = 0, 1
	x, y = 'zero', 'one'

	t = x < y
	print(t)
	if a < b and x > y: 
		print('yes')
	else:
		print('no')

if __name__ == '__main__':main()

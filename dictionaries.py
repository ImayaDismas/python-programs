#!/usr/bin/python3

def main():
	d = {'one' : 1, 'two' : 2, 'three' : 3}
	print(d)
	print(type(d))
	x = dict(four = 4, five = 5, six = 6)
	print(x)

	y = dict(one = 1, two = 2, three = 3, **x)
	print(y)
	print('three' in x)
	print('three' in y)

	print(x.get('three'))
	print(y.get('three'))

	print(x.get('three', 'not found'))

	del x['four']
	print(x)
	print(x.pop('five'))
if __name__ == "__main__":main() 
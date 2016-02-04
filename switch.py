#!/usr/bin/python3
#/usr/bin/python3 path to the python3 interpreter
def main():
	choices = dict(
		one = 'first',
		two = 'second',
		three= 'third',
		four = 'fourth',
		five = 'fifth'
	)
	v = 'five'
	print(choices.get(v, 'other'))


if __name__ == "__main__": main()

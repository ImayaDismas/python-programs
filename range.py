#!/usr/bin/python3
def main():
	for n in inclusive_range(5, 250, 3): 
		print(n)


# def inclusive_range(start, stop, step):
# 	i = start
# 	while i <= stop:
# 		yield i
# 		i +=step

def inclusive_range(*args):
	numargs = len(args)
	if numargs < 1 : raise TypeError('requires at least one argument')
	elif numargs == 1:
		stop = args[0]
		start = 0
		step = 1
	elif numargs == 2:
		(start, stop) = args
		step = 1
	elif numargs == 3:
		(start, stop, step) = args
	else: raise TypeError('inclusive range expected at most 3 arguments, got ()'.format(numargs))
	i = start
	while i <= stop:
		yield i
		i +=step



if __name__ == "__main__": main()
#!/usr/bin/python3

def main():
	d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
	for k in sorted(d.keys()): #sorted sorts the alphabetically
		print(k, d[k])
	#using a different definition of the dictionaries
	a = dict(
			one=1, two = 2, three = 3, four = 4, five = 'five'
		)#usually are mutable
	a['seven'] = 7#one can add this
	for k in sorted(a.keys()): #sorted sorts the alphabetically
		print(k, a[k])

if __name__ == "__main__": main()
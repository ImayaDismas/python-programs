#!/usr/bin/python3

def main():
	t = tuple(range(25))
	print(t)

	print(10 in t)
	print(50 in t)
	print(540 not in t)

	for i in t: print(i)


	x = list(range(25))
	print(x)

	print(10 in x)
	print(50 in x)
	print(540 not in x)

	for o in x: print(o)
	print(t.count(5))
	print(t.index(5))

	print(x.append(100))
	print(x)
	print(len(x))

	print(x.extend(range(20)))
	print(x)

	x.insert(0, 25)
	print(x)

	x.insert(12, 100)
	print(x)

	x.remove(12)
	print(x)


	del x[12]
	print(x)

	print(x.pop())
	print(x.pop(0))
	print(x)
if __name__ == "__main__":main() 
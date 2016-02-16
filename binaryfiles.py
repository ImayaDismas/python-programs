#!/usr/bin/python3

def main():
	buffersize = 50000# one has to use a brinary datatype and buffered io
	infile = open('imaya.jpg', 'rb')
	outfile = open('new.jpg', 'wb')
	buffer = infile.read(buffersize)
	while len(buffer):
		outfile.write(buffer)
		print('.')
		buffer = infile.read(buffersize)
	print()
	print('Done')
if __name__ == "__main__":main() 
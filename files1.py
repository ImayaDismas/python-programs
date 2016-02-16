#!/usr/bin/python3

def main():
	buffersize = 50000 #if the file is big enough
	infile = open('lines.txt', 'r')
	outfile = open('new.txt', 'w')
	buffer = infile.read(buffersize)
	# for line in infile:
	# 	print(line, file == outfile)

	while len(buffer):
		outfile.write(buffer)
		print('.')
		buffer = infile.read(buffersize)
	print('')
	print('Done')
if __name__ == "__main__":main() 
#!/usr/bin/python3

class Duck:
	def quack(self):
		print('Quaaack!')

	def walki(self):
		print('Walks like a duck')
def main():
	donald = Duck()
	print(donald)
	donald.quack()
	donald.walki()
	

if __name__ == "__main__": main()
#!/usr/bin/python3

class Duck:
	
	def quack(self):
		print('Quaaack!')


	def fur(self):
		print('the duck has no fur')


	def walk(self):
		# super( ).walk() to overide the methods
		print('Walks like a duck')

	def bark(self):
		print('the duck cnanot bark')

class Dog:
	def bark(self):
		print('Woof!')

	def fur(self):
		print('the dog has brown and white fur')

	def quack(self):
		print('The dog cannot quack')  

	def walk(self):
		# super( ).walk() to overide the methods
		print('Walks like a duck')
		
def main():
	donald = Duck()
	fido = Dog()
	for o in (donald, fido):
		o.quack()
		o.walk()
		o.bark()
		o.fur()
	

if __name__ == "__main__": main()
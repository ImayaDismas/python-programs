#!/usr/bin/python3
class Animal:
	def talk(self):print('I have something to say!')
	def walk(self):print('hey! I''m walkin!'' here')
	def clothes(self):print('I have nice clothes!')

class Duck(Animal):
	
	def quack(self):
		print('Quaaack!')

	def walk(self):
		# super( ).walk() to overide the methods
		print('Walks like a duck')

class Dog(Animal):
	def clothes(self):
		print('I have brown and white fur')
def main():
	donald = Duck()
	donald.quack()
	donald.walk()
	donald.clothes() 

	fido = Dog()
	fido.walk()
	fido.clothes()

if __name__ == "__main__": main()
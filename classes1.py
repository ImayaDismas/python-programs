#!/usr/bin/python3

class Duck:
	def __init__(self, value):
		# self._v is attached to the object and not class.
		# the value is part of the object(encapsulation)
		self._v  = value
	def quack(self):
		print('Quaaack!', self._v)

	def walki(self):
		print('Walks like a duck', self._v)
def main():
	donald = Duck(52)
	frank = Duck(151)
	donald.quack()
	donald.walki()
	frank.quack()
	frank.walki()
	

if __name__ == "__main__": main()
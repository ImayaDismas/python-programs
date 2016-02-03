#!/usr/bin/python3

class Egg:
	#constuctor
	def __init__(self, kind = "fried"):
		self.kind = kind#each object can have a different item as kind


	def whatkind(self):
		return self.kind

def main():
	# Object is an instance of the class
	# An encapsulation of all the methods and the variables inside a class
	fried = Egg()
	scrambled = Egg("scrambled")
	print(fried.whatkind())#uses the default value
	print(scrambled.whatkind())

if __name__ == "__main__": main()
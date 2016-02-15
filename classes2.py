#!/usr/bin/python3

class Duck:
	def __init__(self, **kwargs):
		# self._v is attached to the object and not class.
		# the value is part of the object(encapsulation)
		#control of how the data is being used
		#underscore used locally
		# self._color  = kwargs.get('color', 'white')
		self.variables  = kwargs
	def quack(self):
		print('Quaaack!')

	def walki(self):
		print('Walks like a duck')

	# def set_color(self, color):
	# 	# self._color = color
	# 	self.variables['color']= color

	# def get_color(self):
	# 	# return self._color
	# 	return self.variables.get('color', None)
	def set_varible(self, k, v):
		self.variables[k] = v

	def get_variable(self, k):
		return self.variables.get(k, None)


def main():
	donald = Duck(color = 'blue')
	print(donald.get_variable('color'))

	donald = Duck(money = '100')
	print(donald.get_variable('money'))

	donald = Duck(feet = 2)
	print(donald.get_variable('feet'))
	
if __name__ == "__main__": main()
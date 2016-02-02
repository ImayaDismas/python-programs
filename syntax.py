#!/usr/bin/python3
#/usr/bin/python3 path to the python3 interpreter
def main():
	print("This is the syntax.py file.")
	egg()

def egg():
	print("egg")

if __name__ == "__main__": main()

#allow us to run the scripts with the function in the order that we want.
#  allows us to define function after they are called 
# if __name__ == "__main__": allow only to be run when this model is called as the main modal
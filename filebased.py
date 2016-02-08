#!/usr/bin/python3
def storage():
    file = open("filebased.txt", "w")
    words = input("Enter the words to store:\n")
    file.write(words)
    file.close()



def  main():
  option = ''
  while option != 'end':
    option = input("Enter your choice:\n 'store' to Store in the database \n 'find' to Search in the database\n 'end' to quit\n")
    if option == "store":
      storage()

    elif option == "find":
      searching()

    elif option == 'end':
        print("\nGoodbye. See you later.\n")

    else:
        print("\nI don't understand that choice, please try again.\n")

if __name__ == "__main__":main()
  


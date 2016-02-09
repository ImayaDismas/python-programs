#!/usr/bin/python3
# Pattern: (d\w+)\W(d\w+)
import re
def searching():
  file = open("filebased.txt", "r")
  words = input("Enter the words to search:\n")
  # for line in file:
  #   # match = re.search(words, line)
  #   m = re.match(words + "\w+", line)
  #   # m = re.match(words + "\w+\W\w+", line)
  #   if m:
  #     print(m.group())
  print("<html>")
  print("<body>")
  print("<table>")
  print("<tr><th>Search Results</th></tr>")
  print("<tr>")
  for line in file:
    # match = re.search(words, line)
    m = re.match(words + "\w+", line)
    # m = re.match(words + "\w+\W\w+", line)
    if m:
      print("<td>")
      print(m.group())
      print("</td>")
  print("</tr>")
  print("</table>")
  print("</body>")
  print("</html>")
  file.close()

def storage():
    file = open("filebased.txt", "a")
    words = input("Enter the words to store:\n")
    file.write(words)
    file.write("\n")
    file.close()



def  main():
  option = ''
  while option != 'end':
    option = input("Enter your choice:\n 'store' to Store in the database \n 'find' to Search in the database\n 'end' to quit\n")
    if option == "store" or option == "Store":
      storage()

    elif option == "find" or option == "Find":
      searching()

    elif option == 'end' or option == 'End':
        print("\nGoodbye. See you later.\n")

    else:
        print("\nI don't understand that choice, please try again.\n")

if __name__ == "__main__":main()
  


def spellchecker(sentence):
  words = open('checker.words').readlines()
  words = list(map(lambda x: x.strip(),words))
  items = sentence.split()
  misspelt = []
  for item in items:
    if(item not in words):
      misspelt.append(item)
  return misspelt

def  main():
  lst = []
  sentence = input("Enter the sentence:\n")
  lst = spellchecker(sentence)
  print(lst)

if __name__ == "__main__":main()
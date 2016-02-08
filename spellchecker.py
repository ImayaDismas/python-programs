def spellchecker(sentence):
  words = open('checker.words').readlines()
  words = list(map(lambda x: x.strip(),words))
  res = sentence.split()
  ret = []
  for item in res:
    if(item not in words):
      ret.append(item)
  return ret

def  main():
  sentence = input("Please enter a sentence\n")
  lst = []

  lst = spellchecker(sentence)
  print(lst)

if __name__ == "__main__":main()
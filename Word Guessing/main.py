import math
import random
class GuessingGame:

    def GuessWord(self):
         words=["science","python","leetcode","football","django","golang","matlib","pandas","numpy"]
         word=random.choice(words)
         
         hashMap={}
         for i,w in enumerate(word):
             if w in hashMap.keys():
                 hashMap[w].append(i)
             else:
                 hashMap[w]=[i]     
         list_of_chars=["_" for x in word]
         attempts=12
         i=0
         print("the word is anything related to python \n")
    
         while i<attempts:
             ch_guess=input("Guess one character from the word?")
             if ch_guess in word:
                 if not len(hashMap[ch_guess])>0:
                      print("already found!")
                      continue
                 ind=hashMap[ch_guess][0]
                 hashMap[ch_guess].remove(ind)
                 list_of_chars[ind]=ch_guess
                 print("char found ,👏")
                 print(" ".join(list_of_chars))
                 if "".join(list_of_chars)==word:
                     print("\n")
                     print("Hooray, you found the word!!!!")
                     break

             else:
                 print("char not present ,keep trying!")
             i+=1 

                     




if __name__=="__main__":
    g=GuessingGame()
    g.GuessWord()

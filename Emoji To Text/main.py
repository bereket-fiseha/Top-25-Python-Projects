import demoji


def decodeAllEmojis():
   inp=input("enter your emojis, by pressing ((🪟 and .) in windowns) \n") 
   res= demoji.findall(inp)
   print(res)

if __name__=="__main__":
   decodeAllEmojis()
import math
import random
class GuessingGame:

    def GuessNumber(self):
        lower_bound=input("Enter Lower Bound, \n")
    
        upper_bound=input("Enter Upper Bound, \n")
        lower_int=int(lower_bound)
        upper_int=int(upper_bound)
        chances= math.floor(math.log((upper_int-lower_int+1),2))
        sys_pick=random.randint(lower_int,upper_int)
        while chances>0:
            user_pick=input("guess the number!, \n")
            user_pick_int=int(user_pick)
            if user_pick_int== sys_pick:
                 print("Yaay , U Got It! 👏👏👏👏👏")  
                 break
            elif user_pick_int > sys_pick:
                 print("z🙋‍♂️, Its too High!")
                
            else:
                print("🙅‍♂️, Its too Low!")    
            chances-=1
        print("😔😔💔💔, sorry you have run out of chances!")   
        try_again=input("you want to try again,y/n \n")
        if try_again== "y":
            self.GuessNumber()











if __name__=="__main__":
    g=GuessingGame()
    g.GuessNumber()

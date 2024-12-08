import random
from enum import Enum,auto
class GameChoice(Enum):
    Rock=auto()
    Paper=auto()
    Scissor=auto()


class RockPaperScissor:

     def Play(self):
      while True:  
        choiceList=[GameChoice.Rock,GameChoice.Paper,GameChoice.Scissor]

        comIntChoice=random.randint(1,3)

        userIntChoice=input("choose \n      1.Rock\n      2.Paper\n      3.Scissor\n")
        print("Your choice",GameChoice(int(userIntChoice)).name)
        print("Computer choice is .....") 
        print("Computer  chooses",GameChoice(comIntChoice).name)
        
        comChoice=GameChoice(comIntChoice)
        userChoice=GameChoice(int(userIntChoice))
        if (comChoice,userChoice)==(GameChoice.Rock,GameChoice.Paper)or(comChoice,userChoice)==(GameChoice.Paper,GameChoice.Rock):
            
            if userChoice==GameChoice.Paper:
                 print("You have won!")
               
            else:
               print("Sorry ,you lost!")
            print("Paper covers Rock!")  
        elif (comChoice,userChoice)==(GameChoice.Scissor,GameChoice.Paper)or(comChoice,userChoice)==(GameChoice.Paper,GameChoice.Scissor):
            
            if userChoice==GameChoice.Scissor:
                 print("You have won!")
               
            else:
               print("Sorry ,you lost!")
            print("Scissor cuts Paper!")   
        elif (comChoice,userChoice)==(GameChoice.Scissor,GameChoice.Rock)or(comChoice,userChoice)==(GameChoice.Rock,GameChoice.Scissor):
            
            if userChoice==GameChoice.Rock:
                 print("You have won!")
               
            else:
               print("Sorry ,you lost!")
            print("Rock beats Scissor!")   
        else:
            print("its a tie!")
        playAgain=input("do you want to play again? y/n... ")
        if playAgain.lower()!="y":   
              break


if __name__=="__main__":
    rps=RockPaperScissor()
    rps.Play()
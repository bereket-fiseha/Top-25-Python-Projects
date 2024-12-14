import time

def count_down():
    inp=input("Enter duration in sec:  ")
    totalSecs=int(inp)
   
    while totalSecs!=0:
        mins=totalSecs//60
        secs=totalSecs-(mins*60)
        totalSecs-=1
        timer='{:02d}:{:02d}'.format(mins, secs) 
        print(timer,end="\r")
        time.sleep(1)
if __name__=="__main__":
     count_down()



    


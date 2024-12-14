from plyer import notification


def notify_user():
    title=input("enter title,\n")
    
    desc=input("enter message,\n")

    notification.notify(title=title,message=desc,timeout=10)

if __name__=="__main__":
    notify_user()    
  
import requests
#from win32com.client import Dispatch
from dotenv import load_dotenv
import time
import os
from enum import Enum,auto
class NewsSource(Enum):
    bbc_news=auto()
    associated_press=auto()
    al_jazeera_english=auto()


class NewsApp:
    def __init__(self):
         load_dotenv()
    def FetchTopHeadLines(self):
          pass
    def FetchArticles(self):
         #replace with your own api key
         src_inp=input("choose your source?\n 1.bbc news 2.abc news 3. aljazeera-en ")
         temp= NewsSource(int(src_inp)).name
         src_splite=temp.split("_")
         src="-".join(src_splite)
         print(src)
         api_key=os.getenv("api_key")
         query_params = {
              "source":src,
              "sortBy": "top",
          
              "apiKey": api_key
    }
         main_url = "https://newsapi.org/v1/articles"
         res=requests.get(main_url,params=query_params)
         data=res.json()["articles"]
         i=1
         ls=[]
         #speak = Dispatch("SAPI.Spvoice")
         
         for news in data:
             news_title=f"{i}. title:{news['title']}"
             
             speak_title=f"{i}. :{news['title']}"
             news_desc=f"   description:{news['description']}\n"
             i+=1
             print(news_title)
             print(news_desc)
             # speak.Speak(speak_title)   
             time.sleep(2)
             
   
         

if __name__=="__main__":
    g=NewsApp()
    g.FetchArticles()

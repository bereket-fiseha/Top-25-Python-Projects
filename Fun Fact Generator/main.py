from pywebio.input import *
from pywebio.session import *
from pywebio.output import *
import requests
import json

def clear_page(_):
     clear()
     
     put_html( '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>')
   
     put_buttons(
        [dict(label='Show Fact', value='outline-success', color='outline-success')],
        onclick=fun_fact
    )
     put_buttons(
        [dict(label='Clear Page', value='outline-success', color='outline-success')],
        onclick=clear_page
    )
   
def fun_fact(_):
    put_html("<br/>")
    
    put_html("<br/>")
    
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response=requests.get(url)
    result=response.text
    pyDict=json.loads(response.text)
    print(pyDict["text"])
    style(put_text(pyDict["text"]), 'color:blue; font-size: 30px')



if __name__=="__main__":
   put_html( '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>')
   
   put_buttons(
        [dict(label='Show Fact', value='outline-success', color='outline-success')],
        onclick=fun_fact
    )
   put_buttons(
        [dict(label='Clear Page', value='outline-success', color='outline-success')],
        onclick=clear_page
    )
   
   
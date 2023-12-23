from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep


def wtspmsg(name,message):
    
    # startfile("https://web.whatsapp.com/")
    startfile("C:\\Users\\MD FAISAL KHAN\\Desktop\\WhatsApp.lnk")

    sleep(7)
    
    click(x=221, y=154)
    
    sleep(1)

    write(name)

    sleep(1)
    
    click(x=322, y=246)
    
    sleep(1)
    
    click(x=1001, y=998)
    
    write(message)
    
    sleep(1)
    
    press('enter')
    
    
def VoiceCall(name):
    
    startfile("C:\\Users\\MD FAISAL KHAN\\Desktop\\WhatsApp.lnk")
    
    sleep(7)
    
    click(x=221, y=154)
    
    sleep(1)

    write(name)

    sleep(1)
    
    click(x=322, y=246)
    
    sleep(1)
    
    click(x=1801, y=97)
  
def VideoCall(name):
    
    startfile("C:\\Users\\MD FAISAL KHAN\\Desktop\\WhatsApp.lnk")
    
    sleep(7)
    
    click(x=221, y=154)
    
    sleep(1)

    write(name)

    sleep(1)
    
    click(x=322, y=246)
    
    sleep(1)
      
    click(x=1738, y=84)
    
       
    
def youtubeSearch(search):
    
    startfile("https://www.youtube.com/")
    
    sleep(5)
    
    click(x=774, y=159)
    
    write(search)
    
    press('enter')
    

def mail(name,msg):
    startfile('https://mail.google.com/mail/u/0/#inbox')
    
    sleep(10)
    
    click(x=169, y=269)
    
    sleep(1)
    
    click(x=1290, y=465)

    sleep(1)
    
    write(name)
    
    sleep(1)
    
    press('enter')
    
    sleep(1)
    
    click(x=1353, y=664)
    
    write(msg)
    
    sleep(1)
    
    click(x=1231, y=982)

    
    
def makautlogin(username,password):
    startfile("https://makaut1.ucanapply.com/smartexam/public/")
    sleep(5)
    
    click(x=316, y=318)
    
    sleep(1)
    
    click(x=730, y=294)
    click(x=730, y=294)
    
    write(username)
    
    sleep(1)
    
    click(x=1173, y=373)
    click(x=1173, y=373)
    
    write(password)
    
    click(x=1116, y=462)
    sleep(5)
    
  
    



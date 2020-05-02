from tkinter import *
import base64
from PIL import Image, ImageTk
import random
import math

root=Tk()
root.title('grid')
root.geometry('500x500')
root.resizable(False,False)



class info:

    words="do you want to play a game?"

    turn=0
    center=False
    gamestart=False
    player=0
    computer=0
    board=[0,0,0,0,0,0,0,0,0]
    playermove=0


##first iteration:
def makegrid1(num):
    buttons=0
    newrow=num**0.5
    x=0
    y=0
    while buttons!=num:
        Button_1 = Button(root, bg='#fff',width=2,height=1)
        Button_1.grid(row=x,column=y)
        y+=1
        if y==newrow:
            x+=1
            y=0
        buttons+=1

##making the new buttons defined in a list so they can all be called individually (theoretically):

def makegrid2(num):
    blist=[]
    while len(blist)!=num:
        blist.append(0)
    buttons=0
    newrow=num**0.5
    x=0
    y=0
    while buttons!=num:
        blist[buttons] = Button(root, bg='#fff',width=2,height=1)
        blist[buttons].grid(row=x,column=y)
        y+=1
        if y==newrow:
            x+=1
            y=0
        buttons+=1

##adding a global list that I can hopefully map a seperate command function to so that it changes the number on the list
##accociated with the number of the button to a 1 instead of a 0 therby allowing me to check if a button has been activated and then
##theoretically, perform actions that change that button and the other buttons around it:


def makegrid(num):
    global gridstats
    blist=[]
    while len(blist)!=num:
        blist.append(0)
    gridstats=[]
    while len(gridstats)!=num:
        gridstats.append(0)
    buttons=0
    newrow=num**0.5
    x=0
    y=0
    while buttons!=num:
        blist[buttons] = Button(root, bg='#fff',width=2,height=1)
        blist[buttons].grid(row=x,column=y)
        y+=1
        if y==newrow:
            x+=1
            y=0
        buttons+=1

##I am not even sure if #2 worked.
makegrid(256)










root.mainloop
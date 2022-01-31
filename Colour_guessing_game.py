# Colour guessing game

from tkinter import*
import random
from tkinter import messagebox

colors = ["Red", "Blue", "Green", "Pink", "Black", "Yellow", "Orange", "White", "Purple", "Brown", "Cyan"]

score = 0
timeleft = 60

def startGame(event):
  if timeleft == 60:
    countdown()
  
  nextcolor()

def countdown():
  global timeleft
  if timeleft == 0:
    messagebox.showinfo("Time left","Time is over and your score is",str(score))
  if timeleft > 0:
    timeleft -= 1
    timeLabel.config(text="Time left : "+str(timeleft))
    timeLabel.after(1000,countdown)

def nextcolor():
  global score
  global timeleft

  if timeleft > 0:
    e.focus_set()
    if e.get().lower() == colors[1].lower():   # red = Red 
      score += 1

    e.delete(0,END)
    random.shuffle(colors)

    Label.config(fg = str(colors[1]), text= str(colors[0]))   # red --> black
    scoreLabel.config(text= "Score: " + str(score))


root = Tk()
root.title("My Color Game")
root.geometry("375x200")
root.resizable(0,0)

instructions = Label(text = "Type the color of the words, and NOT the word text!!", font=('Helvetica'))
instructions.pack()

scoreLabel = Label(root,text= "Press enter to start the game",font= ('Helvetica',12))
scoreLabel.pack()

timeLabel = Label(root,text= "Time left: " +str(timeleft), font= ('Helvetica',12))
timeLabel.pack()

Name = Label()(text="Created by: Amoksh Layane", font=('Helvetica'))
Name.pack()

Label = Label(root,font= ('Helvetica',60))
Label.pack()

e = Entry(root)
root.bind('<Return>',startGame)
e.pack()
e.focus_set()

root.mainloop()

# print("Done Jack")

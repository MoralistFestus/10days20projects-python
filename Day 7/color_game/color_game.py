# import the modules  

import tkinter 

import random 

  
# store colors in list

colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown','Indigo'] 

score = 0

# the game time left, initially 30 seconds. 
timeleft = 30

# function that will start the game. 

def startGame(event): 
    if timeleft == 30: 
        # start the countdown timer. 
        countdown() 
        
    # run the function to 

    # choose the next colour. 
    nextColour() 
  
# Function to choose and 
# display the next colour. 

def nextColour(): 
    # use the globally declared 'score' 

    # and 'play' variables above. 
    
    global score 
    global timeleft 
    
    # if a game is currently in play 

    if timeleft > 0: 
        # make the text entry box active.
        e.focus_set() 
        
        # if the colour typed is equal 

        # to the colour of the text 

        if e.get().lower() == colours[1].lower(): 
            score += 1
            
        # clear the text entry box. 

        e.delete(0, tkinter.END) 
        random.shuffle(colours) 

        # change the colour to type, by changing the 

        # text _and_ the colour to a random colour value 

        label.config(fg = str(colours[1]), text = str(colours[0])) 

          
        # update the score. 

        scoreLabel.config(text = "Score: " + str(score)) 
  
# Countdown timer function  

def countdown(): 
    global timeleft 

    # if a game is in play 

    if timeleft > 0: 

        # decrement the timer. 

        timeleft -= 1

        # update the time left label 

        timeLabel.config(text = "Time left: " + str(timeleft)) 

        # run the function again after 1 second. 

        timeLabel.after(1000, countdown) 
  
# create a GUI window 

root = tkinter.Tk() 

# set the title 

root.title("Random Color Game") 

# set the size 

root.geometry("375x300") 

# add an instructions label 

instructions = tkinter.Label(
root, text = "Enter the colors displayed"
" not the word texts!", 
fg = "orange", 
bg = "white", 
font = ('Georgia', 8)) 
instructions.pack()  

# add a score label 

scoreLabel = tkinter.Label(
root, 
text ="Press enter to start", 
font = ('serif', 10)) 
scoreLabel.pack(padx=20, pady=20) 

# add a time left label 

timeLabel = tkinter.Label(
root, 
text = "Time left: " +str(timeleft), 
font = ('Helvetica', 12)) 

timeLabel.pack() 
  
# add a label for displaying the colours 

label = tkinter.Label(
root, 
font = ('Helvetica', 60)) 
label.pack() 

# add a text entry box for 
# typing in colours 

e = tkinter.Entry(root) 

# run the 'startGame' function  
# when the enter key is pressed 

root.bind('<Return>', startGame) 
e.pack(padx=20, pady=20) 

# set focus on the entry box 
e.focus_set() 
 
# start the GUI 
root.mainloop() 
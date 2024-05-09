from colorHandler import *
from tkinter import Label, Frame, IntVar, BooleanVar, Tk

def gameTurn(r:int, c:int, frame:Frame, turnNumber:IntVar, turnLabel:Label, infoLabel:Label, gameRunning:BooleanVar):
    if gameRunning.get():
        #Check if the grid cell isn't occupied
        if frame.grid_slaves(row=r, column=c)[0].cget("text") != " ":
            infoLabel.config(text="This cell is already occupied!")
        else:
            #Change Label text
            frame.grid_slaves(row=r, column=c)[0].config(text="X" if turnNumber.get() % 2 == 0 else "O")
            infoLabel.config(text="")
            #Check if player has won
            if playerWon(frame, "X" if turnNumber.get() % 2 == 0 else "O"):
                infoLabel.config(text="{} HAS WON!".format("X" if turnNumber.get() % 2 == 0 else "O"))
                gameRunning.set(False)
                return
            else:
                #End the game if the grid is full
                if gridIsFull(frame):
                    infoLabel.config(text="No one won!")
                    gameRunning.set(False)
                    return
                else:
                    #Increase turnNumber value
                    turnNumber.set(turnNumber.get() + 1)
                    #Update turnLabel's text
                    turnLabel.config(text="{}'s turn".format("X" if turnNumber.get() % 2 == 0 else "O"))
    else:
        pass
    
def loadGame(frame:Frame, padSize:int, turnNumber:IntVar, turnLabel:Label, infoLabel:Label, gameRunning:BooleanVar,isDarkTheme:BooleanVar):
    
    #List with padding values (padx(left,right),pady(top,bottom))
    paddingSizeList = [[padSize,0,padSize,padSize], 
                       [padSize,padSize,padSize,padSize],
                       [0,padSize,padSize,padSize],
                       [padSize,0,0,0],
                       [padSize,padSize,0,0],
                       [0,padSize,0,0],
                       [padSize,0,padSize,padSize],
                       [padSize,padSize,padSize,padSize],
                       [0,padSize,padSize,padSize]]    
    for r in range(3):
        for c in range(3):
            #"Index" for the label 
            labelIndex = r * 3 + c
            
            #Cell Label
            TTT_Label = Label(frame, 
                              text=" ",
                              background=getLabelBackgroundColor(isDarkTheme),
                              fg=getFontColor(isDarkTheme),
                              font=("Arial", 50),
                              width=4,
                              height=2)
            TTT_Label.grid(row=r, column=c, 
                           padx=(paddingSizeList[labelIndex][0],
                                 paddingSizeList[labelIndex][1]),
                           pady=(paddingSizeList[labelIndex][2],
                                 paddingSizeList[labelIndex][3]))
            #Check if user clicked one of the labels
            TTT_Label.bind("<Button-1>", lambda event, row=r, col=c: gameTurn(row, 
                                                                              col, 
                                                                              frame,
                                                                              turnNumber,
                                                                              turnLabel,
                                                                              infoLabel,
                                                                              gameRunning))
            
def playerWon(frame:Frame, symbol:str):
    #Horizontal check
    for h in range(3):
        if frame.grid_slaves(row=h, column=0)[0].cget("text") == symbol and frame.grid_slaves(row=h, column=1)[0].cget("text") == symbol and frame.grid_slaves(row=h, column=2)[0].cget("text") == symbol:
            return True

    #Horizontal check
    for v in range(3):
        if frame.grid_slaves(row=0, column=v)[0].cget("text") == symbol and frame.grid_slaves(row=1, column=v)[0].cget("text") == symbol and frame.grid_slaves(row=2, column=v)[0].cget("text") == symbol:
            return True

    #Diagonal check left
    if frame.grid_slaves(row=0, column=0)[0].cget("text") == symbol and frame.grid_slaves(row=1, column=1)[0].cget("text") == symbol and frame.grid_slaves(row=2, column=2)[0].cget("text") == symbol:
            return True
    
    #Diagonal check right
    if frame.grid_slaves(row=0, column=2)[0].cget("text") == symbol and frame.grid_slaves(row=1, column=1)[0].cget("text") == symbol and frame.grid_slaves(row=2, column=0)[0].cget("text") == symbol:
            return True
    
    return False

def gridIsFull(frame:Frame):
    for r in range(3):
        for c in range(3):
            if frame.grid_slaves(row=r, column=c)[0].cget("text") == " ":
                return False
    return True

def resetGame(frame:Frame, turnNumber:IntVar, TTT_Turn_Label:Label, TTT_Info_Label:Label, gameRunning:BooleanVar):
    #Reset Grid
    for r in range(3):
        for c in range(3):
            frame.grid_slaves(row=r, column=c)[0].config(text=" ")
            turnNumber.set(0)
    
    #Reset TTT_Turn_Label text
    TTT_Turn_Label.config(text="{}'s turn".format("X" if turnNumber.get() % 2 == 0 else "O"))

    #Reset TTT_Info_Label text
    TTT_Info_Label.config(text="")

    #Reset gameRunning value
    gameRunning.set(True)

def changeTheme(isDarkTheme:BooleanVar, window:Tk, TTT_Turn_Label:Label, TTT_Info_Label:Label, TTT_Grid_Frame:Frame):
    #Change isDarkTheme
    isDarkTheme.set(not isDarkTheme.get())

    #Change padding color
    TTT_Grid_Frame.config(background=getPadColor(isDarkTheme))

    #Change Window background color 
    window.config(background=getBackgroundColor(isDarkTheme))
    
    #Change TTT_Label font color and background color
    for r in range(3):
        for c in range(3):
            TTT_Grid_Frame.grid_slaves(row=r, column=c)[0].config(fg=getFontColor(isDarkTheme),
                                                                  background=getLabelBackgroundColor(isDarkTheme))

    #Change TTT_Turn_Label font color and background color
    TTT_Turn_Label.config(fg=getFontColor(isDarkTheme),
                          background=getBackgroundColor(isDarkTheme))

    #Change TTT_Info_Label font color and background color
    TTT_Info_Label.config(fg=getFontColor(isDarkTheme),
                          background=getBackgroundColor(isDarkTheme))



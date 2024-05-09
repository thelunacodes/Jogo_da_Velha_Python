from tkinter import Label, Frame

def onLabelClick(index):
    print("Index: {}".format(index))

def loadGame(grid:list, frame:Frame):
    #Frame
    TTT_Label_Frame = Frame(frame,
                        background="white",
                        width=100,
                        height=100,
                        relief="flat")
    for r in range(3):
        for c in range(3):
            labelIndex = r * 3 + c 

            #Label
            TTT_Label = Label(frame, 
                              text=grid[r][c].get(),
                              background="white",
                              fg="black",
                              font=("Arial", 30),
                              width=4,
                              height=2)
            TTT_Label.grid(row=r, column=c, padx=3, pady=3)
            TTT_Label.bind("<Button-1>", lambda event, idx=labelIndex: onLabelClick(idx))
    
    #TTT_Label_Frame.pack(padx=5, pady=5)
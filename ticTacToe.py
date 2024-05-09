from window import createWindow
from TTT_Functions import loadGame
from tkinter import Frame, StringVar

window = createWindow("Tic-Tac-Toe", 700, 700)
TTT_Grid = [[StringVar(value="X") for i in range(3)] for i in range(3)]

TTT_Main_Frame = Frame(window,  
                       background="black",)
TTT_Main_Frame.pack(padx=30, pady=30)

loadGame(TTT_Grid, TTT_Main_Frame)

window.mainloop()
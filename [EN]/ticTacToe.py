from window import createWindow
from TTT_Functions import loadGame, changeTheme, resetGame
from colorHandler import *

from tkinter import Frame, Label, IntVar, BooleanVar, Menu

#Game Window
window = createWindow("TicTacToe - by thelunacodes", 900, 900)

#Game Variables
isDarkTheme = BooleanVar(value=False)
turnNumber = IntVar(value=0)
gameRunning = BooleanVar(value=True)

#Change Window background color based on "isDarkTheme" value
window.config(background=getBackgroundColor(isDarkTheme))

#Turn Label
TTT_Turn_Label = Label(window,
                       text="{}'s turn".format("X" if turnNumber.get() % 2 == 0 else "O"),
                       background=getBackgroundColor(isDarkTheme),
                       fg=getFontColor(isDarkTheme),
                       font=("Arial",20))
TTT_Turn_Label.pack(pady=(50,0))    

#Game Grid Frame
TTT_Grid_Frame = Frame(window,  
                       background=getPadColor(isDarkTheme))
TTT_Grid_Frame.pack(pady=(30,0))

#Game info Label
TTT_Info_Label = Label(window,
                       text="",
                       background=getBackgroundColor(isDarkTheme),
                       fg=getFontColor(isDarkTheme),
                       font=("Arial",20))
TTT_Info_Label.pack(pady=(30,0))

loadGame(TTT_Grid_Frame,
         5,
         turnNumber,
         TTT_Turn_Label,
         TTT_Info_Label,
         gameRunning,
         isDarkTheme)

#Menubar
TTT_Menu = Menu(window)
window.config(menu=TTT_Menu)

#Reset
TTT_Menu.add_command(label="Reset",
                     command=lambda:resetGame(TTT_Grid_Frame,
                                              turnNumber,
                                              TTT_Turn_Label,
                                              TTT_Info_Label,
                                              gameRunning))

#Change Theme
TTT_Menu.add_command(label="Change Theme", 
                     command=lambda:changeTheme(isDarkTheme,
                                                window, 
                                                TTT_Turn_Label, 
                                                TTT_Info_Label,
                                                TTT_Grid_Frame))

window.mainloop()
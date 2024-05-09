from window import createWindow
from TTT_Functions import loadGame, changeTheme, resetGame
from colorHandler import *

from tkinter import Frame, Label, IntVar, BooleanVar, Menu

#Janela do jogo
window = createWindow("Jogo da Velha - por thelunacodes", 900, 900)

#Variáveis do jogo
isDarkTheme = BooleanVar(value=False)
turnNumber = IntVar(value=0)
gameRunning = BooleanVar(value=True)

#Mudar o background da janela com base no valor de isDarkTheme
window.config(background=getBackgroundColor(isDarkTheme))

#Label do turno
TTT_Turn_Label = Label(window,
                       text="Turno de {}".format("X" if turnNumber.get() % 2 == 0 else "O"),
                       background=getBackgroundColor(isDarkTheme),
                       fg=getFontColor(isDarkTheme),
                       font=("Arial",20))
TTT_Turn_Label.pack(pady=(50,0))    

#Frame do tabuleiro de jogo
TTT_Grid_Frame = Frame(window,  
                       background=getPadColor(isDarkTheme))
TTT_Grid_Frame.pack(pady=(30,0))

#Label de informações/mensagens do jogo
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

#Recomeçar
TTT_Menu.add_command(label="Recomeçar",
                     command=lambda:resetGame(TTT_Grid_Frame,
                                              turnNumber,
                                              TTT_Turn_Label,
                                              TTT_Info_Label,
                                              gameRunning))

#Mudar tema
TTT_Menu.add_command(label="Mudar tema", 
                     command=lambda:changeTheme(isDarkTheme,
                                                window, 
                                                TTT_Turn_Label, 
                                                TTT_Info_Label,
                                                TTT_Grid_Frame))

window.mainloop()
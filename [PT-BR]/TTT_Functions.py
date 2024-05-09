from colorHandler import *
from tkinter import Label, Frame, IntVar, BooleanVar, Tk

def turnoJogo(r:int, c:int, frame:Frame, turnNumber:IntVar, turnLabel:Label, infoLabel:Label, gameRunning:BooleanVar):
    if gameRunning.get():
        #Verificar se a célula não está ocupada
        if frame.grid_slaves(row=r, column=c)[0].cget("text") != " ":
            infoLabel.config(text="Essa célula já está ocupada!")
        else:
            #Mudar o texto da label
            frame.grid_slaves(row=r, column=c)[0].config(text="X" if turnNumber.get() % 2 == 0 else "O")
            infoLabel.config(text="")
            #Verificar se o jogador venceu
            if playerWon(frame, "X" if turnNumber.get() % 2 == 0 else "O"):
                infoLabel.config(text="{} venceu!".format("X" if turnNumber.get() % 2 == 0 else "O"))
                gameRunning.set(False)
                return
            else:
                #Encerrar o jogo se o tabuleiro ficar cheio 
                if gridIsFull(frame):
                    infoLabel.config(text="Deu velha!")
                    gameRunning.set(False)
                    return
                else:
                    #Incrementar o valor do turno
                    turnNumber.set(turnNumber.get() + 1)
                    #Atualizar o texto de turnLabel
                    turnLabel.config(text="Turno de {}".format("X" if turnNumber.get() % 2 == 0 else "O"))
    else:
        pass
    
def loadGame(frame:Frame, padSize:int, turnNumber:IntVar, turnLabel:Label, infoLabel:Label, gameRunning:BooleanVar,isDarkTheme:BooleanVar):
    
    #Lista com os valores do padding(padx(esquerda,direita),pady(cima,baixo))
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
            #"Index" do label
            labelIndex = r * 3 + c
            
            #Label da célula
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
            #Verificar se o usuário clicou em um dos labels
            TTT_Label.bind("<Button-1>", lambda event, row=r, col=c: turnoJogo(row, 
                                                                              col, 
                                                                              frame,
                                                                              turnNumber,
                                                                              turnLabel,
                                                                              infoLabel,
                                                                              gameRunning))
            
def playerWon(frame:Frame, symbol:str):
    #Verificação vertical
    for h in range(3):
        if frame.grid_slaves(row=h, column=0)[0].cget("text") == symbol and frame.grid_slaves(row=h, column=1)[0].cget("text") == symbol and frame.grid_slaves(row=h, column=2)[0].cget("text") == symbol:
            return True

    #Verificação horizontal
    for v in range(3):
        if frame.grid_slaves(row=0, column=v)[0].cget("text") == symbol and frame.grid_slaves(row=1, column=v)[0].cget("text") == symbol and frame.grid_slaves(row=2, column=v)[0].cget("text") == symbol:
            return True

    #Verificação diagonal (esquerda)
    if frame.grid_slaves(row=0, column=0)[0].cget("text") == symbol and frame.grid_slaves(row=1, column=1)[0].cget("text") == symbol and frame.grid_slaves(row=2, column=2)[0].cget("text") == symbol:
            return True
    
    #Verificação diagonal (direita)
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
    #Resetar tabuleiro
    for r in range(3):
        for c in range(3):
            frame.grid_slaves(row=r, column=c)[0].config(text=" ")
            turnNumber.set(0)
    
    #Tesetar o texto do TTT_Turn_Label
    TTT_Turn_Label.config(text="Turno de {}".format("X" if turnNumber.get() % 2 == 0 else "O"))

    #Resetar o texto do TTT_Info_Label
    TTT_Info_Label.config(text="")

    #Resetar o valor de gameRunning 
    gameRunning.set(True)

def changeTheme(isDarkTheme:BooleanVar, window:Tk, TTT_Turn_Label:Label, TTT_Info_Label:Label, TTT_Grid_Frame:Frame):
    #Mudar o valor de isDarkTheme
    isDarkTheme.set(not isDarkTheme.get())

    #Mudar a cor do padding
    TTT_Grid_Frame.config(background=getPadColor(isDarkTheme))

    #Mudar a cor do fundo da janela
    window.config(background=getBackgroundColor(isDarkTheme))
    
    #Mudar a cor de fonte e de fundo do TTT_Label
    for r in range(3):
        for c in range(3):
            TTT_Grid_Frame.grid_slaves(row=r, column=c)[0].config(fg=getFontColor(isDarkTheme),
                                                                  background=getLabelBackgroundColor(isDarkTheme))

    #Mudar a cor de fonte e de fundo do TTT_Turn_Label
    TTT_Turn_Label.config(fg=getFontColor(isDarkTheme),
                          background=getBackgroundColor(isDarkTheme))

    #Mudar a cor de fonte e de fundo do TTT_Info_Label
    TTT_Info_Label.config(fg=getFontColor(isDarkTheme),
                          background=getBackgroundColor(isDarkTheme))



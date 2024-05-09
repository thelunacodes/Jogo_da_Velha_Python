from tkinter import Tk

def createWindow(title:str, width:int, height:int):
    window = Tk()
    window.title(title)

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry("{}x{}+{}+{}".format(width, height, x, y))

    return window 


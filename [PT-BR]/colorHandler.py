#Cor de fundo
def getBackgroundColor(darkTheme):
    return "#121213" if darkTheme.get() else "#EFEFEF"

#Cor da fonte
def getFontColor(darkTheme):
    return "#EFEFEF" if darkTheme.get() else "#000000"

#Cor do padding
def getPadColor(darkTheme):
    return "#EFEFEF" if darkTheme.get() else "#000000"

#Cor do fundo da label
def getLabelBackgroundColor(darkTheme):
    return "#121213" if darkTheme.get() else "#FFFFFF"

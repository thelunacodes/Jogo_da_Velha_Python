def getBackgroundColor(darkTheme):
    return "#121213" if darkTheme.get() else "#EFEFEF"

def getFontColor(darkTheme):
    return "#EFEFEF" if darkTheme.get() else "#000000"

def getPadColor(darkTheme):
    return "#EFEFEF" if darkTheme.get() else "#000000"

def getLabelBackgroundColor(darkTheme):
    return "#121213" if darkTheme.get() else "#FFFFFF"

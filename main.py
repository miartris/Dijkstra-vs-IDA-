from sys import argv
from ui.gui import GUI

args = argv[1:]
if len(args) > 0 and args[0] == "-t":
    # Suorituskykytestaus täällä
    pass
else:    
    ui = GUI()
    ui.käynnistä()



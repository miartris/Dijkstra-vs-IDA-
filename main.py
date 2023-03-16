from sys import argv
from ui.gui import GUI
from tests import suorituskykytestaus

args = argv[1:]
if len(args) > 0 and args[0] == "-t":
    testaaja = suorituskykytestaus.Suorituskykytestaus()
    testaaja.testaa()
else:    
    ui = GUI()
    ui.käynnistä()



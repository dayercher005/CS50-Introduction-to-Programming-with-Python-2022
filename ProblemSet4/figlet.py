import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fontList = figlet.getFonts()

if len(sys.argv) == 1:
    string = input()
    randomFont = random.choice(fontList)
    figlet.setFont(font = randomFont)
    print(figlet.renderText(string))
    sys.exit()
elif len(sys.argv) == 3 and sys.argv[1] == '-f' or sys.argv[1] == '--font':
    if sys.argv[2] in fontList:
        string = input()
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(string))
    else:
        sys.exit("Error!")
else:
    sys.exit("Error!")

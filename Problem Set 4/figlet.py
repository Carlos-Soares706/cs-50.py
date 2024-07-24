import sys

import random

from pyfiglet import Figlet

figlet = Figlet()

if (len(sys.argv) == 1):
    randomFont = True

elif (len(sys.argv) == 3) and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    randomFont = False

else:
    print('Invalid usage')
    sys.exit(1)

if randomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print('Invalid usage')
        sys.exit(1)

else:
    rand_font = random.choice(figlet.getFonts())
    figlet.setFont(font=rand_font)

msg = input('Input: ')

print('Output:')
print(figlet.renderText(msg))

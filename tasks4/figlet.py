from pyfiglet import Figlet
import sys

if len(sys.argv) == 1:
    f = Figlet()
elif len(sys.argv) == 3 and (sys.argv[1] in ["-f", "--font"]):
    f = Figlet(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

txt = input("Input: ")
print("Output: ")
print(f.renderText(txt))

def main():
    s = input("Enter text: ")
    print(convert(s))
    
def convert(s):
    s = s.replace(":)", u"\U0001F642")
    s = s.replace(":(", u"\U0001F641")
    return s

main()

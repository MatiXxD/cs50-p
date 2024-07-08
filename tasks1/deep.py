txt = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip()

if txt == "42" or txt.lower() == "forty-two" or txt.lower() == "forty two":
    print("Yes")
else:
    print("No")

names = []
while True:
    try:
        name = input("Input: ")
    except EOFError:
        break
    names.append(name)

if len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}")
elif len(names) == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")
else:
    print("Adieu, adieu, to ", end="")
    for i, name in enumerate(names):
        end_with = ", " 
        if i == len(names) - 1:
            print("and ", end="")
            end_with = "\n"
        print(name, end=end_with)

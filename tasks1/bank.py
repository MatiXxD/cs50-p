greeting = input("Greeting: ").strip()

if greeting.lower().find("hello") != -1:
    print("$0")
elif greeting.lower().startswith("h"):
    print("$20")
else:
    print("$100")

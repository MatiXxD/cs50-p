# Ask user for their name
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print("hello, " + name)
print("hello,", name)
print("hello, ", end="")
print(name)
print(f"hello, {first}")

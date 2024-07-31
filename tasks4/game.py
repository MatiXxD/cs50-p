from random import randint

level = -1
while level <= 0:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass

num = randint(1, level)
guess = -1 
while guess != num:
    try: 
        guess = int(input("Guess: "))
    except ValueError:
        continue

    if guess < num:
        print("Too small!")
    elif guess > num:
        print("Too large!")
print("Just right!")

import random


def main():
    QUESTION_COUNT = 10
    level = get_level()

    score = 0
    for _ in range(QUESTION_COUNT):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        res = num1 + num2

        attempt = 3
        while attempt > 0:
            print(f"{num1} + {num2} = ", end="")
            guess = input()
            if guess.isnumeric() and int(guess) == res:
                score += 1
                break
            else:
                print("EEE")
                attempt -= 1

        if attempt == 0:
            print(f"{num1} + {num2} = {res}")

    print(f"Score: {score}")


def get_level():
    level = input("Level: ")
    while level not in ["1", "2", "3"]:
        level = input()
    return int(level)


def generate_integer(level):
    num = -1
    if level == 1:
        num = random.randint(0, 9)
    elif level == 2:
        num = random.randint(10, 99)
    elif level == 3:
        num = random.randint(100, 999)
    return num


if __name__ == "__main__":
    main()

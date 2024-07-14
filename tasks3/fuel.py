def main():
    x, y = get_fraction("Fraction: ")
    fuel = get_fuel(x, y)
    print(fuel)


def get_fraction(prompt):
    while True:
        fraction = input(prompt).strip().split("/")
        if len(fraction) == 2 and fraction[1] != "0":
            try:
                x, y = int(fraction[0]), int(fraction[1])
                if x <= y:
                    return x, y
            except ValueError:
                pass



def get_fuel(x, y):
    fuel = round(x / y * 100)
    if fuel >= 99:
        return "F"
    elif fuel <= 1:
        return "E"
    else:
        return str(fuel)+"%"


if __name__ == "__main__":
    main()

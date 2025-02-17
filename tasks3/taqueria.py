menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

total_price = 0
while True:
    try:
        total_price += menu[input("Item: ").strip().title()]
    except KeyError:
        pass
    except EOFError:
        break
    else:
        print(f"Total ${total_price:.02f}")

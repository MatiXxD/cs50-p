grocery_list = {}

while True:
    try:
        item = input().strip().upper()
    except EOFError:
        break
    else:
        grocery_list[item] = grocery_list.get(item, 0) + 1

for item, count in sorted(grocery_list.items(), key=lambda pair: pair[0]):
    print(count, item)

def camelcase_to_snakecase(s):
    res = "" 
    for letter in s:
        tmp = str(letter)
        if tmp.isupper():
            res += "_" + tmp.lower() 
        else:
            res += tmp
    return res


s = input("camelCase: ").strip()
print("snake_case:", camelcase_to_snakecase(s))

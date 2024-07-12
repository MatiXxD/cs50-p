def make_shorter(s):
    res = ""
    for letter in s:
        if letter in "aeiouAEIOU":
            continue
        res += letter
    return res


txt = input("Enter some text: ").strip()
print("Output:", make_shorter(txt))

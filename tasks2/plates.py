def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not str(s[0]).isalpha() or not str(s[0]).isalpha():
        return False
    if not s.isalnum():
        return False

    is_first_digit = True
    digit_pos = 7
    letter_pos = 0
    for i, letter in enumerate(s):
        letter = str(letter)
        if letter.isdigit():
            if is_first_digit:
                if letter == "0":
                    return False
                digit_pos = i
                is_first_digit = False
        else:
            letter_pos = i
    return letter_pos < digit_pos


if __name__ == "__main__":
    main()

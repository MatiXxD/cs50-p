def main():
    date = get_date()
    print(date)


def validate_date(date, months, flag):
    if flag == 1:
        try:
            return (
                int(date[0]) >= 1
                and int(date[0]) <= 12
                and int(date[1]) >= 1
                and int(date[1]) <= 31
            )
        except ValueError:
            return False
    elif flag == 2:
        try:
            return (
                int(date[1]) >= 1
                and int(date[1]) <= 31
                and months.get(date[0], -1) != -1
            )
        except ValueError:
            return False
    return False


def get_date():
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }

    while True:
        try:
            inpt = input("Date: ").strip().title()
        except EOFError:
            break
        else:
            if inpt.find("/") != -1:
                date_input = inpt.split("/")
                if len(date_input) == 3 and validate_date(date_input, months, 1):
                    return f"{date_input[2]}-{int(date_input[0]):02}-{int(date_input[1]):02}"
            else:
                date_input = inpt.split(" ")
                date_input[1] = date_input[1][:-1]
                if len(date_input) == 3 and validate_date(date_input, months, 2):
                    return f"{date_input[2]}-{int(months[date_input[0]]):02}-{int(date_input[1]):02}"


if __name__ == "__main__":
    main()

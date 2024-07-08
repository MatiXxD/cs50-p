def main():
    time = input("Enter time: ").strip()
    hours = convert(time)
    
    if hours >= 7.0 and hours <= 8.0:
        print("breakfast time")
    elif hours >= 12.0 and hours <= 13.0:
        print("lunch time")
    elif hours >= 18.0 and hours <= 19.0:
        print("dinner time")


def convert(time):
    time_parts = time.split(" ")
    time = time_parts[0]

    hours, mins = map(float, time.split(":"))
    hours += mins / 60.0 
    if len(time_parts) > 1:
        if time_parts[-1].lower() == "p.m.":
            hours += 12.0

    return hours


if __name__ == "__main__":
    main()

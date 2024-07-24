def main():
    input1 = input("What time is it? ").strip()
    input1 = convert(input1)


    if 7.0 <= input1 <= 8.0:
        print("breakfast time")
    elif 12.0 <= input1 <= 13.0:
        print("lunch time")
    elif 18.0 <= input1 <= 19.0:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    fminute = round(float(minute)/60, 2)
    return float(hour) + fminute


if __name__ == "__main__":
    main()

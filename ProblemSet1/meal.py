def main():
    timing = input("What time is it?")
    mealTime = convert(timing)

    if mealTime >= 7 and mealTime<= 8:
        print("breakfast time")
    elif mealTime >= 12 and mealTime <= 13:
        print("lunch time")
    elif mealTime >= 18 and mealTime <= 19:
        print("dinner time")


def convert(time):
    length = len(time)
    if length == 4:
        hours = time[0]
    else:
        hours = time[0:2]
    minutes = float(time[-2:])/60
    duration = float(hours) + float(minutes)
    return duration


if __name__ == "__main__":
    main()

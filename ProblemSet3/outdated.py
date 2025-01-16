months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    inputDate = input("Enter a Date: ")
    inputDate.strip()
    if "/" in inputDate:
        try:
            month, day, year = inputDate.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

        except ValueError:
            pass

        else:
            if month > 12 or day > 31:
                pass
            else:
                break

    else:
        try:
            monthAndDay, year = inputDate.split(",")
            month, day = monthAndDay.split()
            month = months.index(month) + 1
            day = int(day)
            year = int(year)

        except ValueError:
            pass

        else:
            if month > 12 or day > 31:
                pass
            else:
                break

print(f"{year}-{month:02}-{day:02}")

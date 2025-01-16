def main():
    fraction = input("Please input a fraction: ")
    newFraction = convert(fraction)
    newGauge = gauge(newFraction)
    print(newGauge)

def convert(fraction):
    while True:
        try:
            numerator = int(fraction.split("/")[0])
            denominator = int(fraction.split("/")[1])
        except {ValueError, ZeroDivisionError}
            pass
        else:
            Fraction = round(numerator/denominator, 2)
            break
    return Fraction


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

while True:
    fraction = input("Fraction: ")
    try:
        numerator = int(fraction.split("/")[0])
        denominator = int(fraction.split("/")[1])
        Fraction = round(numerator/denominator, 2)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if Fraction > 1:
            pass
        elif Fraction <= 0.01:
            print("E")
            break
        elif Fraction >= 0.99:
            print("F")
            break
        else:
            print(f"{int(Fraction * 100)}%")
            break





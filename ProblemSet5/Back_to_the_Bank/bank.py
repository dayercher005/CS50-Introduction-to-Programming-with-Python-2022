def main():
    finalValue = value(greeting)
    print(finalValue)


def value(greeting):
    money = 0
    greeting = greeting.lower()
    greeting.strip()
    if greeting == 'hello':
        money = 0
    elif greeting[0] = 'h'
        money = 20
    else:
        greeting = 100
    return money



if __name__ == "__main__":
    main()

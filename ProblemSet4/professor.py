import random


def main():
    attempts = 0
    wrong_tries = 0
    questions = 0
    level = get_level()
    while questions < 10:
        integer1 = generate_integer(level)
        integer2 = generate_integer(level)
        correctAns = integer1 + integer2
        while True:
            try:
                answer = int(input(f"{integer1} + {integer2} = "))
            except ValueError:
                print("EEE")
                attempts += 1
                pass
            else:
                if answer != correctAns and attempts == 2:
                    print("EEE")
                    attempts = 0
                    wrong_tries += 1
                    print(f"{integer1} + {integer2} = {correctAns}")
                    break
                elif answer != correctAns and attempts <2:
                    print("EEE")
                    attempts += 1
                    pass
                elif answer == correctAns:
                    attempts = 0
                    break
        questions += 1

    finalScore = 10 - wrong_tries
    print(finalScore)



def get_level():
    while True:
        try:
            level = int(input("Enter an integer between 1 and 3 inclusive: "))
        except ValueError:
            pass
        else:
            if level > 3 or level < 1:
                pass
            else:
                break
    return level

def generate_integer(level):
    if level == 1:
        randomInteger = random.randint(0, 9)
    elif level == 2:
        randomInteger = random.randint(10, 99)
    else:
        randomInteger = random.randint(100, 999)
    return randomInteger


if __name__ == "__main__":
    main()

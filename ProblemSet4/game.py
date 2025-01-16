import random

while True:
    try:
        level = int(input("Enter a level: "))
    except ValueError:
        pass
    else:
        if level < 1:
            pass
        else:
            number = random.randint(1, level)
            try:
                guessNumber = int(input("Guess the integer: "))
            except ValueError:
                pass
            else:
                if guessNumber < 1:
                    pass
                elif guessNumber < number:
                    print("Too small!")
                elif guessNumber > number:
                    print("Too Large!")
                else:
                    print("Just right!")
                    break

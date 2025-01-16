import inflect

p = inflect.engine()

names = []

while True:
    try:
        newNames = input()
        names.append(newNames)

    except EOFError:
        break

    else:
        print(f"Adieu, adieu, to {p.join(names)}")

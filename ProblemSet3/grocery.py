groceryList = {}

while True:
    try:
        item = input().lower()
    except EOFError:
        break
    else:
        try:
            groceryList[item] += 1
        except KeyError:
            groceryList[item] = 1

for i in sorted(list(groceryList)):
    print(f"{groceryList[i]} {i.upper()}")

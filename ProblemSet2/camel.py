word = input("Enter a string")
newWord = ""
index = 0

for i in word:
    if i == i.lower():
        newWord += i
        index += 1

    else:
        newWord += "_"
        newWord += i.lower()
        index += 1

print(newWord)



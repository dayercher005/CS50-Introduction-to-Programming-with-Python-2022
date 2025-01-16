
def main():
    testcase = shorten(word)
    print(testcase)

def shorten(word):
    word = input("Please input a string: ")
    output = ""
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in word:
        if letter not in vowels:
            output += letter

    return output


if __name__ == "__main__":
    main()

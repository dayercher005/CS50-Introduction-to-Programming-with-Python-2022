def convert(inputString):
    return inputString.replace(":)","🙂").replace(":(","🙁")

def main():
    userString = input()
    print(convert(userString))

main()

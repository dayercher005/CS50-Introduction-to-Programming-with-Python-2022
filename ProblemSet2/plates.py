def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    index = 0
    for i in s:
        if i.isalpha() != True and i.isnumeric() != True: # Ensure that there is no punctuation,periods or spaces
            return False

        if i.isnumeric() == True:  #Ensure that numbers are not used in the middle plate and only come at the end
            for x in s[index:]:
                if x.isalpha() == True:
                    return False
            if i == "0":
                if s[:index].isalpha() == True:
                    return False
        index += 1

    if len(s) > 6 or len(s) < 2: #Ensure that it contains at most 6 characters and at least 2 characters
        return False
    elif s[0].isnumeric() == True or s[1].isnumeric() == True : #Ensure that the first 2 characters start with an alphabet
        return False
    else:
        return True


main()

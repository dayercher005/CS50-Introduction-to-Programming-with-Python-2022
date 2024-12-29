greeting = input("Enter a greeting")
greeting = greeting.strip()
if greeting[0:5] == "Hello":
    print("$0")
elif greeting[0] == "H":
    print("$20")
else:
    print("$100")

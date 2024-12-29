expression = input("Please input an arithmetic expression")

x, y, z = expression.split(" ")

x = float(x)
z = float(z)

match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        print(x / z)
    case _:
        print(9)

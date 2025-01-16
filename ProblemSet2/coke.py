price = 50
while price>0:
    print(f"Amount Due: {price}")
    coin = input("Insert coin: ")
    if coin == "25" or coin =="5" or coin == "10":
        price = price - int(coin)
    else:
        price = price

if price<=0:
    print(f"Change Owed: {-price}")

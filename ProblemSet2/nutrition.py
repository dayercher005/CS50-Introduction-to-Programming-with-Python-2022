fruits = {"apple":130, "Avocado":50, "banana": 110, "cantaloupe":50, "grapefruit": 60, "grapes":90, "Honeydew Melon": 50, "Kiwifruit": 90, "Lemon": 15, "Lime": 20, "Nectarine": 60, "Orange": 80, "Peach": 60, "pear":100, "Pineapple":50, "Plums": 70, "Strawberries": 50, "Sweet Cherries": 100, "Tangerine": 50, "Watermelon" : 80 }
inputFruit = input("Please input a fruit")
for i in fruits:
    if i == inputFruit:
        print(fruits[i])

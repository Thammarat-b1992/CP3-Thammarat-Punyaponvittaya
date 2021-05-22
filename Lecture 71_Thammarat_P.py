menuList = []
priceList = []
total = 0

def showBill():
    print("----- My Food -----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])

while True:
    menuName = input("Plese Enter Menu :")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
        total += menuPrice
showBill()
print("total :", total)
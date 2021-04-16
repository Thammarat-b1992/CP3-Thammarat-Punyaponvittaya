usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "admin" and passwordInput == "1234":
    print("Done !")
    print("---Welcome Exercise 8---")
    print("1.ชาเขียว = 60 บาท")
    print("2.ก๋วยเตี๋ยว = 70 บาท")
    print("3.ลูกชิ้น = 50 บาท")
    print("4.ส้มตำ = 60 บาท")
    print("5.ไก่ย่าง = 55 บาท")
    print("-----------------------")
    userSelected = int(input("เลือกสินค้า 1-5: "))
    if userSelected == 1:
        price = 60
        quantity = int(input("จำนวนที่ต้องการ: "))
        totalPrice = price * quantity
        print("ชาเขียว", quantity, "ชิ้น")
        print("รวมทั้งสิ้น" ,totalPrice, "บาท")
        print("-----------------------")
    elif userSelected == 2:
        price = 70
        quantity = int(input("จำนวนที่ต้องการ: "))
        totalPrice = price * quantity
        print("ก๋วยเตี๋ยว", quantity, "ชิ้น")
        print("รวมทั้งสิ้น" ,totalPrice, "บาท")
        print("-----------------------")
    elif userSelected == 3:
        price = 50
        quantity = int(input("จำนวนที่ต้องการ: "))
        totalPrice = price * quantity
        print("ลูกชิ้น", quantity, "ชิ้น")
        print("รวมทั้งสิ้น" ,totalPrice, "บาท")
        print("-----------------------")
    elif userSelected == 4:
        price = 60
        quantity = int(input("จำนวนที่ต้องการ: "))
        totalPrice = price * quantity
        print("ส้มตำ", quantity, "ชิ้น")
        print("รวมทั้งสิ้น" ,totalPrice, "บาท")
        print("-----------------------")
    elif userSelected == 5:
        price = 55
        quantity = int(input("จำนวนที่ต้องการ: "))
        totalPrice = price * quantity
        print("ไก่ย่าง", quantity, "ชิ้น")
        print("รวมทั้งสิ้น" ,totalPrice, "บาท")
        print("-----------------------")
else:
    print("Error !")
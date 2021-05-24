class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print(self.name,self.lastName,self.age)


customer1 = Customer()
customer1.name = "admin"
customer1.lastName = "admin"
customer1.age = 21
customer1.addCart()

customer2 = Customer()
customer2.name = "admin"
customer2.lastName = "admin"
customer2.age = 22
customer2.addCart()

customer3 = Customer()
customer3.name = "admin"
customer3.lastName = "admin"
customer3.age = 23
customer3.addCart()

customer4 = Customer()
customer4.name = "admin"
customer4.lastName = "admin"
customer4.age = 24
customer4.addCart()
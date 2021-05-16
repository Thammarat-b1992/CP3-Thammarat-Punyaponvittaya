price = (int(input("price : ")))
def vatCalculate(price):
    result = price + (price * 7 / 100)
    return result
print(vatCalculate(price))

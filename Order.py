# Q)Create a class called order which stores item in its price.Use dunder function __gt __() To convey that order1 > order2 if price of order1 > price of order2
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,ord2):
        return self.price>ord2.price
od1=Order("Pizza",200)
od2=Order("Burger",150)
print(od1>od2)
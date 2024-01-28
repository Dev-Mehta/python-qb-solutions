"""
Write a python program that has class store which keeps record of code and price of each product. Display a menu of all 
products to the user and prompt him to enter the quantity of each item required. generate a bill and display total amount.
Sample Output:
enter no of items: 3
enter code of item: milk
enter cost of item: 30
enter code of item: apple
enter cost of item: 35
enter code of item: gems
enter cost of item: 40
Item Code 	 Price
milk 	 30
apple 	 35
gems 	 40
Enter quantity of each item: 
Enter quantity of milk : 2
Enter quantity of apple : 3
Enter quantity of gems : 4
************************Bill**********************
ITEM 	 PRICE QUANTITY 	 SUBTOTAL
milk 	 30 	 2 	 60
apple 	 35 	 3 	 105
gems 	 40 	 4 	 160
**************************************
Total: 325
"""

class Store:
    def __init__(self,items=[]):
        self.items = items

    def accept(self, n: int):
        for i in range(n):
            name = input("Enter name of item: ")
            cost = int(input("Enter cost of item: "))
            self.items.append({"name": name,"cost": cost})
        print("\n************************************************")
        print("*********************menu***********************")
        print("Item\tPrice")
        
        for i in self.items:
            print(f"{i['name']}\t{i['cost']}")

    def bill(self):
        print("Enter quantity of each item. Enter 0 to skip")
        total = 0
        for i in self.items:
            qty = int(input(f"Enter quantity of {i['name']}: "))
            i['qty'] = qty
            total += qty * i['cost']
        print("\n*****************************************************************")
        print("******************************BILL*******************************")
        print("Item\tPrice\tQty\tSubtotal")
        for i in self.items:
            print(f"{i['name']}\t{i['cost']}\t{i['qty']}\t{i['cost']*i['qty']}")
        print("*****************************************************************")
        print(f"Total = {total}")

s = Store()
n = int(input("Enter the number of items: "))
s.accept(n)
s.bill()
"""
You own a pizzeria named Olly’s Pizzas 
and want to create a Python program to handle 
the customers and revenue. Create the following 
classes with the following methods:
Class Pizza containing
1.	init method: to initialize the size 
(small, medium, large), 
toppings (corn, tomato, onion, capsicum, mushroom, olives, 
broccoli), 
cheese (mozzarella, feta, cheddar). 
Note: One pizza can have only one size but many 
toppings and cheese. (1.5 marks)
Throw custom exceptions if the selects toppings or cheese not available in lists given above. (1 mark)
2. price method: to calculate the prize of the pizza in the following way:
small = 50, medium = 100, large = 200
Each topping costs 20 rupees extra, 
except broccoli, olives and mushroom, 
which are exotic and so cost 50 rupees each.
Each type of cheese costs an extra 50 rupees. (1.5 marks)

Class Order containing
1.	init method: to initialize the name, customerid 
    of the customer who placed the order (0.5 marks)
2.	order method: to allow the customer to select pizzas 
    with choice of toppings and cheese (1 mark)
3.	bill method: to generate details about each pizza 
    ordered by the customer and the total cost of the order. (2 marks)
*Note: A customer can get multiple pizzas in one order.
1.5 marks for creating appropriate objects of these classes and writing correct output.
"""
class Pizza:
    class ToppingError(Exception):
        pass

    class CheeseError(Exception):
        pass

    class SizeError(Exception):
        pass
    ALLOWED_SIZES = ('small', 'medium', 'large')
    ALLOWED_TOPPINGS = ('corn', 'tomato', 'onion', 'capsicum', 'mushrooms', 'olives', 'broccoli')
    ALLOWED_CHEESE = ('mozzarella', 'feta', 'cheddar')
    prices = {'small':50, 'medium':100, 'large':200}
    def __init__(self, size: str, toppings: list, cheese: list):
        if not size in self.ALLOWED_SIZES:
            raise Pizza.SizeError("Invalid size option", size)
        valid_cheese = all([ch in self.ALLOWED_CHEESE for ch in cheese])
        if not valid_cheese:
            raise Pizza.CheeseError("Invalid cheese option")
        valid_toppings = all([topping in self.ALLOWED_TOPPINGS for topping in toppings])
        if not valid_toppings:
            raise Pizza.ToppingError("Invalid topping entered")
        else:
            self.size = size
            self.cheese = cheese
            self.toppings = toppings

    def price(self):
        base = self.prices[self.size]
        base += len(self.toppings)*20
        exotics = ['mushrooms', 'broccoli', 'olives']
        for exotic in exotics:
            if exotic in self.toppings:
                base += 30
        base += len(self.cheese) * 50 # for cheese
        return base
    
class Order:
    def __init__(self, name, customerid):
        self.name = name
        self.customerid = customerid

    def order(self, n: int):
        self.pizzas = []
        for i in range(n):
            toppings = []
            cheese = []
            size = input("Enter size: ")
            while size not in Pizza.ALLOWED_SIZES:
                print("Enter valid size: [Choices][small, medium, large]")
                size = input("Enter size: ")
            tc = int(input("Enter count of toppings: "))
            print("Choices: ", Pizza.ALLOWED_TOPPINGS)
            for i in range(tc):
                tp = input("Enter topping: ")
                if tp not in Pizza.ALLOWED_TOPPINGS:
                    raise Pizza.ToppingError("Invalid topping " + tp)
                else:
                    toppings.append(tp)
            c = int(input("Enter cheese count: "))
            print("Choices: " , Pizza.ALLOWED_CHEESE)
            for i in range(c):
                tp = input("Enter cheese type: ")
                if tp not in Pizza.ALLOWED_CHEESE:
                    raise Pizza.CheeseError("Invalid cheese " + tp)
                else:
                    cheese.append(tp)
            pizza = Pizza(size, toppings, cheese)
            self.pizzas.append(pizza)

    def bill(self):
        self.total = 0
        i = 1
        print("********************************")
        for p in self.pizzas:
            print("Pizza", i)
            print(p.size, p.toppings, p.cheese)
            print(f"Pizza {i} price: {p.price()}")
            i += 1
            self.total += p.price()
            print("********************************")
        print("Total: ", self.total)

n = int(input("Enter num of pizzas: "))
order = Order("Dev", "MYORDERID#22")
order.order(n)
order.bill()
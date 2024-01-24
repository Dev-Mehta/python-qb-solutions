"""
Write a function cust_data() to ask user to enter their names and age to store data in customer.txt file. 
"""

from helper import File, inti, ip

num_of_customers = inti("Enter number of customers: ")

f = File("customers.txt", "w+")
for i in range(num_of_customers):
    name = ip(f"Enter name of customer [{i+1}]: ")
    age = inti(f"Enter age of customer[{i+1}]: ")
    f.write(f"{name} : {age}\n")
f.save_as("503_customers.txt")
f.delete()
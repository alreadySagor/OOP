"""
Docstring for Restaurant_Management

check line between 82 to 87 (maybe 85)
self.items.items() er mane ki?

... self.items --> Order class e chilo
    (self.items = {}, mane items holo ekta dictionary.
    Format : {
                FoodItem : Quantity
              }
    example : {
                burger_obj : 2,
                pizza_obj : 1
               }
    )
    ekhon : .items() ki kore?
    ... Eta dictionary method.
    ... Eta Key-value pair return kore.
    
    folafol : dict_items([
        (burger_obj, 2),
        (pizza_obj, 1)
    ])

Tahole ami bolte pari...
..> self.items মানে Order ক্লাসের items নামের dictionary।
আর .items() সেই dictionary এর ভিতরে থাকা সব key-value pair (key, value) আকারে return করে।

ba..
...> self.items.items() Order ক্লাসের items dictionary থেকে প্রতিটা element কে (key, value) tuple আকারে রিটার্ন করে।

ba..
...> Order ক্লাসের cart এ যা যা আছে,
.items() সেগুলাকে (item, quantity) বানিয়ে দেয়।

ba..
...> self.items.items() dictionary থেকে সব key-value pair এনে দেয়।
"""

from abc import ABC

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu() # menu class er object ke nilam

    def add_employee(self, employee): # employee er object ke ekhane pass kore dibo
        self.employees.append(employee)
    
    def view_employee(self):
        print('---------------------------------')
        print('*** Employee List ***')
        for emp in self.employees:
            print(f'Name : {emp.name} <--> Phone : {emp.phone} <--> Email : {emp.email} <--> Address : {emp.address}')
        print('---------------------------------')

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Menu:
    def __init__(self):
        self.items = [] # Sob food Item ekhane thakbe..
    
    def add_item(self, item):
        self.items.append(item) # item er object ashbe setake nibo/nilam

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item # khuje pele item jabe..
        return None # Na khuje pele None jabe..

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item: # item ta jodi exists kore
            self.items.remove(item)
            print('---------------------------------------')
            print('Item Deleted !!!') 
            print('---------------------------------------')
        else:
            print('---------------------------------------')
            print('Item Not Found !!!')
            print('---------------------------------------')
    
    def show_menu(self):
        print('----------------------------------')
        print('\t*** Menu ***')
        print('***********************')
        print('Name\tPrice\tQuantity')
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')
        print('----------------------------------')


class Order:
    def __init__(self):
        self.items = {} # Customer er cart {FoodItem : quantity}

    def add_item(self, item): # item er object ashbe
        if item in self.items:
            self.items[item] += item.quantity # item ta jodi cart e already thake
        else:
            self.items[item] = item.quantity # item ta cart e jodi na thake
        
    def remove(self, item):
        if item in self.items:
            del self.items[item]
    
    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items()) # ei line ta eita mean kore ("total = 0" "for item, quantity in self.items.items():" "total += item.price * quantity" "return total")
    
    def clear(self):
        self.items = {} # cart khali kore



class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order() # order class er object # Prottek customer er nijossho cart

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()
    
    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print('------------------------------------')
                print('Item Quantity Exceeded !!')
                print('------------------------------------')
            else:
                item.quantity -= quantity
                self.cart.add_item(item)
                print('------------------------------------------')
                print('Item Added')
                print('------------------------------------------')
        else:
            print('------------------------------------------')
            print('Item Not Found')
            print('------------------------------------------')
        
    def view_cart(self):
        print('------------------------------------------')
        print('\t*** View Cart ***')
        print("***************************")
        print('Item Name\tPrice\tQuantity')
        for item, quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        print('-----------------')
        print(f'Total Price : {self.cart.total_price}')
        print('-----------------')
        print('------------------------------------------')
    
    
    def pay_bill(self):
        print('--------------------------------------------')
        print(f'Total {self.cart.total_price} paid successfully')
        self.cart.clear()
        print('--------------------------------------------')

class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employees = []
    
    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)
    
    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_item(self, restuarent, item):
        restuarent.menu.add_item(item)
    
    def remove_item(self, restaurant, item):
        restaurant.menu.remove_item(item)

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

#------------------------------------------------------------------------
mamar_restaurant = Restaurant('Mamar_Restaurant')

def customer_menu():
    name = input('Enter Your Name : ')
    email = input('Enter Your Email : ')
    phone = input('Enter Your Phone : ')
    address = input('Enter Your Address : ')

    # func er moddhe kon serial e ache seta janina tai variable naam diye pathiye dilam
    customer = Customer(name=name, email=email, phone=phone, address=address)

    while(True):
        print(f'Welcome {customer.name}!!')
        print('1. View Menu')
        print('2. Add item to cart')
        print('3. View cart')
        print('4. PayBill')
        print('5. Exit')

        option = int(input('Enter Option: '))
        if option == 1:
            customer.view_menu(mamar_restaurant)
        elif option == 2:
            item_name = input('Enter item name: ')
            item_quantity = int(input('Enter item quantity: '))
            customer.add_to_cart(mamar_restaurant, item_name, item_quantity)
        elif option == 3:
            customer.view_cart()
        elif option == 4:
            customer.pay_bill()
        elif option == 5:
            break
        else:
            print('Envalid input!!')

def admin_menu():
    name = input('Enter your Name: ')
    email = input('Enter your Email: ')
    phone = input('Enter your Phone: ')
    address = input('Enter your Address: ')
    # func er moddhe kon serial e ache seita janina tai variable naam diye pathiye dilam
    admin = Admin(name = name, email = email, phone = phone, address = address)

    while True:
        print(f'Welcome {admin.name}!!')
        print('1. Add New Item')
        print('2. Add New Employee')
        print('3. View Employee')
        print('4. View Items')
        print('5. Delete Item')
        print('6. Exit')

        option = int(input('Enter Option: '))
        if option == 1:
            item_name = input('Enter Item Name: ')
            item_price = int(input('Enter Item Price: '))
            item_quantity = int(input('Enter Item Quantity: '))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_item(mamar_restaurant, item)

        elif option == 2:
            name = input('Enter Employee Name: ')
            phone = input('Enter Employee Phone: ')
            email = input('Enter Employee Email: ')
            address = input('Enter Employee Address: ')
            designation = input('Enter Employee Designation: ')
            age = int(input('Enter Employee Age: '))
            salary = int(input('Enter Employee Salary: '))
            employee = Employee(name, phone, email, address, age, designation, salary)
            admin.add_employee(mamar_restaurant, employee)

        elif option == 3:
            admin.view_employee(mamar_restaurant)
        elif option == 4:
            admin.view_menu(mamar_restaurant)
        elif option == 5:
            item_name = input('Enter Item Name: ')
            admin.remove_item(mamar_restaurant, item_name)
        elif option == 6:
            break
        else:
            print('Envalid input!!')


while True:
    print('Welcome!')
    print('1. Customer')
    print('2. Admin')
    print('3. Exit')

    option = int(input('Enter Option: '))

    if option == 1:
        customer_menu()
    elif option == 2:
        admin_menu()
    elif option == 3:
        break
    else:
        print('Envalid Input!')
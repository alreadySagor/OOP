from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restuarent):
        # restuarent class er moddhe gelam, sekhan theke Menu class e gelam
        # Menu class er jei show item ache seitake call kore dilam
        restuarent.menu.show_menu()

    def add_to_cart(self, restuarent, item_name, quantity):
        item = restuarent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print('Item quantuty exceeded!!')
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print('Item added')
        else:
            print('Item not found!!')

    def view_cart(self):
        print('\t*****View Cart*****')
        print('------------------------')
        print('Name\tPrice\tQuantity')
        for item, quantity in self.cart.items.items(): # items naam er function ta je python e use kora hoy dictionary er jonno, oi items func ta key & value ke pair hisebe ber kore ane
            print(f'{item.name}\t{item.price}\t{quantity}') # quantity ta user er kach theke nebo tai items. likhinai
        print(f'Total Price: {self.cart.total_price}')

    def pay_bill(self):
        print(f'Total {self.cart.total_price} paid successfully')
        self.cart.clear()

class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


# Admin onnano class er method gula call korar maddhome sob kaj korbe
class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employees = [] # eta hocche amader database (ekhane employee add kora hobe)

    def add_employee(self, restuarent, employee):
        # restuarent er obj ke nilam
        # restuarent ekta obj, tar moddhe Restuarent er ekta method add_employee ke call kore employee obj ke pathiye dilam
        # etake call korle employee add korar kaj ta Restuarent class korbe
        restuarent.add_employee(employee)

    # same as Admin's add_employee   
    def view_employee(self, restuarent):
        # admin, Restuarent er view_employee ke call kore employee der dekhbe
        restuarent.view_employee()

    # resutuarent class er moddhe menu naam er je variable 
    # ta ache tar moddhe (menu er moddhe FoodItem er obj ta capture hobe)
    # ekhon ei menu diye ami Menu class er sob func gula access korte pari
    # tahole Menu er moddhe jei add_menu_item naam er jei func ache oita ekhane bosai dite pari
    def add_new_item(self, restuarent, item):
        restuarent.menu.add_menu_item(item)

    def remove_item(self, restuarent, item):
        restuarent.menu.remove_item(item)

    def view_menu(self, restuarent):
        restuarent.menu.show_menu()
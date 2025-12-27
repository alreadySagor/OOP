from food_item import FoodItem
from menu import Menu
from users import Customer, Admin, Employee
from restaurent import Restuarent
from orders import Order

mamar_restuarent = Restuarent('Mamar Restuarent')
def customer_menu():
    name = input('Enter your Name: ')
    email = input('Enter your Email: ')
    phone = input('Enter your Phone: ')
    address = input('Enter your Address: ')
    # func er moddhe kon serial e ache seita janina tai variable naam diye pathiye dilam
    customer = Customer(name = name, email = email, phone = phone, address = address)

    while True:
        print(f'Welcome {customer.name}!!')
        print('1. View Menu')
        print('2. Add item to cart')
        print('3. View cart')
        print('4. PayBill')
        print('5. Exit')

        option = int(input('Enter Option: '))
        if option == 1:
            customer.view_menu(mamar_restuarent)
        elif option == 2:
            item_name = input('Enter item name: ')
            item_quantity = int(input('Enter item quantity: '))
            customer.add_to_cart(mamar_restuarent, item_name, item_quantity)
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
            admin.add_new_item(mamar_restuarent, item)

        elif option == 2:
            name = input('Enter Employee Name: ')
            phone = input('Enter Employee Phone: ')
            email = input('Enter Employee Email: ')
            address = input('Enter Employee Address: ')
            designation = input('Enter Employee Designation: ')
            age = int(input('Enter Employee Age: '))
            salary = int(input('Enter Employee Salary: '))
            employee = Employee(name, phone, email, address, age, designation, salary)
            admin.add_employee(mamar_restuarent, employee)

        elif option == 3:
            admin.view_employee(mamar_restuarent)
        elif option == 4:
            admin.view_menu(mamar_restuarent)
        elif option == 5:
            item_name = input('Enter Item Name: ')
            admin.remove_item(mamar_restuarent, item_name)
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
from menu import Menu

class Restuarent:
    def __init__(self, name):
        self.name = name
        self.employees = [] # eta hocche amader database (ekhane employee add kora hobe)
        self.menu = Menu() # Menu class ke obj hisebe rekhe dilam

    def add_employee(self, employee): # employee naam er obj pass kore dibo eikhane
        self.employees.append(employee)

    def view_employee(self):
        print('Employee List!!')
        for emp in self.employees:
            print(f'Name: {emp.name} <--> Phone: {emp.phone} <--> Email: {emp.email} <--> Address: {emp.address}')
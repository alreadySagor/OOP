class Company:
    def __init__(self, name, address):
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counters = []
        self.managers = []
        self.supervisors = []
        self.fare = [] # vara

class Driver:
    def __init__(self, name, license, age):
        self.name = name
        self.lisence = license
        self.age = age

class Counter:
    def __init__(self):
        pass
    def purchase_a_ticket(self, start, destination):
        pass

class Passenger:
    pass

class Supervisor:
    pass

class Manager:
    pass

class Route:
    pass


laal_mia = Driver('LaalMiya', 'urff3242', 43)
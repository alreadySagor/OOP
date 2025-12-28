from abc import ABC, abstractmethod
from ride import Ride_Request, RideMatching

class User(ABC): # eta mean kore je user class er object kokhono make korbo na
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self): # ei abstact base class ta kind of chach(sach) hisebe kaj korbe, etar implementation ta kokhonoi abstract base class e hoy na, eta implement hoy ey class ke je inherite korbe sekhane ei display_function(method) ta must use korte hobe
        raise NotImplementedError
    

class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount):
        super().__init__(name, email, nid)
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location

    def display_profile(self):
        print(f'Rider: {self.name} and Email {self.email}')

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print('Amount less than 0')
    
    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self, ride_sharing, destination, vehicle_type):
        ride_request = Ride_Request(self, destination) # self means object of ride class
        ride_matching = RideMatching(ride_sharing.drivers)
        ride = ride_matching.find_driver(ride_request, vehicle_type)
        ride.rider = self
        self.current_ride = ride
        print("Yah!! We got a ride!!")

    def show_current_ride(self):
        print('Ride Details!!')
        print(f'Rider: {self.name}')
        print(f'Driver: {self.current_ride.driver.name}')
        print(f'Selected Car: {self.current_ride.vehicle.vehicle_type}')
        print(f'Started Location: {self.current_ride.start_location}')
        print(f'End Location: {self.current_ride.end_location}')
        print(f'Total cost: {self.current_ride.estimated_fare}')

    

class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0
    
    def display_profile(self):
        print(f'Driver: {self.name}')
    
    def accept_ride(self, ride):
        ride.start_ride()
        ride.set_driver(self) # driver er object dite hobe[ekhane self maanei driver class er object ke mean korteche]

    def reach_destination(self, ride):
        ride.end_ride()
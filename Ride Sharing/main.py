from ride import Ride, Ride_Request, RideMatching , RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

niye_jao = RideSharing('niye jao')
rahim = Rider('Rahim uddin', 'rahim@gmail.com', 8734857, 'mohakhali', 1200)
niye_jao.add_rider(rahim)

kolim = Driver('Kolim uddin', 'kolim@gmail.com', 75343, 'Gulshan')
niye_jao.add_driver(kolim)

rahim.request_ride(niye_jao, 'Uttara', 'car')

kolim.reach_destination(rahim.current_ride)
rahim.show_current_ride()
print(niye_jao)
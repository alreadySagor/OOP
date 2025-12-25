class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.name} {self.price}'

    def move(self):
        pass

class Bus(Vehicle):
    def __init__(self, name, price, seat):
        self.seat = seat
        # Vehicle.__init__(name, price) --> এটা একদম নিচের লাইনের মতোই কাজ করে
        super().__init__(name, price)
    
    def __repr__(self):
        # return Vehicle.__repr__() --> এটা একদম নিচের লাইনের মতোই কাজ করে
        return super().__repr__()
    

class Truck(Vehicle):
    def __init__(self, name, price, weight):
        self.weight = weight
        super().__init__(name, price)

class PickUpTruck(Truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)

class AcBus(Bus):
    def __init__(self, name, price, seat, temparature):
        self.temaparature = temparature
        super().__init__(name, price, seat)

    def __repr__(self):
        print(f'{self.seat}')
        return super().__repr__()

green_line = AcBus('Green', 5000000, 22, 16)
# eivabe call hobe:
# AcBus --> super() == super maane AcBus er parent ke taake call korteche
# Bus --> super() == super maane Bus er parent ke taake call korteche
# AcBus --> super() --> Bus --> super() --> Vehicle

print(green_line)

#--------------------------------------------------------------------------------------------------------------------------------------------
"""
super() Call Chain Diagram

print(green_line)
        |
        v
AcBus.__repr__()
   |
   |-- print(self.seat)        ---> 22  (এখানেই আগে প্রিন্ট হয়)
   |
   v
super().__repr__()  (Bus)
        |
        v
Bus.__repr__()
        |
        v
super().__repr__()  (Vehicle)
        |
        v
Vehicle.__repr__()
        |
        v
return "Green 5000000"
        |
        v
print(...)  ---> Green 5000000

"""
#--------------------------------------------------------------------------------------------------------------------------------------------




"""

1️⃣ super() কী?

super() ব্যবহার করা হয় parent class (base class) এর method বা constructor কল করার জন্য।

এখানে:

Vehicle → parent class

Bus → child class

অর্থাৎ Bus ক্লাস থেকে আমরা Vehicle ক্লাসের জিনিস ব্যবহার করতে চাই।

2️⃣ এই লাইনটা দেখো 👇
super().__init__(name, price)


এর মানে হচ্ছে:

👉 Vehicle ক্লাসের __init__ মেথড কল করো

এটা একদম নিচের লাইনের মতোই কাজ করে:

Vehicle.__init__(self, name, price)


কিন্তু super() ব্যবহার করাই best practice।

3️⃣ Bus ক্লাসে super() না দিলে কী হতো?

ধরো তুমি super() ব্যবহার করোনি:

class Bus(Vehicle):
    def __init__(self, name, price, seat):
        self.seat = seat


এখন যদি করো:

bus = Bus("Green Line", 2000000, 40)
print(bus.name)


❌ Error আসবে:

AttributeError: 'Bus' object has no attribute 'name'


কারণ:

name এবং price সেট হয় Vehicle.__init__ এ

তুমি সেটা কলই করোনি

4️⃣ super() থাকলে কী হয়?
class Bus(Vehicle):
    def __init__(self, name, price, seat):
        self.seat = seat
        super().__init__(name, price)


এখন কাজের flow হবে:

1️⃣ Bus.__init__ কল হয়
2️⃣ self.seat = seat
3️⃣ Vehicle.__init__ কল হয়
4️⃣ self.name = name
5️⃣ self.price = price

এখন Bus object-এ থাকবে:

bus.name
bus.price
bus.seat


সব ঠিকঠাক ✅

5️⃣ __repr__ মেথডে super() কেন?
def __repr__(self):
    return super().__repr__()


এর মানে:

👉 Vehicle ক্লাসের __repr__ ব্যবহার করো

এটা সমান:

return Vehicle.__repr__(self)


তাই:

bus = Bus("Hanif", 3000000, 45)
print(bus)


Output হবে:

Hanif 3000000


কারণ Bus নিজের __repr__ না লিখে parent এরটা reuse করছে।

6️⃣ সহজ ভাষায় সংক্ষেপে 💡
জায়গা	super() কী করে
__init__	Parent ক্লাসের constructor কল করে
__repr__	Parent ক্লাসের method ব্যবহার করে
কেন দরকার	কোড repeat না করে reuse করার জন্য
7️⃣ এক লাইনে মনে রাখার ট্রিক 🧠

super() = “আমার parent ক্লাসের জিনিসটা ব্যবহার করো”

"""
# base class / parent class

class BaseClass:
    pass

# DerivedClass /ChildClass
class DerivedClass(BaseClass): # DerivedClass BaseClass ke inherite korbe
    pass

""" 
1. simple inheritance: parent class --> child class (Gadget --> Phone) (Gadget --> Laptop)
2. Multi - level inheritanc: Grandpa --> parent --> child (vehicle --> Bus --> AcBus) 
  (Vehicle --> Truck --> PickUpTruck)
  (Vehicle --> Bus --> AcBus)

3. Multiple Inheritance: Student (Family, School, Sports)

4. Hybrid (multi-level + multiple): Grandpa --> Father, Uncle, Aunty --> Child (Father, Uncle)
"""
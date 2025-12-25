# inheritance provide you "is a" relation ("is a" relation)
# etar halka ektu different version hocche composition

""" Composition """
class Engine:
    def __init__(self):
        pass

    def start(self):
        return 'Engine started'

class Driver:
    def __init__(self):
        pass
# car "has a" engine ("has a" relation)
class Car:
    def __init__(self):
        self.engine = Engine()
        self.driver = Driver()

    def start(self):
        self.engine.start()
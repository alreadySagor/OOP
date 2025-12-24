# animal ra sobai eki food khay na, sobai jate sobar moto food
# khete pare tai import korlam ABC
from abc import ABC, abstractmethod
# abc --> abstract base class
class Animal(ABC):
    @abstractmethod # enforce all derived class to have a eat method
    def eat(self):
        print('I need food')
        pass
    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name):
        self.category = 'Monkey'
        self.name = name
        super().__init__()
    def eat(self):
        print('Eating banana')
    def move(self):
        print('Hanging on the branches')

layka = Monkey('Lucky')
layka.eat()
layka.move()



""" amra chai je hocche monkey tar nijossho (Animal er eat e jodi
banana thake tahole sobai to aar banana khabe na, jemon tiger khabe mangsho)
tai amra chai je animal er moddhe kichu thakuk aar na thakuk. Ekhon amader system ta hobe 
ei je jei hocche Animal ke use kori na keno amake kintu ei eat ta amar moto
kore ekta method e implement korte hobe (inforce korbo). To sei inforce korar jonno
python e emon ekta jinish ache seta hocche [from abc import ABC, abstractmethod (abc --> abstract base class)]
eta niye nilam, ekhon amra bolbo je tomar jei Animal ta ache eita ke Inherite korbo kotha theke? ABC theke
"class Animal(ABC):| tarpor eat er aage (eitake decorator bole, amra aste dheere janbo) eita diye dibo
@abstractmethod | ekhon taile ki obostha hoy run korle dekha jay monkey take eat soho make korte partechena
                | karon ki? karon eat asole Monkey class er moddhe nai. karon @abstractmethod bolteche
                (inforce all derived class to have a eat method) tar maane sob gula child class jara eitake inherite korbe(Animal ke) tader 
                sobar eat method ta thaktei hobe (@abstractmethod er niche jei method thakbe seitakei inforce korbe)

abstractmethod er kachakachi ekta jisnish ache (interface) jeitar difference amra janbo
"""
##ABSTRACTION:
##    abstract base class - hiding the unecessary datas, only showing important data to user

from abc import ABC, abstractmethod
class Flipcard(ABC):
    @abstractmethod
    def mobiles(self):
        print("code program")
class User(Flipcard):
    def mobiles(self):
        print("screen is visible")
        print("choose anything")

ram=User()
ram.mobiles()

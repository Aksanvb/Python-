##ENCAPSULATION :
##    encapsulation means hiding internal details of a class and only exposing what's
##    necessary.it helps to protect important data from being changed directly and keeps
##    the code secure and organized.

##Access modifiers :
##    public
##    protected(_)
##    private(__)

class Person:
    def walk(self):
        print("walking")
        self._singlehand()
    def _singlehand(self):
        print("Riding in single hand")
        self.__Withouthand()
    def __Withouthand(self):
        print("Not possible")
a=Person()
##a._singlehand()
##a.__Withouthand()
a.walk()

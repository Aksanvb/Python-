##POLYMORPHISM:
##    poly--many
##    morphism--behaviour

##method overriding:
##    different class, same method and same parameter

class Dad:
    def action(self):
        print("he is a left hander")
    def act(self):
        print("good morning")
class Son(Dad):
     def action(self):
         super().action() #above and below sts can be used
         print("he is a right hander")
        
a=Son()
a.action()

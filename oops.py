##OOPS : Object Oriented Programming Language - it is used object and classes in programming
##
##CLASS :
##    it is a collection of objects and it is an blue print for the objects
##
##    SYNTAX :
##        class classname: classname-1st letter uppercase
##            .
##            .
##            statements
##            .
##            .
##            .
##            .
##OBJECTS :
##    it is an instance of the class and it acts as an real world entity. the object is defined
##    as attributes (data)(name,age,gender(like that)) and behaviour (methods) action
##
##    SYNTAX :
##        object = classname

##class Person:
##    fruit_1="apple"
##    fruit_2="cherry"
##
##a=Person()
##shop_keeper=Person()
##print(a.fruit_1)
##print(a.fruit_2)
##print(shop_keeper.fruit_1)
##print(shop_keeper.fruit_2)

##class Person():
##    name=""
##    age=0
##a=Person()
##b=Person()
##a.name="Ram"
##b.name="Sam"
##a.age=22
##b.age=20
##print(a.name)
##print(b.name)

##a.name=input("Enter name:")
##b.name=input("Enter name:")
##a.age=int(input("Enter your age:"))
##b.age=int(input("Enter your age:"))
##print(a.name)
##print(b.name)
##print(a.age)
##print(b.age)

##class Park:
##    a=10
##    b=20
##    name=" "
##    def walk(s):
##        print("walking",s.a)
##    def jog(s):
##        print("jogging")
##ram=Park()
##ram.name="Ram"
##ram.walk()

##class Park:
##    name=" "
##    age=0
##    def walk(s,Min):
##        print("walking",s.name,Min)   #no need to give s. while giving the value through positional arguement..otherwise s. is needed (s=self)
##    def jog(s):
##        print("jogging",s.name)
##        
##ram=Park()
##ram.name="Ram"
##ram.walk(int(input("enter the duration of walking:")))
##sam=Park()
##sam.name="Samuel"
##sam.walk(int(input("enter the duration of walking:")))


##__init__ method is special method --- CONSTRUCTOR :
##    A constructed object is a unique function that gets called automatically when an object is created of a class

##class Person:
##    def __init__(self):
##         print("welcome")
##         print("good morning")
##    def walk(self):
##        print("walking")
##    def run(self):
##        print("running")
##sam=Person()
##sam.walk()


##class Person:
##    def __init__(self,ID,Pass):
##        self.name=ID
##        self.Pass=Pass
##    def home(self):
##        b=["hi","hello"]
##        for i in b:
##            print(i)
##        print(self.name)
##    def home2(self):
##        print(self.Pass)
##a=Person("E4108","es123")
##a.home()
##a.home2()


##IHERITANCE :
    ##it is used to inherits all the methods and properties from another class
##single inheritance  :
##    Parent
##    Child
##class Parent:
##    def assets(self):
##        print("10")
##class Child(Parent):
##    def amt(self):
##        print("5")
##obj=Parent()
####obj=Child()
####obj.amt()
##obj.assets()

# multilevel inheritance

##class Grandparent:
##    a=100
##    def home1(self):
##        print("i have a own house")
##class Parent(Grandparent):
##    def home2(self):
##        print("i have a car")
##class Child(Parent):
##    def home3(self):
##        print("i have a bike",self.a)
##obj=Child()
##obj.home3()

# multiple inheritence

##class person1:
##    def fun1(self):
##        print("we are first parents")
##class person2:
##    def fun2(self):
##        print("we are second parents")
##class person3:
##    def fun3(self):
##        print("we are third parents ")
##class child(person1,person2,person3):
##    def son(self):
##        print("hiiiiiiii")
##obj=child()
##obj.fun3()
##obj.fun2()
##obj.fun1()
##obj.son()


##hierarchial inheritance : #no child share

##class parents:
##    def fun(self):
##        print("yes this is my child")
##class child1:
##    def fun1(self):
##        print("im the first child of my parents")
##class child2:
##    def fun2(self):
##        print("im the second child of my parents")
##class child3:
##    def fun3(self):
##        print("im the third child of my parents")
##
##obj=child2()
##obj.fun1()
##obj.fun2()

##hybrid inheritance :

##class Base:
##    def base_method(self):
##        print("this is the base class")
##class parent1(Base):   #base class data can be used if base is in the paranthesis
##    def method1(self):
##        print("thi is method1")
##class parent2:
##    def method2(self):
##        print("this is method2")
##class Child(parent1,parent2):
##    def child_method(self):
##        print("this is the Child class.")
##
###obj=Child() any class's data can be used
##obj=parent1()
##obj.base_method()



































##DICTIONARY :
##    key value pair
##    mutable
##    ordered
##    unindexed
##    value are allow duplicate values,values i smutable
##    key does not allow duplicate values,key is immutable

##a={"value1":10,20:10}
##print(a[20])

##a={"Tamil":70,"English":60,"Maths":60}
##print(a["Maths"])

##for i in a:      #for printing the keys alone
##    print(i)

##for i in a:      #for printing the values alone
##    print(a[i])
    
     
####METHODS :

##1. get, 2. setdefault :

##a={"name":"Rahul","age":25}
##print(a.get("age"))
##print(a.get("gender","male"))   #temprory

##c=a.setdefault("e_no",5820)
##print(c)
##print(a) 

##3. clear, 4. copy :

##a={"key":"Good morning"}
##b=a.copy()                #diff id same value,copied one clear but original wont clear
##b.clear
##print(a)

##a={"key":"Good morning"}
##b=a                       #same id for both og n copied
##a.clear()                 #original will be cleared
##print(a)


##5.items, 6.keys, 7.values, 8.pop, 9.popitem, 10.update :

##a={"colour":"Black","name":"Red","brand":"A1"}
##print(a.items())  #keys and values
##print(a.keys())
##print(a.values())
##a.update({"colour":"yellow"})
##print(a)

 #or

##a["colour"]="Green"
##print(a)


##a.pop("name")  #removes particular item
##print(a)

##a.popitem()  #removes last item
##print(a)

##a={"Student_1":{"name":"akash","age":21},
##   "Student_2":{"name":"ram","age":20}}

##for i in a:
##    print(i)                  #to print the value of outside dictionary
##    for j in a[i]:            #to print the keys in nested dictionary
##           print(j,a[i][j])     #to print the value inside nested dictionary..print(j) for keys alone

##a={"Student_1":{"name":{"akash":21}},
##   "Student_2":{"name":"ram","age":20}}
##print(a["Student_1"]["name"]["akash"])


































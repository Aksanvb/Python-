##SET :
##    mutable
##    add or remove elements
##    unchangeable
##    unordered
##    unindexed
##    does not allow duplicatge value

##a={10,20,30,"varchar",50,10}
##print(a)

##a={50,30,40,20,10}
##b=1
##for i in a:
##    if i==10:
##        while i>b:
##            print(b)
##            b=b+1
##    else:
##        print(i)

##1. ADD :

##a={1,2,3,4,5,"hi"}
##a.add(value)
##print(a)


##2. CLEAR
##3. COPY :

##a={1,2,3,4,5,"hi"}
##c=a.copy()
##print(c)
##a={1,2,3,4,5,"hi"}
##b=a
##b.clear()
##print(b)

##4. UNION       [makes as single set]
##%. UPDATE :    [updates a set with the other set]

##a={5,7,8,9,12,10}
##b={9,64,13,5,6,7,1}
##c=a.union(b)
##print(c)
##
##a={5,7,8,9,12,10}
##b={9,64,13,5,6,7,1}
##a.update(b)
##print(a)
##print(b)

##6. INTERSECTION          [common values printed]
##7. INTERSECTION_UPDATE : [updating the intersecting values to the other set too]

##a={5,7,8,9,12,10}
##b={9,4,3,5,6,7,1}
##c=a.intersection(b)
##print(c)
##a.intersection_update(b)
##print(a)

##8. DIFFERENCE           [checking difference of a wrt b]
##9. DIFFERENCE_UPDATE :  [updating the difference in the set]

##a={5,7,8,9,12,10}
##b={9,4,3,5,7,1}
##c=a.difference(b)
##print(c)
##a.difference_update(b)
##print(a)

##10. SYMMETRIC_DIFFERENCE           [uncommon values stored in c and printed]
##11. SYMMETRIC_DIFFERENCE_UPDATE :  [updates the above in the b set]

##a={5,7,8,9,12,10}
##b={9,4,3,5,7,1}
##c=a.symmetric_difference(b)
##print(c)
##a.symmetric_difference_update(b)
##print(a)


##12. isdisjoint(),13.issuperset(),14.issubset()

#isdisjoint(..it take false)it means !=[not equa]
##a={6,5,10,11,20}
##b={"hi","python"}
##c=a.isdisjoint(b)
##print(c)


#issuperset() [checking a with b,all balues below should in above set]
##a={1,2,3,4,5}
##b={2,3,4}
##print(a.issuperset(b)) #output=True 

#issubset()   [checking b with a,all values above should be below set]
##a={1,2,3,8}
##b={1,2,3,4,5}
##print(a.issubset(b)) #output=False


##16. remove,17. pop,15. discard :

##a={1,2,3,4,5}
##a.pop()
##print(a)
##a.remove(3) #error
##print(a)
##a.discard(20) 
##print(a)
##a.pop
##print(a)
##a={6,5,10,11,2}
##a.discard(11)
##print(a)
##a.remove(2)
##print(a)




































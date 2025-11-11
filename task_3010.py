##a=["apple","cherry","orange","kiwi","banana","green"]
##pp,rr,ee those alone shud be printed..adjacent same letters alone should be printed

def words():
    a=["apple","cherry","orange","kiwi","banana","green"]
    for i in a:
        print(i[4])
        for j in range(len(i)-1):
            if i[j] == i[j + 1]:
                print(i[j]*2)
##
words()

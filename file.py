##file handling:
##    creating, retrieveing and updating the data into the file using the code file=open("sample.txt")
##    if you open the file, properly close the file
##    file.close()

##syntax:
##    file = open("sample.txt","accessmode")
##    file.close()

##Accessmdode:
##    "x"-create the file
##    "r"-read the file
##    "w"-write the file
##    "a"-append the file

##create file:
    
##file= open("sample.txt","x")
##file.close()

##read file:

##file= open("sample.txt","r")
##print(file.read())

##write file:

##file= open("sample.txt","w")
##for i in range(10):
##    file.write("Hello World\n")
##file.close()


##append file:

##file= open("sample.txt","a")
##file.write("\nHello World")
##file.close()

##file= open("sample.txt","w")
##file.write("Hello world")
##file.close()

##file = open("sample.txt","a")
##b="Hello"
##for i in range(10):
##    file.write(f"{b}\n")
##file.close()

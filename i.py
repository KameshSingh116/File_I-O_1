#Radhe Radhe
#This is a complete guide code for the files input and output operations in python.

f=open("1.txt")
data=f.read()
print(data)
f.close()

#We can also use a different way of performing the same operation without using the close() function.
#Instead we can use the "with" statement 
#The with statement ensures that the file is closed
#as soon as the block is exited and even if an error occurs its closes the filr

with open("1.txt") as f:
    data=f.read()
    print(data)

#We have different modes in theopen function which can be provided withhin the open function
#By default the mode is set to "r" i.e read.

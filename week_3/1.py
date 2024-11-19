# Question1.
"""a=input("Enter your name :")
if(a):
    print("Hello World ")
    """
    
#Qustion 2.
"""
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

print("the product is:",num1*num2)
"""

#Question 3.

"""
num1=int(input("Enter a particular number"))
print("the number before is {} the number after is {} ".format (num1-1,num1+1))

"""

#Question 4
"""
print("The Quick Brown Fox jumps over the Lazy Dog".center(100))
print("and".center(100))
print("Pack my box with Five Dozen Liquor Jug".center(100))
"""

#Question5 
# This program should read first name and last name  
# of the user and display the name that user has entered. 
 
"""
fName = input("Enter your first name: ") 
print("\nThanks") 
lName = input("Enter your last name: ") 
 
print("\n" + fName + " " + lName) 
 
print(fName, lName) 
"""
#Question 6
"""print('F','U',sep='',end='')    #Here default '\n' is suppressed 
print('N') 

print('17','03','2005',sep='-',end="@")
"""

#Question 7
"""print("Two digit value : %2d, Float value : %5.2f" % (1, 354.1732))
print("Total Students: %3d, Boys,%2d"%(240,120))
print("Octal oof %2d is %7.3o"%(34,34))
print("The value of gravitational constant is =%10.3E"%(6.6743e-11))"""

#Question 8
"""print("I love {} for {}! {} {}".format('Python', 'Programming', 'for', 'Data Analytics')) 
  
# Using format() method and referring a position of the object 
print('{0} and {1}'.format('Sumit', 'Kumar')) 
#indexing specifies the order of the strings to be placed in those curly braces
print('{1} and {0}'.format('Sumit', 'Kumar'))"""


#Question 9
"""fName = input("Enter your first name: ") 
lName = input("Enter your last name: ") 
 
print("\n" + fName + " " + lName) 
"""
#Question 10
"""name = input("Enter your first name: ")
print(len(name))"""

#Question 11
"""list=[]
for i in range(3):
    name=input("Enter the %d letter "%(i))
    list.append(name)

print(list)"""

#Question12
"""str=""
for i in range(4):
    name=input("Enter the %d letter "%(i))
    str+=name+" "

print(str)"""


#Question 13
"""str=input("Enter the string her:")
i=int(input("Enter the ith index"))
new_str=str[0:i:]+str[i+1:len(str):]
print(new_str)"""


#Question 14
"""list=[]
for i in range(3):
    name=input("Enter the %d letter "%(i))
    marks=int(input("Enter the marks"))
    dept=input("enter the department")
    list.append((name,marks,dept))
print(list)"""

#Question 15
"""list1 = [1, 2, 3] 
list2 = [5, 7,6] 
list3 = [10, 11, 12]

set1=set(list2) 
#also sorts the array
set2=set(list1)
set1.update(set2)
print(set1)

set1.update(list3)
print(set1)"""

#Question16
"""list1 = [1, 2, 3, 4] 
list2 = [1, 4, 2, 3, 5] 

set1=set(list1)
set2=set(list2)

print(set1.union(set2))
print(set1.intersection(set2))
print(set2.difference(set1))"""

#Question 17
"""Set1 = {1, 2, 3, 4, 5}
myDict = {6: 'Six', 7: 'Seven', 5: 'Eight', 9: 'Nine', 10: 'Ten'}
Set1.update(myDict)
print(Set1)"""

#Question 18
"""dict={}
print("Enmpty dictionary",end="")
print(dict)

for i in range(3):
    fruit=input("Enter the name nof the fruit:")
    dict[i]=fruit

print("Dictionary updated")
print(dict)

dict[3]='Orange','Papaya','WaterMelon'
print(dict)

dict[2]='Peach','Litchi'
print(dict)"""

#Question 19
a=int(input("Enter the fist number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))
listm=[a,b,c]
list.extend(listm)
list.sort()
print(list[2])
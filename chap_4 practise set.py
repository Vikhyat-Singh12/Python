#1. Write a programme to store seven Fruits in a list entered by the user?

a1 = input("Enter the name of first Fruit :")
a2 = input("Enter the name of second Fruit :")
a3 = input("Enter the name of third Fruit :")
a4 = input("Enter the name of fourth Fruit :")
a5 = input("Enter the name of fifth Fruit :")
a6 = input("Enter the name of sixth Fruit :")
a7 = input("Enter the name of seventh Fruit :")

b = [a1 ,a2 ,a3 ,a4 ,a5 ,a6, a7]
print("Your Fruits list is", b)


#2. Write a programme to accept marks of 6 students and display them in sorted manner?

a1 = int(input("Enter the number of first student : "))
a2 = int(input("Enter the number of second student : "))
a3 = int(input("Enter the number of third student : "))
a4 = int(input("Enter the number of fourth student : "))
a5 = int(input("Enter the number of fifth student : "))
a6 = int(input("Enter the number of sixth student : "))

b = [a1 ,a2 ,a3 ,a4 ,a5 ,a6]
print(b)
b.sort()
print(b)


#3. Check that a Tuple cannot be changed in python?

'''t = (12,4,53,76,54,97,43,2)
print(t[3])
t[3] = 41          #changing the value of index 3  to 41.
print(t)'''


#4. Write a programme to sum a list with 4 numbers?

a1 = int(input("Enter the 1 number :"))
a2 = int(input("Enter the 2 number :"))
a3 = int(input("Enter the 3 number :"))
a4 = int(input("Enter the 4 number :"))

b = [a1 ,a2 ,a3 ,a4 ]
print("Your list is",b)
c = a1+a2+a3+a4
print("sum of the list is :",c)


#Write a programme to count the number of Zeroes in the following Tuple?

a = (7,0,8,0,0,9)
print(a)
a1 = a.count(0)
print(a1)








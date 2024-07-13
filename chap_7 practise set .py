'''#1. Write a program to print the table of given no. entered by the user using For loop ?

n = int (input("Which number Table Do You Want? :  "))

for i in range (1,11):
    j = n*i
    print(j)
     
print("Table of " + str(n) + " printed successfully.")       
 

#2. Write a program to greet all the persons name stored in a list l1 and which  starts with S?

l1 = ["Vishu","Sunita","Sohan", "Sachin","Rahul"]

for name in l1 :
    if name.startswith("S"):
        print("Hello ," + name)  


#3. Attempt problem one using while loop ?

n = int (input("Which number Table Do You Want? :  "))

i=1
while i<=10:
    j = n*i
    print(j)
    i=i+1
print("Table of " + str(n) + " printed successfully.")


#4. Write a program to find whether a given number is prime or not ?

n = int (input("Enter a number to check it is prime or not :  "))
prime = True

for i in range(2,n):
    if (n%i == 0):
        prime = False
        break

if prime:
    print(str(n) + " is a Prime Number.")
else:
    print(str(n) + " is  not a Prime Number.")
    

#5. Write a progam to find the sum of n natural numbers using while loop?

n = int (input("Enter a number  :  "))
i = 0
c = 0
while i<=n:
     c += i 
     i=i+1
print(c)


#6. Write a program to calculate the Factorial of a number given by the user  using for loop?

n = int (input("Enter a number to find Factorial  :  "))

factorial = 1
for i in range (1,n+1):
    factorial = factorial * i
print("The Factorial of " + str(n) + " is :", factorial)


#7. Write a program to print the following star pattern?

n = int (input("Enter a number :  "))

for i in range (n):
      print(" " * (n-i-1),end="")
      print("*" * (2*i+1),end="")
      print(" " * (n-i-1))                                    # Very Tricky Question.
    

#8. Write a program to print the following star pattern?

n = int (input("Enter a number :  "))

for i in range (n+1):
    print("*"*(i))'''
    

#9. Write a program to print the following star pattern?

for  i in range (20):
    print(i)





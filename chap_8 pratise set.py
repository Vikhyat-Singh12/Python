#1. Write a program function to find greatest of the three number?


a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))

def greatest(x,y,z):
    if x >y:
       f=x
    else:
        f=y
    if f >z:
        g=f
    else:
        g=z
    return g

t = greatest(a,b,c)
print("Greatest of three number  is "+ str(t))                           # First Type 
print("Greatest of three number  is "+ str(greatest(a,b,c)))             # Second Type


#2. Write a python program using function to convert celsious to fahrenheit?

def C_to_F(x):
    fahrenheit =  (9*x)/5 + 32
    return fahrenheit

a = int(input("Enter the Temperature in Celsious to convert it in Fahrenheit : \n"))

f = C_to_F(a)
print("Temperature in Fahrenheit is  " + str(f))


#3. How do you prevent a python print() function to print a new line at the end?

print("Hello,",end=" ")
print("How",end=" ")
print("are",end=" ")                               # We Can Prevent This By using (end="")at the last .
print("you?")


#4. Write a Recursive function to caculate the sum of first n natural numbers.

def sum_recursive(s):
    if  s==0:
        return s
    return s + sum_recursive (s-1)
  

n = int(input("Enter a number : "))
x = sum_recursive(n)
print("Sum of first " ,n," natural number is "+ str(x))


#5. Write a python  function  to print first n lines of the following pattern ?

def pattern (x):
    for i in range (x,0,-1):                            
        print("*"*i)                                                  

a = int(input("Enter a number  to print the structure : "))
pattern(a)


#6. Write a pyton function which converts inches  to cms?

def I_to_C (x):
    q = 2.54*x
    return q

a = int(input("Enter a number  to convert it from inches to cms : "))
c = I_to_C(a)
print(c)

    
#7. Write a python function to remove a given word from a list and a strip at the same time?

l = ["23","56","32","97","Vishu","Aditri","Avani","Ladoo"]
print(l)

def remove(x):
    a = l.remove(x)
    return a 

r = input("Enter a word from the given list to remove it : ")
remove(r)
print(l)

r = input("Enter a word from the left list to remove it : ")
remove(r)
print(l)


#8. Write a python function to print table of a given number entered by the user?

def table(x):
    for i in range (1,11):
        a = x*i
        print(a)    

y = int(input("Enter a number to print table : "))
table(y)
print ("Table printed Successfully")








    

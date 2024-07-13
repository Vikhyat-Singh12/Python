                                  # FUNCTION  &  RECURSIONS



# Function  without returning:

# Ex 1.:
def greet():                             # Here ,  [def means (definition)]  after that assigned the name of function [ex = here {greet()} is a function name]
    print("Hello")
    print("Good Morning")

greet()                                  # And when we have to call the function simply use name of the function [Ex = greet()]
                                         # we can call the function infinite number of Times.
    

# Ex 2.:
def sum(x,y):                            # Here function name is sum()
    c = x+y
    print(c)

sum(4,5)                                 # Here sum() function is called.


# Function  return  with one Value:

def sum(x,y):                            # Here function name is sum()
    c = x+y
    return c                             # return help us to stor value and can be used later .

s = sum(4,5)                             # Here sum() function is called.
print(s)


# Function return with many values :

def DMAS(x,y):                            # Here function name is DAMS()
    c = x+y
    d = x-y
    e = x*y
    f = x/y
    return c,d,e,f

r,s,t,u = DMAS(5,4)                        # Here DAMS() function is called.
print(r)                               
print(s)                                                     
print(t)                                                           
print(u)                                                  
 


# Quick Quiz :  Write a program to greet a user with "Good Day " using Function?

n = input("Enter Your Name Please : ")
def greet(name):
    print("Good Day, "+ name )

greet(n)


# Default Arguments :

n = input("Enter Your Name Please : ")
def greet(name="Stranger"):                         # Here, Stranger is a defalt name.
    print("Good Day, "+ name )

greet(n)                                               # Here, It will print the name that you will give through n.
greet()                                                # Here, it will print the Default name.



# Recurtion :

n! = 1 * 2 * 3 * 4...*n
n! = [1 * 2 * 3 * 4... n-1] *n
n! = n * (n-1)! 


# Factorial  through loops:

n =int(input("Enter a number :"))
product = 1
for i in range(n):
     product = product * (i+1)
print(product)


# Factorial  through functions: 

n =int(input("Enter a number :"))
def factorial (n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

f = factorial(n)
print(f)

 
#  Factorial  through recursion:

n =int(input("Enter a number :")) 
def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)

f = factorial_recursive(n)
print(f)




 

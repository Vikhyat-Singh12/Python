                             #  PROJECT  CALCULATER



print ("\t\t\t Welcome To Calculator World")
print("\t\t\t\t\t\t\t - By Vikhyat Singh \n\n")
def addition(x,y):
    return(x+y)

def subtraction(x,y):
    return(x-y)

def multiplication(x,y):
    return(x*y)

def division(x,y):
    return(x/y)



a = int(input("Enter the First  number : "))
b = int(input("Enter the Second number : "))
print("")

n  = input("Press for (+) Addition , (-)Subtraction ,(*)Multiplcation , (/)Division : ")
print("")

if n == "+":
    print("Your answer is : ",addition(a,b))

elif n == "-":
    print("Your answer is : ",subtraction(a,b))

elif n == "*":
    print("Your answer is : ",multiplication(a,b))

elif n == "/": 
     print("Your answer is : ",division(a,b))
    
else:
    print("YOu Choose Wrong Key. PLease Try Again! ")
    
print("")
print("")
print ("\t\t\t\t\t\tThanks for Using!")

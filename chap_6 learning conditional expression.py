                              #  CONDITIONAL  EXPRESSION



#  It is called if, else, elif Ladder:

a = int(input("Enter a positive  number only  : "))

if (a<3):                                                        #  (:) must be used after conditional statement otherwise it will throws an error.
    print("The value of a is less than 3") 
elif (a<13):                                                     #  (:) must be used after conditional statement otherwise it will throws an error.
    print("The value of a is less than 13")
elif (a<25):                                                     #  (:) must be used after conditional statement otherwise it will throws an error.
    print("The value of a is less than 25")
elif (a<38):                                                     #  (:) must be used after conditional statement otherwise it will throws an error.
    print("The value of a is less than 38")     
elif (a<45):                                                     #  (:) must be used after conditional statement otherwise it will throws an error.
    print("The value of a is less than 45")
else :                                                           #  (:) must be used after conditional statement otherwise it will throws an error.
    print("The value of a is greater than 3  and  45 both")



'''#  Multiple if Statement:

a = int(input("Enter a positive  number only  : "))

if (a<3):                                                      #  It is Independent Of Others
    print("The value of a is less than 3")
    
if (a<13):                                                     #  It is Independent Of Others 
    print("The value of a is less than 13")
    
if (a<25):                                                     #  It is Independent Of Others
    print("The value of a is less than 25")
    
if (a<38):                                                     #  It is Independent Of Others
    print("The value of a is less than 38") 
elif (a<45):                                                   #  But it is dependent of upper if
    print("The value of a is less than 45")
else :                                                         #  And it also is dependent of upper if
    print("The value of a is greater than 3  and  45 both")'''


    
# Quick Quiz:  Write a program to print yes when The age entered by the user is greater than 18?


Age  =  int(input("Enter Your Age plese : "))
if (Age>=18):                                                #  (>= --> greter than or  equal to)
    print("Yes,You can proceed")
else :
    print ("No, You can't  proceed")



#   Logical  And  Relational Operater:


age = int(input("Enter your age please : "))  

if(age>34 and age<56):                                       #  (And) means both the condition should be true for True the  statement otherwise  False.
    print("You can work with us")

else :
    print ("You can't work with us")



age = int(input("Enter your age please : "))  

if(age>34 or age==34):                                       #  (Or) means any one or both of  the condition should be true for True the  statement otherwise  False.
    print("You can work with us")

else :
    print ("You can't work with us")


# in or is:

a = None

if(a is None):                                              # { is = (==)} check  the value of  a:
    print ("Yes")
else:
    print("No")


a = [45,56,6,67]       
print(45 in a)                                              # (in) find the value in your List and return True if present.
print(435 in a)                                             # (in) find the value in your List and return False if not  present.


# IMPORTANT  NOTES:

'''1. There can be any number of elif statement .
   2. Last else  is executed only if all the condition  inside elifs fail.
   3. else is optional  but we use it because if all the conditions are false then else is executed otherwise no any output comes.'''


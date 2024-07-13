#1. Write a program to find greatest of four numbers entered by the user?

a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
c = int(input("Enter the number : "))
d = int(input("Enter the number : "))

if (a>b and a>c and a>d):
    print("Greatest of the four number is : ",a)
elif(b>a and b>c and b>d):
    print("Greatest of the four number is : ",b)
elif(c>a and c>b and c>d):
    print("Greatest of the four number is : ",c)
else:
    print("Greatest of the four number is : ",d)

# Alternative of this solution is :

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")


#2. Write a program to find out   whether a student is pass or fail,if it required total 40% and atleast 33% in each subject to pass . Assume 3 subjects and take marks as an input from the user?

a = int(input("Enter the Marks of First Subject : "))
b = int(input("Enter the Marks of Second Subject : "))
c = int(input("Enter the Marks of Third Subject : "))

if (a<33 or b<33 or c<33):
    print ("You are Fail  because you have less than 33% in one of the subject  ")
elif ((a+b+c)/3 < 40) :
    print("You  are fail due to total percentage less than 40")
else :
    print("Congratulation! , You are Successfully Passed in this Exam")


#3. A Spam Comment is defined as a text contaning following keywords:  "Make a lot of money","Buy Now","Subscribe This","Click This ".Write a program  to detect these Spams ?

 
text = input ("Enter the Text : ")

if ("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("click this" in text):
    spam = True
else:
    spam = False

if (spam):
    print("This text is a spam")
else:
     print("This text is not a spam")



#4. Write a program to find whether a given username contains less thsn 10 characters or not?

a = input("Enter Your name : ")
b = len(a)

if (b<10):
    print("Your name has less than 10 characters")
else:
    print("Your name has more than 10 characters")


#5. Write a program which Find out whether a given name is present in a list or not?


L = ["vikhyat" , "vishu" , "vinod" , "sunita", "aditry", "ladoo", "lucky ", "anshika"]

a = input("Enter your Name  to check in List : ")
if( a in L):
    print(a + "  is present in the List.")
else:
     print(a +  "  is not present in the List.")



#6. Write a program to calculate the grade of a student?

a = int(input ("Enter your Marks please : "))

if (90<=a<100):                                                # () is not Compulsory.
    a = " Excelent"
elif (80<=a<90):
   a = " A"
elif (70<=a<80):
   a =  " B"
elif (60<=a<70):
    a = " C"
elif (50<=a<60):
    a = " D"
else: 
    a = " F"  

print("Your grade is" + a ) 


#7. Write a program to find out whether a given Post is talking about "Harry" or "not"?


text = input ("Enter the Text : ")

if ("HARRY" in text):
    spam = True
elif("Harry" in text):
    spam = True
elif("HarrY" in text):
    spam = True
elif("HArry" in text):
    spam = True
elif("HARry" in text):
    spam = True
elif("HARRy" in text):
    spam = True
else:
    spam = False

if (spam):
    print("This text is Talking about Harry")
else:
     print("This text is not Talking about Harry")


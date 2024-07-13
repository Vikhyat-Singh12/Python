                             # LOOPS IN PYTHON


#1. While Loop
                             
i = 0
while i<10:
    print("Yes"+ str(i))
    i=i+1

print("Done")
                            
#Quick Quiz 1. : Write a program to print 1 to 50 using While Loop?

i = 1
while i<=50:
    print(str(i) + "  Done")
    i = i+1


# Qes.1 : Print "Vishu singh" for five times using (While Loop)?

i = 0
while i<5:
    print("Vishu Singh")
    i=i+1

### Note --> Tf the condition never becomes false , the loop keeps get executed for Infinite times.    

#Quick Quiz 2. : Write a programme to print the content of a list using (while loop)


fruits = ["Banana","Apple","Mango","Lichi","Pine Apple","Watermelon","Grapes"]

i=0
while i<len(fruits):
    print(fruits[i])
    i = i+1


#2. For Loop:


l = [1,7,8]
for items in l:
    print(items)
    
#Quick Quiz 2. : Write a programme to print the content of a list using (For loop):


fruits = ["Banana","Apple","Mango","Lichi","Pine Apple","Watermelon","Grapes"]

for items in fruits:
    print(items)


# Range Function in Python:


for i in range (8):                              # By defalt  range starts from (0,n-1). [Ex. Here loop starts from 0 to 7]
    print(i)

for i in range (1,10):                           # [Ex. Here loop starts from 1 to 9 ]
    print(i)

for i in range (1,10,3):                         # [Ex. Here loop starts from 1 to 10 with skip value 3]
    print(i)


                            #### range (Start, Stop, Skip Size)


# for loop with else:

for i in range (10):
    print(i)
else :
    print("This is inside else of for")
    
    
# Break Statement:

for i in range (10):
    if i==6:
        break
    print(i)
else :                                             # else statement print only when For Loop end successfully 
    print("This is inside else of for")


#  Continue  Statement :


for i in range (10):
    if i==5:
        continue
    print(i)
else :                                             # else statement print only when For Loop end successfully 
    print("This is inside else of for")


# Qus 2. Print all the even number from 0 to 100 ?
    
for i in range (101):
    if i%2==0:
        print(i)
print("Done")



# Pass Statement:

i=4
if i>0:
   pass                                           # (pass) tell the system to leave it(do nothing with this) without pass it will throw an error.

print("Vikhyat is a good coder.")















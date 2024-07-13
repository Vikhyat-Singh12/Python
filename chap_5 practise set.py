#1. Write A program to create the dictionary?

mydict = {
    "Pankha" : "Fan",
    "Dabba": "Box",
    "Vastu" : "Item",
    "Kitab": "Book"
}

print("Your options are :",list(mydict.keys()))
a = input ("Enter a Word :")
print("Meaning of the word is : ",mydict.get(a))

#2. Write a program to input eight no.  from the user and display all  the unique no. (once)?

a1 = int(input("Enter the 1 no. : "))
a2 = int(input("Enter the 2 no. : "))
a3 = int(input("Enter the 3 no. : "))
a4 = int(input("Enter the 4 no. : "))
a5 = int(input("Enter the 5 no. : "))
a6 = int(input("Enter the 6 no. : "))
a7 = int(input("Enter the 7 no. : "))
a8 = int(input("Enter the 8 no. : "))

a = [a1,a2,a3,a4,a5,a6,a7,a8]
print("Your numbers  are :",list(a))
a = {a1,a2,a3,a4,a5,a6,a7,a8}
print("Unique numbers are : ",a)

#3. Can  we have  a set with 18 (int) and "18"(str) as a value in it ?

a = {18,"18"}
print(a)                  # Yes,we can store (str) & (int) in the set.


#4. What will be the length of the following set S after operations ?

s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
print(s)

#5. s = {}.What is the type of s?

s = {}
print(type(s))


#6. Create an empty Dictionary. Allow 4 Friends to enter their favorite language  as value and use key as their name . Assume that the names are uniqe?


a = input("Vikhyat enter your favorite language :")
b = input("Sachin enter your favorite language :")
c = input("Jayendra enter your favorite language:")
d = input("Vikash enter your favorite language :")

D = {
     "Vikhyat": a,
     "Sachin": b,
     "Jayendra":c,
     "Vikash":d
}
print(list(D.items()))


#7. What if the name of two Friends are same .What will happen to the programme of problem 6?


a = input("Vikhyat enter your favorite language :")
b = input("Sachin enter your favorite language :")
c = input("Jayendra enter your favorite language:")
d = input("Vikash enter your favorite language :")

D = {
     "Vikhyat": a,
     "Sachin": b,
     "Jayendra":c,
     "Sachin":d
}
print(list(D.items()))               # It will print the latest value assigned to this name.


#8. What if the language of two Friends are same . What will happen to the programme of problem 6?

a = input("Enter your favorite language Vikhyat :")
b = input("Enter your favorite language Sachin :")
c = input("Enter your favorite language Jayendra:")
d = input("Enter your favorite language Vikash :")

D = {
     "Vikhyat": a,
     "Sachin": b,
     "Jayendra":c,
     "Vikash":d
}
print(list(D.items()))              # No problem occures .


#9. Can we chane the value inside a list which is contained in set S?

'''S = {8,7,12,"Harry",[1,2]}   # Since, List is not allowed in set so it will throw an error.
                             # Hence, we can't hane the value inside a list which is contained in set S.'''










                         ##  STRINGS  ##

name="Vishu"
greeting="Good Morning ,"
print(greeting + name)    #It add both the strings



# String slicing


name="Vishu"
                   
print(name[4])     #name[4]="d"    --> Change does not work
print(name[1:4])   #4 should not be taken  because it is excluded 
print(name[:3])    #is same as [0:3]  or [-5:-2]
print(name[1:])    # is same as [1:4]  or [-4:-1]
print(name.replace("Vishu","Vikhyat"))

#                       0   1   2   3   4
#                       V   i   s   h   u               this  is how values are assigned
#                      -5  -4  -3  -2  -1




#  Slicing  with skip value

name="VishuIsGood"
d = name[1:9:2]                  # here 2 is skipping values 
e = name[0:10:3]                 # here 3 is skipping values
print (d)
print (e)


#  String Functions


story = "Once upon a time Vikhyat Singh is a good person. Hello"

 
#Strings functions

print(len(story))                        # len = length of the strings.
print(story.endswith("person"))          # endswith means  it checks last letter and return with True if correct  and return False if incorrect.
print(story.startswith("Once"))          # startswith means it checks starting letter and return with True if correct  and return False if incorrect.
print(story.count("o"))                  # Count helps to count the total no. of occurence of any character or word etc.
print(story.capitalize())                # Capitalise  helps to capital the first letter .
print(story.find("Vikhyat"))             # Finds the positions of the letters or words etc and -1 means no word found in the entire strings.
print(story.replace("Vikhyat", "Vishu")) # It helps to replace the word or letters etc. in the entire string.
print(story.upper())                     # It helps to upper case all the  words of the entire string.
print(story.lower())                     # It helps to lower case all the  words of the entire string.


#  Escape Sequence Characters (\n(for new line) ,\t(for new tab) ,\'(for single quotes) ,\\(for baclslash))

story = 'Vikhyat\'s \t Singh \nis A Very Good  Boy'
print(story)


# f strings :

greeting = "Hello"
name = "Vikhyat"


message = f"{greeting}, {name}. Welcome!"         # f""  can be used like that.

print(message)
print(greeting +", " +name + ". Welcome")         # this can also be used but take lots of time.



                                   # This is How f''strings works.
a="He"
b="is a"
c="good"
d= "boy"

print(f'{a},  {b}, {c}, {d}!?')                

a="Vishu"
print(a.lower())
print("Vishu".lower())






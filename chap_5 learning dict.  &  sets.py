                              #  DICTIONARY  AND  SETS
                    
                              # Dictionaries

#Creating a Dictionary Using A = {}

mydict = {
    "Fast": "A Quick Learner",
    "Vishu":"A Coder",                    # For learning ; {"Keys":"Values"}
    "Marks":[12,23,34],
    "anotherdict":{'Vishu':'Player'}
}


# print dictionary using it.
print(mydict["Fast"])
print(mydict["Marks"])
print(mydict["anotherdict"]["Vishu"])

print()
print()

# It is mutable , So values can be replaced by  using this and print to get new values.
mydict["Marks"] = [45,78]
mydict["anotherdict"]['Vishu'] = 'Khiladi'
print(mydict["Marks"])
print(mydict["anotherdict"]["Vishu"])

print()
print()


#  Dictionary  Methods


mydict = {
    "fast": "A Quick Learner",
    "vishu":"A Coder",                    # For learning ; {"Keys":"Values"}
    "marks":[12,23,34],                   
    "anotherdict":{'vishu':'Player'},
    1:2
}

print(mydict.keys())                                # For printing the keys of the Dictionary.
print()
print(type(mydict.keys))                            # Type of keys
print()
print(list(mydict.keys()))                          # Converting  its type to list.
print()


print(mydict.values())                              # For printing the values of the dictinary.
print()
print(type(mydict.values))                          # Type of values
print()
print(list(mydict.values()))                        # Converting  its type to list.
print()


print(mydict.items())                               # Prints the (Key , Value) for all contents of the dictionary. 
print()
print(type(mydict.items))                           # Type of items
print()
print(list(mydict.items()))                         # Converting  its type to list.
print()
print()
print()



# Updating the dictionary

print(mydict)
print()
UD = {
     "Lovish":"Friends",
     "Killer":"Don",
     "Vishu":"A Coder",    
     34 : 45
     
}
mydict.update(UD)                               # It is used  to update the dictionary By the Update Function.
print (mydict)  
print()                                
mydict["Killer"] = [56]                         # Assigning the new value  to Killer
print(mydict["Killer"])
print()
print(mydict)                                   # Printing the Dictionary.


print(mydict.get("vishu"))          # Since, vishu is present in the dictionary,
print(mydict["vishu"])              # so both show same answer .

# The difference between .get and [] syntax in the Dictionary?

print(mydict.get("vishu2"))         # Return None as vishu2 is not present in the dictionary.
#print(mydict["vishu2"])            # Throws an error as vishu2 is not present in the dictionary.


                                    # Sets

a = {1,2,4,5,6,2,1}                                          
print(type (a))
print(a)
print()
print()

# Empty set.
# IMPORTANT : This syntax will create an empty Dictionary not an empty set
a = {}
print(type(a))

#An empty set can be created using the below syntax:
b = set()
print(type(b))


# Functions in sets.
b.add(4)                              # .add help to add the no. in the set
b.add(5)
b.add(5)                              #  It will add 5 only one time.
b.add((4,5,6))                        #  It will add Tuple in the set. 
#b.add([4,5,6])                       #  But not add the List. It will throw an error.
#b.add ({4:5})                        #  But also not add the Dictionary. It will throw an error.
print(b)


# Length of the Set
print(len(b))                         #  Prints the length of the set.


#Removal of an items from the set 
b.remove(5)                           #  Removes 5 from the set b
print (b)

'''b.remove(15)                          #  Throws an error while trying  to remove 15 (which is not in the set) 
print (b)'''


b.pop()                               #  Removes any random values from the set.
print (b)


c = {1,2,3,5,3,32,4,6,76,43,2,1}      
c.clear()                             #  It help to clear all the element of the set.
print (c)










 

                            # LISTS  AND  TUPLES


# Create a list using []
a = [1  ,  2,  4,   56  , 6]

#print the list using print()function
print(a)

# Access by using index  a[0], a[1], a[2], .......
print(a[3])

# Change the value of list using a[0], a[1], a[2], .......
a[3] = 645
print(a)


#We can  create  list with items of different types

c = [45,"Vishu",True,8.4]
print(c)
c[2] = False
print(c)
print(type(c[2]))
print(len(c))


# List slicing

friends = ["Vishu","Parth","Roachak","Jayendra","Sachin"]
print(friends)
print(friends[0:5:3])


#  List methods

l1 = [1,8,4,9,7,64,21]
print(l1)
l1.sort()                 # It  sort the list from ascending order.
print(l1)
l1.reverse()              # It reversed  the list  from decending order.
print(l1)
l1.append(45)             # Adds 45 at the ends if the list
print(l1)
l1.insert(2,544)          # Inserts 544 at index 2.
print(l1)
l1.pop(2)                 # It remove the no. of the given index.[ex--> 2]
print(l1)
l1.remove(21)             # It remove the given no. from the list if present.[ex--> 21]
print(l1)
l1[-1]="Vishu"            # It change the value of the given index.
print(l1)
print(type(l1[-1]))       # It help to know the type of  of given index. 


 
#  Tuples  in Python



# Creating the tuple using ().
t  = (1,2,4,5,7)                        # Tuple With More Than One Element
t1 = ()                                 # Empty Tuple
'''#t2 = (1)                               # Wrong way to declare Tuple with Single Element'''
t2 = (1,)                               # Right Way to declare Tuple with Single Element               


#printing the element of tuples
print(t)
print(t1)
print(t2)


'''# We Cannot update the value of a tuple
t[1] = 3
print(t)'''


# Tuple Methods


t = (1,2,4,5,3,2,1,1,7,1,4,1,2,8,0,51,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
print(t.count(1))                           # Count the occurence of the no.
print(t.index(5))                           # Find the first index of the given character.































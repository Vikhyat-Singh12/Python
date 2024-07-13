                               #  FILE  I/O

'''
# Use open fuction to read the content of a file!

#f = open('sample.txt','r')                 # 'r'  is the read  mode.
f = open('sample.txt')                      # By Default mode is r.
#data = f.read ()                           # Read its Content
data = f.read (5)                           # [.read(5)]  It read first 5 character of the file.
print(data)                                 # Print its Content
f.close()                                   # Close the File



# By Read line  Function:

f = open('sample.txt')

# read first line
data = f.readline() 
print(data)

# Read second line
data = f.readline() 
print(data)

# Read third line
data = f.readline() 
print(data)

# Read fourth line... and so on...
data = f.readline() 
print(data)
f.close()


# Writing  Files  in python

f = open('sample.txt','w')                            # 'w'  is the write mode.
f.write("Please Write this to the file.")             # It will delete all all thigs in the file and write only this.
f.close()

# But when we want to add this in end of the  of the file we use (append(a)) mode

f = open('sample.txt','a')                            # 'a'  is the append  mode.
f.write(" I am Appending.")                           # It will add this to the end of the file.
f.close()


# Qus:
f = open('this.txt','w')
f.write('This is nice.\n')
f.write('This is nice.\n')
f.write('This is nice.\n')
f.write('This is nice.\n')
f.write('This is nice.\n')
f.close()
'''

# With Statement.


with open('this.txt', 'w') as f:
    a = f.write("me as ai . I want to concqure the world.\n  ")
print(a)
with open('this.txt', 'r') as f:
    a = f.read()
print(a)




























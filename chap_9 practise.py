# Q. Write a programe to write a poem.txt and find wheater it contain twinkle or not ?  

'''

with open("poem.txt","w" ) as  f:
    a= f.write("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.
""")
f.close()

a = open("poem.txt","r")
f = a.read()
print(f)
if "Twinkle" in f :
    print("Twinkle is present.")
else:
    print("Twinkle is not present")
a.close()

'''


# Q. The game() function in a programe lets a user play a game and return the scrore as an integer. 
# You need to read a file 'Hiscrore.txt' which is either blank or contain previous Hiscore.
# you need to write a programe to update the Hiscore when ever game() breaks Hiscore.

'''def game(x):
    return x


a = int(input("Enter the Score  : "))
score = game(a)

with open("hiscore.txt") as f:
    hiscoreStr = f.read()


if  hiscoreStr=="":
     with open("hiscore.txt","w") as f:
        f.write(str(score))
        print("Last Hiscore",hiscoreStr)
     with open("hiscore.txt") as f:
        a = f.read()
        print("New Hiscore is, ",a)

elif int(hiscoreStr)<score :
    with open("hiscore.txt","w") as f:
        f.write(str(score))
        print("Last Hiscore",hiscoreStr)
    with open("hiscore.txt") as f:
        a = f.read()
        print("New Hiscore is: ",a)
else:
    print("Last Hiscore",hiscoreStr)'''



# Q. Write a programe to generate multiplication tables from 2 to 20 and
# write it to the different files in a folder name table ?

'''for i in range (2,21):
    with open(f'table/table_of_{i}.txt','w') as f:
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}")
            if j != 10:
                f.write('\n')

'''


#Q. find the word from the file which are inappopriate and replace the with "#@**@#"?


'''words = ["donkey", "kaddu", "mote" , "bsdk"]
 

with open("gali.txt") as f:
    content = f.read()

for word in words :
    content = content.replace(word,"#@**@#")
     
    with open("gali.txt", "w") as f:
        f.write(content)'''


#Q. Write a programe to mine a log file and find whether it contains "python"?


'''with open("log.txt","r") as f:
    content = f.read()

if "python" in content:
    print("It contain python.")
    
else:
    print("pyhton not present.)'''


#Q. In Q.6 find the line where python iis present?


'''with open("log.txt","r") as f:
    content = f.read().lower()

if "python" in content:
    print("It contain python.")

else:
    print("pyhton not present.")'''


#Q. in the previous q. find the line in which python is present?

'''content = True
i = 1
with open("log.txt","r") as f:
    while content:
        content = f.readline()
        if "python" in content.lower():
            print(content)
            print(f"Yes! Python is present in line {i}")

        i+=1'''


#Q. Write a programme to make a copy of a text file "this.txt"?

'''with open("this.txt","r") as f:
    content = f.read()
    

with open("xyz.txt","w") as a:
    a.write(content)
    '''
    

#Q. Find out wheather two files are same or not?

'''file1 = "this.txt"
file2 = "xyz.txt"

with open(file1) as f:
    cont = f.read()

with open(file2) as a:
    cont1 = a.read()

if cont == cont1 :
    print("Files are same.")

else:
    print("Files not same.")'''


#Q. Write a prigramme to wipe out the content of a file using python?

'''n = input("Enter the word to write in the file:")
with open("new.txt","w") as f:
    f.write(n)
'''

#Q. Write a python programe to rename a file to "removed_by_python.txt"?

import os                               # This built in function is used to remove the existing file.

oldname = "old.txt"
newname = "removed_by_python.txt"

with open(oldname) as f:
    content = f.read()

with open(newname,"w") as f:
    f.write(content)

os.remove(oldname)              
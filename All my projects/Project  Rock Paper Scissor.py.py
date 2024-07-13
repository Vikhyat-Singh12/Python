                                   # Rock , Paper and Scissor



print("\t\t\t\t Welcome! to the Game.")
print("\t\t\t      ROCK , PAPER  AND  SCISSORS\n")


import random


def game(comp,you):
    
    if comp == you:
        return None
    
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
        
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False

    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False

        

randno=random.randint(1,3)
if randno == 1:
    comp = 'r'
elif randno == 2:
    comp = 'p'
elif randno == 3:
    comp = 's'
    
print("Comp turn : Comp has choosen.")
you = input("Your turn : Rock(r) Paper(p) Scissor(s)? ")

print("Computer choose : ",comp)
print("You choose      : ",you)


a = game(comp,you)

if a==None:
    print("Game is Tie\n ")
elif a == True:
    print("Congratulation, You Win!\n")
else:
    print("You Lose.\n")


print("\t\t\t\t\t\t\t\t Thanks  For  Playing")
print("\t\t\t\t\t\t\t\t - By Vikhyat Singh")

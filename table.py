

def table(x):
    i = 1
    while i<11:
        a = x*i 
        print(f'{x} X {i} = {a}')
        i = i+1
       
while True:
    f = int(input("Enter 1 to OPERATE Enter 0 to EXIT :-"))

    if f == 1 :
        a = int(input("Enter the no for table :-"))
        table(a)
        print("Table Printed Sucessfully !!")
        
    elif f == 0 :
        print("Programe Terminated Sucessfully !!")

    else :
        print("You choose wrong  ")




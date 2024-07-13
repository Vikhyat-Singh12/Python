
print("\t\t\t\t Welcome to Fake Id Generator!\n\n")

n = int(input('How many fake id do you want to generate please enter : '))
print("")
print("")

import random

first_name = ["Rahul","Rohit","Vasi","Vaibhav","Aranav","Aditya","Anay","Anmol","Ansh","Devansh","Gopal","Garav","Harsh","Hardik","Pappu","Shubham","Sunil","Vishal","Vikram","Karan","Arjun","Shayam","Shivam","Aryan","Raj","Avinash","Sachin","Vikash","Ranveer","Samar","Veer"]
last_name = ["Singh","Tiwari","Yadav","Jaiswal","Agrahari","Pandey","Chakrawarti","Ruthra","Lundia","Dholakiya","Patel","Rajput","Rajvat"]
city_name = ["Varanasi","Prayagraj ","Bareilly","Aligarh","Gorakhpur","Noida","Firozabad","Muzaffarnagar","Mathura","Faizabad","Luchnow","Kanpur","Mirzapur","Agara","Rampur","Farrukhabad","Agra"]
special_character = ['!','#','$','%','^','&','*','?']

for i in range(n):
    name =  random.choice(first_name)
    title = random.choice(last_name)

    print(f'Name          : {name}  {title}')
    print(f'Father Name   : {random.choice(first_name)}  {title}')
    print(f'D.O.B         : {random.randint(1,31)}/{random.randint(1,12)}/{random.randint(1950,2021)}')
    print(f'Addhar Number : {random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}')
    print(f'Address       : {random.choice(city_name)}, Road- {random.randint(1,190)}, UTTER PRADESH')
    print(f'Phone Number  : {random.randint(6500000000,9999999999)}')
    print(f'Email Id      : {name.lower()}_{title.lower()}_{random.choice(special_character)}{random.randint(1,200)}@gmail.com')
    print(f'Pin Code      : {random.randint(100000,999999)}\n\n')

print ("Your "+str(n)+" Fake Id's Generated Successfully!")
print("Thanks for using!")
print("\t\t\t\t\t\tPresented By -  VIKHYAT  SINGH ")


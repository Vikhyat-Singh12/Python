#1. Write a programme for user name folowed by Good Afternoon?
 
G = "Good  Afternoon,  "
N = input("Enter your Name:")
print(G+N)


#2. WRITE A PROGRAMME TO FILL IN A LETTER TEMPLATE GIVEN BELOW WITH NAME AND DATE?


letter = '''Dear,  <|Name|>
       You are Selected!
Date = <|Date|>'''
name = input("Enter Your Name :")
date = input("Enter Date :")

letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)


#3.  Write a programme to detect Double spaces in a string?
               

st = "This is a string with  double  spaces"
DS=st.find("  ")
print(DS)


#4. Replace this double space with single space?


DSP=st.replace("  "," ")
print(DSP)


#5. Write a programme to formate the following letter using escape squence characers?

letter = "Dear Harry,\n\tThis Python Course is nice.\nThanks!"
print(letter)




                              # IMPORT RANDOM



#  Type of random:

import random                         # It is always used to use random function

value = random.random()               # [.random()] is used to print random value between 0 and 1 and , we never get 0 & 1.
print(value) 

 
value = random.uniform(1,20)          # [.uniform(x,y)] is used to get floating value between x & y and , we never get x & y.
print(value)


value = random.randint(1,20)          # [.randint(x,y)] is used to get integer value between x & y and , we can also get x & y.
print(value)


greetings = ['Hello','Hi','Hey']
value = random.choice(greetings)      # [.choice(list name)] is used to get a random value which is given in the list.
print(value + ", Vikhyat Singh")


deck = list(range(1,53))
random.shuffle(deck)                  # [.shuffle(list name)]  is used to shuffle the list.
print(deck)


deck = list(range(1,53))
hand = random.sample(deck , k=9)      # [.sample(list name , k=x)] is used to get a random value from a list.
print(hand)                           # Here , k=10(or x) to get 10 or x uniqe  value from the list.



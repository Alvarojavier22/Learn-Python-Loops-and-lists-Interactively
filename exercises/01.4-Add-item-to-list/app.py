#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:
for i in range(10):
    number = random.randint(1, 1000)

    my_list.append(number)

print(my_list)
from random import randint
num = randint(1, 1000) #picks random number from 1-1000
# NO TOUCHING ======================================
if num % 2 == 1:
    print("odd")
else:
    print("even")
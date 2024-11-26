#!/usr/bin/env python3

def happy_new_year():
   counter=10
   while counter > 0:
       print(counter)
       counter +=-1
   print("Happy New Year!")    
def square_integers(int_list):
    for i in int_list:
        print(i*i)

def fizzbuzz():
    nums = 1  
    while nums <= 100:  
        if nums % 3 == 0 and nums % 5 == 0:
            print("FizzBuzz")
        elif nums % 3 == 0:
            print("Fizz")
        elif nums % 5 == 0:
            print("Buzz")
        else:
            print(nums)
        nums += 1  

happy_new_year()
square_integers(int_list=[12,13,14,25])
fizzbuzz()

  
   

#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while (count >= 1):
        print (count)
        count -=1
        print ("Happy New Year!")
    
def square_integers(int_list):
    squared_numbers = [num ** 2 for num in int_list ]
    return squared_numbers

def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
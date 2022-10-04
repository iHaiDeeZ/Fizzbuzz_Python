"""
Author: ShiroKlein
Year: 2022
Purpose: It was created while relearning Python for IoT 
Program: Fizzbuzz
Description:
This script checks wether the integer given when divided by 3 or 5 will yield 0 remins which is the modular.
"""
def fizzbuzz(L): # Function that check that given number  is dividable by either 3 or 5
    m = L%5
    n =L%3
    if m == 0 and n == 0:
        print("{} is dividable by 3 and 5 and yield 0 reminder".format(L))
    elif m ==0 and n != 0: 
        print ("{} is Number is only dividable by 5 and yield 0 Reminder".format(L))
    elif n ==0 and m != 0:
        print("{} is Number is only dividable by 3 and yield 0 Reminder".format(L))
    else:
        print("{} is not dividable by either 3 or 5".format(L))   
    
       

while(1):
    
    x = input("Enter an integer Number: \n ")
    y = int(x)
    if  not(issubclass(type(y), (int))):
        print("Entered data is not integer ")
    else:
        fizzbuzz(y)

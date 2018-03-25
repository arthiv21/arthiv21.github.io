# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import time



def countdown(n):
    while n>0:
        print ('Your food will expire in {0} days'.format(n))
        n = n-1
        if n==0:
            print('Expired. You are killing the environment')

food = {}

while True:
    option = int(input("What would you like to do? [1] track your food expiration date or [2] insert a food option: "))
    if (option==1):
        for key in food:
            print(key)
        k = food[input("What food are you tracking: ").lower()]
        countdown(k)
    elif (option==2):
        for value in food:
            print(value)
        key = input("What food do you want to add?: ").lower() 
        value = int(input("In how many days will it expire?: "))
        food[key] = value
    else:
        break
    



    

# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 15:08:46 2019
Monty Hall Problem 
@author: Amol
"""
import random 

lose_if_change = 0 
win_if_change = 0

door = [1,0,0]
# 1 is a car and 0 is a goat 
num_of_sim = 100000
for i in range(num_of_sim):
    random.shuffle(door)# randomly assigning the car to a place 
    # choosing a door 
    user_choice = random.randrange(3)
    array = [i for i in range(3)]
    #^monty picks a door 
    random.shuffle(array)
    
    for i in array:
        if i == user_choice or door[i] == 1:
            continue 
    if door[user_choice] == 1:
        lose_if_change += 1
    else:
        win_if_change += 1

print("changing will make you win {} and lose {} out of {}".format(win_if_change,lose_if_change,num_of_sim))
print("win percentage {} loss percentage {}".format(win_if_change/num_of_sim,lose_if_change/num_of_sim))

        
        






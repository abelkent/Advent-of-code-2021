# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 12:21:30 2022

@author: abelw
"""

import time

def sol_a(filepath, countdown):
    
    with open(filepath) as file:
        raw_text = file.read()
        raw_text = raw_text.split(",")
        data = [int(x) for x in raw_text]
    
    for day in range(countdown):
        print(day)
        for index in range(len(data)):
            
            if data[index] == 0:
                data[index] = 6
                data.append(8)
            else:
                data[index] -= 1
    

with open("test.txt") as file:
    raw_text = file.read()
    raw_text = raw_text.split(",")
    data = [int(x) for x in raw_text]


def sol_b(data, time_limit):

    def recursive(item, time_limit, current):
        if time_limit == current:
            return 1
        elif item != 0:
            print(current)
            return recursive(item-1, time_limit, current + 1)
        elif item == 0:
            return recursive(6, time_limit, current + 1) + recursive(8, time_limit, current+1)    

    unique_counts = []

    total = 0
    
    for number in range(0,9):
        local_count = 0
        for item in data:
            if item == number:
                local_count += 1
            
        unique_counts.append(int(local_count))
    print(unique_counts)
            
    
    for index in range(len(unique_counts)):
        print(index)
        if unique_counts[index] > 0:
            local_total = recursive(index, time_limit, 0)
            total += (local_total * unique_counts[index])
        
    return total


    
test = sol_b(data, 256)
#experimental = sol_a("input.txt",80)

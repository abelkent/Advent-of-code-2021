# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:19:01 2022

@author: abelw
"""

def sol_a(filepath):

    with open(filepath) as file:
        data = file.read()
        data = data.split(",")
        data = [int(x) for x in data]
        print(data)
        
    max_value = max(data)
    distance_count = []
    
    for target in range(max_value+1):
        #print(target)
        
        distance_from_target = 0
        
        for value in data:    
            distance_from_target += abs(target - value)
        
        distance_count.append(distance_from_target)
            
    return min(distance_count)



def sol_b(filepath):
                

    with open(filepath) as file:
        data = file.read()
        data = data.split(",")
        data = [int(x) for x in data]
        print(data)
        
    max_value = max(data)
    distance_count = []
    
    for target in range(max_value+1):
        #print(target)
        
        distance_from_target = 0
        
        for value in data:    
            distance_from_target += triangular(abs(target - value))
        
        distance_count.append(distance_from_target)
            
    return min(distance_count)        


def triangular(index):
    
    return(sum(range(1,index+1)))

print(triangular(3))

test = sol_b("input.txt")

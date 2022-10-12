# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 19:52:06 2022

@author: abelw
"""

with open("Sonar input.txt") as sonar:
    sonar_inputs = sonar.readlines()
    

def sol_a(input_path):
    
    increase_count = 0
    
    with open(input_path) as sonar:
        sonar_inputs = sonar.readlines()
        
    for index in range(1, len(sonar_inputs)):
        previous = int(sonar_inputs[index-1])
        current = int(sonar_inputs[index])
        
        if current > previous:
            increase_count += 1
    
    return increase_count
    
#test_result = sol_a("test input.txt")
#experimental_result = sol_a("Sonar input.txt")


def sol_b(input_path):
    
    increase_count = 0
    
    with open(input_path) as sonar:
        sonar_inputs = sonar.readlines()
    
    sliding = []
    
    for index in range(1,len(sonar_inputs)-1):
        slide = int(sonar_inputs[index-1]) + int(sonar_inputs[index]) + int(sonar_inputs[index+1])
        sliding.append(slide)
        
    increase_count = 0
    
    for index in range(1, len(sliding)):
        previous = int(sliding[index-1])
        current = int(sliding[index])
        
        if current > previous:
            increase_count += 1
    
    return increase_count    
        
test_result = sol_b("test input.txt")
experimental_result = sol_b("Sonar input.txt")
        
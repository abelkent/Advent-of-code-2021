# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:10:35 2022

@author: abelw
"""

import re

def sol_a(filepath):
    
    horizontal = 0
    vertical = 0
    
    with open(filepath) as file:
        data = file.readlines()
    
    for line in data:
        print(line)
        
        direction, number = line.split(" ")
        number = int(number)
        
        if line[0] == "f":
            horizontal += number
        if line[0] == "d":
            vertical += number
        if line[0] == "u":
            vertical -= number
    
    return(horizontal * vertical)


def sol_b(filepath):
    
    horizontal = 0
    vertical = 0
    aim = 0
    
    with open(filepath) as file:
        data = file.readlines()
    
    for line in data:
        print(line)
        
        direction, number = line.split(" ")
        number = int(number)
        
        if line[0] == "f":
            horizontal += number
            vertical += (aim * number)
        if line[0] == "d":
            #vertical += number
            aim += number
        if line[0] == "u":
            #vertical -= number
            aim -= number
    
    return(horizontal * vertical)


# =============================================================================
# test_result = sol_a("test.txt")
# experimental_result = sol_a("input.txt")
# =============================================================================

test_result = sol_b("input.txt")
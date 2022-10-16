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
    

with open(filepath) as file:
    raw_text = file.read()
    raw_text = raw_text.split(",")
    data = [int(x) for x in raw_text]


def sol_b(data, countdown):
    
    if countdown == 0:
        return len(data)
    
    elif 0 in data:
        
        
    
    

            
        
        
                
            
    
            
            
        

        #time.sleep(0.5)
            
    return(len(data))
    
test = sol_b("test.txt",256)
#experimental = sol_a("input.txt",80)

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 16:19:48 2022

@author: abelw
"""


def sol_a(filepath):
    
    outputs = []
    
    with open(filepath) as file:
        data = file.readlines()
        for row in data:
            outputs.append(row.split("|")[1].split(" "))

    outputs_flat = []
    for row in outputs:
        for item in row:
            outputs_flat.append(len(item.strip("\n")))
    
    print(outputs_flat)
    
    unique_digits = 0
    for item in outputs_flat:
        if item in [2,3,4,7]:
            unique_digits += 1
    
    return(unique_digits)

def sol_b(filepath):
    
    total = 0
    
    with open(filepath) as file:
        data = file.readlines()
    
    
    for line in data:
        input_segment, output_segment = line.split("|")
        input_segment = input_segment.split(" ")
        output_segment = output_segment.split(" ")
        
        digit_0 = []
        digit_1 = []
        digit_2 = []
        digit_3 = []
        digit_4 = []
        digit_5 = []
        digit_6 = []
        digit_7 = []
        digit_8 = []
        digit_9 = []
        digits = [digit_0,
                  digit_1,
                  digit_2,
                  digit_3,
                  digit_4,
                  digit_5,
                  digit_6,
                  digit_7,
                  digit_8,
                  digit_9]
        
        for item in input_segment:
            if len(item) == 2:
                digit_1 = [x for x in item]
                digit_1.sort()
            elif len(item) == 4:
                digit_4 = [x for x in item]
                digit_4.sort()
            elif len(item) == 3:
                digit_7 = [x for x in item]
                digit_7.sort()
            elif len(item) == 7:
                digit_8 = [x for x in item]
                digit_8.sort()
        
        for letter in digit_8:
            print(letter)
            #a
            if (letter in digit_7) and (letter not in digit_1):
                digit_2.append(letter)
            #b
            
            #c
            
            #d
            
            #e
            
            #f
            
            #g
        
        return(digits)   
        


                    
                

    
                
            

test = sol_b("test.txt")
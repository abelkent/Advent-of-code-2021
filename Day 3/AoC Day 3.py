# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:21:26 2022

@author: abelw
"""

import re
#re.sub("[^0-9]", "",)

def diagnose_a(filepath):
    with open(filepath) as file:
        data = file.readlines()
    
    
    input_length = len(re.sub("[^0-9]", "", data[0]))
    max_value = (2**input_length)-1
    
    digits = str()
    
    for index in range(input_length):
        count_1 = 0
        count_0 = 0
        for element in data:
            if element[index] == "1":
                count_1 += 1
            else:
                count_0 += 1
        
        if count_1 > count_0:
            digits += "1"
        else:
            digits+= "0"
        
    gamma = int(digits, 2)
    epsilon = max_value - gamma
    
    return(gamma * epsilon)
            
# =============================================================================
# test = diagnose_a("test.txt")
# experiment = diagnose_a("input.txt")
# =============================================================================


def diagnose_b(filepath):
    
    oxygen_file = open(filepath, "r")
    oxygen_input = oxygen_file.readlines()
    #print(oxygen_input)
    
    carbon_file = open(filepath, "r")
    carbon_input = carbon_file.readlines()
    #print(carbon_input)
    

    
        
    input_length = len(re.sub("[^0-9]", "", oxygen_input[0]))
    
    #print(len(oxygen_input))
    #print(len(carbon_input))
    #print(carbon_input)
    

    
    #print("check")
    while len(oxygen_input) > 1:
        #print("check")
        for index in range(input_length):
            #print(oxygen_input)
            #print(len(oxygen_input))
            count_1 = 0
            count_0 = 0
            for element in oxygen_input:
                if element[index] == "1":
                    count_1 += 1
                else:
                    count_0 += 1
            
            #print("check")
            if (count_1 >= count_0):
                for element in oxygen_input:
                    if element[index] == "0":
                        
                        oxygen_input.remove(element)
            elif (count_0 > count_1):
                for element in oxygen_input:
                    if element[index] == "1":
                        oxygen_input.remove(element)
        print(oxygen_input)

       


    print(carbon_input)
    while len(carbon_input) > 1:
        #print("check")
        for index in range(input_length):
            #print(len(carbon_input))
            count_1 = 0
            count_0 = 0
            for element in carbon_input:
                if element[index] == "1":
                    count_1 += 1
                else:
                    count_0 += 1
            
            #print("Check")
            if (count_0 > count_1):
                for element in carbon_input:
                    if element[index] == "0":
                        #print(element, count_0, count_1)
                        carbon_input.remove(element)
            elif (count_0 <= count_1):
                for element in carbon_input:
                    if element[index] == "1":
                        #print(element, count_0, count_1)
                        carbon_input.remove(element)
                    
    return (oxygen_input, carbon_input)


def diagnose_c(filepath):
    with open(filepath) as file:
        data = file.readlines()
    
    oxygen_input = list(data)
    carbon_input = list(data)
    
    
    for index in range(len(data)):
        oxygen_input[index] = re.sub("[^0-9]", "", oxygen_input[index])
        carbon_input[index] = re.sub("[^0-9]", "", carbon_input[index])
    
    input_length = len(oxygen_input[0])
    print(input_length)
    
    while len(oxygen_input) > 1:
        
        for index in range(input_length):
            count_0 = 0
            count_1 = 0
            
            elements_0 = []
            elements_1 = []
            
            for element in oxygen_input:
                if element[index] == "0":
                    elements_0.append(element)
                else:
                    elements_1.append(element)
            
            if len(elements_1) >= len(elements_0):
                oxygen_input = list(elements_1)
            else:
                oxygen_input = list(elements_0)
            if len(oxygen_input) == 1:
                break
    
    
    while len(carbon_input) > 1:
        
        for index in range(input_length):
            count_0 = 0
            count_1 = 0
            
            elements_0 = []
            elements_1 = []
            
            for element in carbon_input:
                if element[index] == "0":
                    elements_0.append(element)
                else:
                    elements_1.append(element)
            
            if len(elements_0) <= len(elements_1):
                carbon_input = list(elements_0)
            else:
                carbon_input = list(elements_1)
            if len(carbon_input) == 1:
                break
        
    oxygen_value = int(oxygen_input[0],2)
    carbon_value = int(carbon_input[0],2)
    
    return(oxygen_value, carbon_value, oxygen_value * carbon_value)
       
    

                
            
            
            
        
        
    

test = diagnose_c("test.txt")
experiemntal = diagnose_c("input.txt")

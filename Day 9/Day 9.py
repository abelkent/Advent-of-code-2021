# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 21:28:03 2022

@author: abelw
"""

def sol_a(filepath):
    
    
    
    with open(filepath) as file:
        data = file.readlines()
        data = [element.strip("\n") for element in data]
    
    data_array = []
    local_array = []
    for row in data:
        for item in row:
            local_array.append(item)
        data_array.append(local_array)
        local_array = []
    
    
    total_risk = 0

    for row_idx in range(len(data_array)):
        for col_idx in range(len(data_array[row_idx])):
            
            neighbours = ["A","B","C","D"]
            
            item = (data_array[row_idx][col_idx])
            #print(item)
            
            if row_idx == 0:
                neighbours[0] = None
            else:
                neighbours[0] = (data_array[row_idx-1][col_idx])
            
            if row_idx == (len(data_array)-1):
                neighbours[1] = None
            else:
                neighbours[1] = (data_array[row_idx+1][col_idx])
            
            if col_idx == 0:
                neighbours[2] = None
            else:
                neighbours[2] = (data_array[row_idx][col_idx-1])
                
            if col_idx == (len(data_array[row_idx])-1):
                neighbours[3] = None
            else:
                neighbours[3] = (data_array[row_idx][col_idx+1])
            
            if None in neighbours:
                while None in neighbours:
                    neighbours.remove(None)
                    
            
            #print(neighbours)
            
            if all(item < neighbour for neighbour in neighbours):
                print("Low")
                total_risk += int(item)+1
    
    return(total_risk)
    
    
test = sol_a("test.txt")
experimental = sol_a("input.txt")
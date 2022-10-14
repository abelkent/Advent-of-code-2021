# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 13:38:51 2022

@author: abelw
"""

def sol_a(filepath):
    
    with open(filepath) as file:
        data = file.readlines()
    
    pairs = []
    
    num_rows = int()
    num_cols = int()
    
    #Data generation
    for line in data:
        line = line.split(" -> ")
        line[0] = line[0].split(",")
        line[1] = line[1].strip("\n").split(",")
        pairs.append(line)
     
    #Board creation
    x_dims = []
    y_dims = []
    
    for pair in pairs:
        x_dims.append(pair[0][0])
        x_dims.append(pair[1][0])
        
        y_dims.append(pair[0][1])
        y_dims.append(pair[1][1])
    
    row_size = int(max(x_dims))
    column_size = int(max(y_dims))
    
    board = []
    base_board = []
    blank_row = []
    for i in range(row_size):
        blank_row.append(0)
    
    for i in range(column_size):
        board.append(blank_row)
        base_board.append(blank_row)
    
    
    #Board population

    
    for pair in pairs:
        #Coordinate retrieval
        x_a = int(pair[0][0])
        x_b = int(pair[1][0])
        
        y_a = int(pair[0][1])
        y_b = int(pair[1][1])
        
        x_start, x_end, x_row = None, None, None
        y_start, y_end, y_col = None, None, None 
        
        #x_coordinates
        if x_a > x_b:
            x_start = x_b
            x_end = x_a
        elif x_a < x_b:
            x_start = x_a
            x_end = x_b
        elif x_a == x_b:
            x_row = x_a
        
        #y_coordinates
        if y_a > y_b:
            y_start = y_b
            y_end = y_a
        elif y_a < y_b:
            y_start = y_a
            y_end = y_b
        elif y_a == y_b:
            y_col = y_a
            
        
        #Plotting
        if y_col != None:
            for x_coord in range(x_start, x_end):
                board[y_col][x_coord] += 1
                print(board[y_col-1][x_coord])
        
        elif x_row != None:
            for point in range(y_start, y_end):
                board[point][x_row-1] = board[point][x_row-1] + 1
        
        break
        
        
        
    
    
        
        
    
    
    
    
    return(board)
    
    
test = sol_a("test.txt")
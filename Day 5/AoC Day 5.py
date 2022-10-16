# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 13:38:51 2022

@author: abelw
"""

def sol_a(filepath):
    
    with open(filepath) as file:
        data = file.readlines()
    
    tracks = []
    
    num_rows = int()
    num_cols = int()
    
    #Data generation
    for line in data:
        line = line.split(" -> ")
        line[0] = line[0].split(",")
        line[1] = line[1].strip("\n").split(",")
        tracks.append(line)
     
    #Board creation
    x_dims = []
    y_dims = []
    
    for pair in tracks:
        x_dims.append(int(pair[0][0]))
        x_dims.append(int(pair[1][0]))
        
        y_dims.append(int(pair[0][1]))
        y_dims.append(int(pair[1][1]))
    
    row_size = max(x_dims)+1
    number_of_rows = max(y_dims)+1
    
    board = []
    base_board = []
    blank_row = []

    print(number_of_rows)
    print(row_size)
    
    for i in range(number_of_rows):
        board.append([0]*row_size)
        
    
    
    for item in tracks:
        #print(item)
        
        horizontal, vertical = None, None
        
        start = item[0]
        end = item[1]
        
        x_start = int(start[0])
        x_end = int(end[0])
        
        y_start = int(start[1])
        y_end = int(end[1])
        
        if x_start == x_end:
            vertical = True
        elif x_start > x_end:
            x_end,x_start = x_start, x_end
            #print(x_start, x_end)
        
        if y_start == y_end:
            horizontal = True
            print(item)
        elif y_start > y_end:
            y_end, y_start = y_start, y_end
            #print(y_start, y_end)
        
        if horizontal == True:
            y_val = y_start
            for x_val in range(x_start, x_end+1):
                print(y_val, x_val)
                board[y_val][x_val] += 1
        
        elif vertical == True:
            x_val = x_start
            for y_val in range(y_start, y_end+1):
                print(y_val, x_val)
                board[y_val][x_val] += 1
        

    overlap = 0
    for row in board:
        for item in row:
            if item > 1:
                overlap += 1
    
    return(overlap,board)


def sol_b(filepath):
    with open(filepath) as file:
        data = file.readlines()
    
    tracks = []

    
    #Data generation
    for line in data:
        line = line.split(" -> ")
        line[0] = line[0].split(",")
        line[1] = line[1].strip("\n").split(",")
        tracks.append(line)
     
    #Board creation
    x_dims = []
    y_dims = []
    
    for pair in tracks:
        x_dims.append(int(pair[0][0]))
        x_dims.append(int(pair[1][0]))
        
        y_dims.append(int(pair[0][1]))
        y_dims.append(int(pair[1][1]))
    
    row_size = max(x_dims)+1
    number_of_rows = max(y_dims)+1     
    
    board = []
        
    for i in range(number_of_rows):
        board.append([0]*row_size)
    

    for item in tracks:
        #print(item)
        
        horizontal, vertical = None, None
        
        start = item[0]
        end = item[1]
        
        x_start = int(start[0])
        x_end = int(end[0])
        
        y_start = int(start[1])
        y_end = int(end[1])
        
        if x_start == x_end:
            vertical = True
        if y_start == y_end:
            horizontal = True
            #print(y_start, y_end)
            
        
        if horizontal == True:
            y_val = y_start
            if x_start > x_end:
                x_end,x_start = x_start, x_end
            for x_val in range(x_start, x_end+1):
                #print(y_val, x_val)
                board[y_val][x_val] += 1
        
        elif vertical == True:
            x_val = x_start
            if y_start > y_end:
                y_start, y_end = y_end, y_start
            for y_val in range(y_start, y_end+1):
                #print(y_val, x_val)
                board[y_val][x_val] += 1
        
        elif (vertical == None) and (horizontal == None):
            
            if x_start > x_end:
                x_step = -1
            else:
                x_step = 1
                
            if y_start > y_end:
                y_step = -1
            else:
                y_step = 1
            
            x_line = []
            y_line = []
            for x_val in range(x_start, x_end, x_step):
                x_line.append(x_val)
            
            for y_val in range(y_start, y_end, y_step):
                y_line.append(y_val)
            
            print (x_line, y_line)
            
                            
    return(board)
                    
                        

    
    

            
    
    
#test = sol_a("test.txt")
#experimental = sol_a("input.txt")

test = sol_b("test.txt")
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 13:38:51 2022

@author: abelw
"""

#CURRENTLY UNFINISHED

def broken_sol_a(filepath):
    
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
        x_dims.append(pair[0][0])
        x_dims.append(pair[1][0])
        
        y_dims.append(pair[0][1])
        y_dims.append(pair[1][1])
    
    row_size = int(max(x_dims))
    number_of_rows = int(max(y_dims))
    
    board = []
    base_board = []
    blank_row = []
    for i in range(row_size):
        blank_row.append(0)
    
    for i in range(number_of_rows):
        board.append(blank_row)
        base_board.append(blank_row)
    
    
    
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
            points = []
            y_val = y_start-1
            for x_val in range(x_start, x_end):
                points.append([y_val, x_val])
            for coords in points:
                print(coords)
                print(coords[0])
                print(board[coords[0]][coords[1]])
                local_value = board[coords[0]][coords[1]]
                local_value += 1
                print(local_value)
                board[1][1] = local_value
                print(board)
                #print(board)
            
        
        break


def sol_a(filepath):
    with open(filepath) as file:
        data = file.readlines()
    
    tracks = []
    #Data generation
    for line in data:
        line = line.split(" -> ")
        line[0] = (line[0].split(","))
        line[1] = (line[1].strip("\n").split(","))
        
        line[0][0], line[0][1] = int(line[0][0]), int(line[0][1])
        line[1][0], line[1][1] = int(line[1][0]), int(line[1][1])
        
        tracks.append(line)
    
    #Data processing
    for path in tracks:
        start = path[0]
        end = path[1]
        
        
        
        
        
        print(start, end)
        
        if start[0] == end[0]:
            print("Same x axis")

            print(y_points)
        elif start[1] == end[1]:
            print("Same y axis")
        
    
    
    
    
    return (tracks)
    
    
    
test = sol_a("test.txt")
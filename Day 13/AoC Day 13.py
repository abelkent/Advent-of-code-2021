# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 16:37:29 2022

@author: abelw
"""

def sol_a(data_filepath, instruction_filepath):
    #Get data
    with open(data_filepath) as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]

    #Get instruction
    with open(instruction_filepath) as file:
        instructions = file.readlines()
        instruction = instructions[0]
    

    #Find board scope
    x_array, y_array = [],[]
    for line in data:
        x,y = line.split(",")
        x = int(x)
        y = int(y)
        x_array.append(x)
        y_array.append(y)
    
    x_max = max(x_array)
    y_max = max(y_array)
    print("Board dimensions " + str(x_max) + " " + str(y_max))
    
    #Plot board
    board = []
    for y in range(y_max+1):
        board.append(["."]*(x_max+1))
    
    for index in range(len(x_array)):
        x_coord = x_array[index]
        y_coord = y_array[index]
        board[y_coord][x_coord] = "#"
        
    #Process instruction
    instruction = instruction.strip("fold along")
    axis, index = instruction.split("=")
    print(axis, index)
    index = int(index)
    if axis == "y":
        fold = "Up"
    elif axis == "x":
        fold = "Left"
    else:
        raise("Unexpected Error, unknown fold direction")
    
    print(fold)
    
    #Function for combining boards (Assumes equal board dimensions)
    def superimpose(board_a,board_b):
        for index_y in range(len(board_a)):
            for index_x in range(len(board_a[0])):
                
                if (board_a[index_y][index_x] == "#") or (board_b[index_y][index_x] == "#"):
                    board_a[index_y][index_x] = "#"
                    print("set")
        
        return(board_a)
                
        
    
    if fold == "Up":
        top_board = board[:index]
        bottom_board = board[index+1:]
        
        bottom_board.reverse()
        new_board = (superimpose(top_board, bottom_board))
    
    elif fold == "Left":
        left_board = []
        right_board = []
        for row in board:
            left_board.append(row[:index])
            right_row = row[index+1:]
            right_row.reverse()
            right_board.append(right_row)
        new_board = (superimpose(left_board, right_board))
    
    total_points = 0
    for row in new_board:
        for item in row:
            if item == "#":
                total_points += 1

    return (total_points)
    
#test = sol_a("test data.txt","test instructions.txt")
#experimental = sol_a("input data.txt", "input instructions.txt")


def sol_b(data_filepath, instruction_filepath):
    #Get data
    with open(data_filepath) as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]

    #Get instruction
    with open(instruction_filepath) as file:
        instructions = file.readlines()
    

    #Find board scope
    x_array, y_array = [],[]
    for line in data:
        x,y = line.split(",")
        x = int(x)
        y = int(y)
        x_array.append(x)
        y_array.append(y)
    
    x_max = max(x_array)
    y_max = max(y_array)
    print("Board dimensions " + str(x_max) + " " + str(y_max))
    
    #Plot board
    board = []
    for y in range(y_max+1):
        board.append(["."]*(x_max+1))
    
    for index in range(len(x_array)):
        x_coord = x_array[index]
        y_coord = y_array[index]
        board[y_coord][x_coord] = "#"
    
    def process_instruction(instruction):
        nonlocal board
        #Process instruction
        instruction = instruction.strip("fold along")
        axis, index = instruction.split("=")
        print(axis, index)
        index = int(index)
        if axis == "y":
            fold = "Up"
        elif axis == "x":
            fold = "Left"
        else:
            raise("Unexpected Error, unknown fold direction")
        
        print(fold)
        
        #Function for combining boards (Assumes equal board dimensions)
        def superimpose(board_a,board_b):
            for index_y in range(len(board_a)):
                for index_x in range(len(board_a[0])):
                    
                    if (board_a[index_y][index_x] == "#") or (board_b[index_y][index_x] == "#"):
                        board_a[index_y][index_x] = "#"
                        #print("set")
            
            return(board_a)
                    
            
        
        if fold == "Up":
            top_board = board[:index]
            bottom_board = board[index+1:]
            
            bottom_board.reverse()
            board = (superimpose(top_board, bottom_board))
        
        elif fold == "Left":
            left_board = []
            right_board = []
            for row in board:
                left_board.append(row[:index])
                right_row = row[index+1:]
                right_row.reverse()
                right_board.append(right_row)
            board = (superimpose(left_board, right_board))
        

    for instruction in instructions:
        process_instruction(instruction)
    
    print(board)
    return(board)
    
test = sol_b("test data.txt","test instructions.txt")
experimental = sol_b("input data.txt", "input instructions.txt")
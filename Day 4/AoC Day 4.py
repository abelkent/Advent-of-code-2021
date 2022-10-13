# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:16:45 2022

@author: abelw
"""

import itertools
import time

#test_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

class Bingo_board():
    
    def __init__(self, board_data):
        self.raw_data = []
        self.raw_tags = {}
        
        for item in board_data:
            self.raw_data = self.raw_data + item.split()
        
        self.row_1 = self.raw_data[0:5]
        self.row_2 = self.raw_data[5:10]
        self.row_3 = self.raw_data[10:15]
        self.row_4 = self.raw_data[15:20]
        self.row_5 = self.raw_data[20:25]
        
        
        
        self.column_1 = [self.raw_data[0], self.raw_data[5], self.raw_data[10]
                         , self.raw_data[15], self.raw_data[20]]
        self.column_2 = [self.raw_data[1], self.raw_data[6], self.raw_data[11]
                         , self.raw_data[16], self.raw_data[21]]
        self.column_3 = [self.raw_data[2], self.raw_data[7], self.raw_data[12]
                         , self.raw_data[17], self.raw_data[22]]
        self.column_4 = [self.raw_data[3], self.raw_data[8], self.raw_data[13]
                         , self.raw_data[18], self.raw_data[23]]
        self.column_5 = [self.raw_data[4], self.raw_data[9], self.raw_data[14]
                         , self.raw_data[19], self.raw_data[24]]        

    
        self.diagonal_1 = [self.raw_data[0], self.raw_data[6], self.raw_data[12], self.raw_data[18]
                           , self.raw_data[24]]
        self.diagonal_2 = [self.raw_data[20], self.raw_data[16], self.raw_data[12], self.raw_data[8], self.raw_data[4]]
    
        self.axes = [self.row_1,
                     self.row_2,
                     self.row_3,
                     self.row_4,
                     self.row_5,
                     
                     self.column_1,
                     self.column_2,
                     self.column_3,
                     self.column_4,
                     self.column_5,
                     
                     self.diagonal_1,
                     self.diagonal_2]
        
        print(len(self.axes))

    def victory_check(self, tagged_numbers):
        for axis in self.axes:
            print("Check")
            local_check = []
            for item in axis:
                if item in tagged_numbers:
                    local_check.append(True)
                else:
                    local_check.append(False)
            if all(local_check):
                self.victory_calc(axis)
                
    def victory_calc(self, axis):
        print(axis)

def bingo_run(filepath):
    
    with open(filepath) as file:
        data = file.readlines()
        
    bingo_boards = []

    local_board = []
    
    for line in data:
        if len(line) == 1:
            pass
        else:
            local_board.append(line)
        
        if len(local_board) == 5:
            bingo_boards.append(local_board)
            local_board = []
    
    
    board_classes = []
    for board in bingo_boards:
        board_classes.append(Bingo_board(board))
    
    print(board_classes)
    for board in board_classes:
        board.victory_check(test_numbers)
    return(bingo_boards)

def sol_a(input_filepath, numbers_filepath):
    
    marked_numbers = []
    
    with open(input_filepath) as file:
        data = file.readlines()
    
    with open(numbers_filepath) as file:
        numbers = file.read()
        numbers = numbers.split(",")
        new_numbers = []
        for number in numbers:
            new_numbers.append(int(number))
        numbers = new_numbers
        
    board_set = []
    local_board = []
    
    for line in data:
        if len(line) == 1:
            pass
        else:
            line = line.split(" ")
            new_line = []
            for element in line:
                if len(element) != 0:
                    new_line.append(int(element))
            local_board.append(new_line)
        
        if len(local_board) == 5:
            board_set.append(local_board)
            local_board = []
            
    
    solved = False
    while ((not solved) and (len(numbers) != 0)):
        #time.sleep(1)
        marked_numbers.append(numbers.pop(0))
        print(marked_numbers)
        
        for board in board_set:
            #Row check
            for row in board:
                #print(row)
                if (all(x in marked_numbers for x in row)):
                    print("Solved - row")
                    solution = board
                    solved = True
        
            #Column check
            for index in range(len(board)):
                column = []
                for row in board:
                    column.append(row[index])
                    
                if (all(x in marked_numbers for x in column)):
                    print("Solved - column")
                    solution = board
                    solved = True
                    
                    #print("No solve - column")
            
# =============================================================================
#             #Diagonal check
#             diagonal_down = [board[0][0], board[1][1], board[2][2], board[3][3], board[4][4]]
#             #print(diagonal_down)
#             diagonal_up = [board[0][4], board[1][3], board[2][2], board[3][1], board[4][0]]
#             #print(diagonal_up)
#             
#             if (all(x in marked_numbers for x in diagonal_down)):
#                 print ("Solved - diagonal down")
#                 solution = board
#                 solved = True
#                 
#             
#             if (all(x in marked_numbers for x in diagonal_up)):
#                 print("Solved - diagonal up")
#                 solution = board
#                 solved = True
# =============================================================================
        
        if solved == True:
            break
        
    print(solution)
    print(marked_numbers)
    
    flat_solution = []
    for row in solution:
        for item in row:
            flat_solution.append(item)
    
    unmarked_total = 0
    for element in flat_solution:
        if element not in marked_numbers:
            unmarked_total += element
    
    print(unmarked_total)
    
    final_guess = marked_numbers.pop()
    
    return (unmarked_total * final_guess)


def sol_b(input_filepath, numbers_filepath):
    
    marked_numbers = []
    
    with open(input_filepath) as file:
        data = file.readlines()
    
    with open(numbers_filepath) as file:
        numbers = file.read()
        numbers = numbers.split(",")
        new_numbers = []
        for number in numbers:
            new_numbers.append(int(number))
        numbers = new_numbers
        
    board_set = []
    local_board = []
    
    for line in data:
        if len(line) == 1:
            pass
        else:
            line = line.split(" ")
            new_line = []
            for element in line:
                if len(element) != 0:
                    new_line.append(int(element))
            local_board.append(new_line)
        
        if len(local_board) == 5:
            board_set.append(local_board)
            local_board = []
    
    clone_board_set = list(board_set)
    print(clone_board_set)
    
    while (len(clone_board_set) > 0):
        #time.sleep(1)
        marked_numbers.append(numbers.pop(0))
        print(marked_numbers)
        
        for board in board_set:
            #Row check
            if board in clone_board_set:
                for row in board:
                    #print(row)
                    if (all(x in marked_numbers for x in row)):
                        if len(clone_board_set) == 1:
                            solution = clone_board_set[0]
                        clone_board_set.remove(board)
                        print("Removed")
            
            if board in clone_board_set:
                #Column check
                for index in range(len(board)):
                    column = []
                    for row in board:
                        column.append(row[index])
                        
                    if (all(x in marked_numbers for x in column)):
                        if len(clone_board_set) == 1:
                            solution = clone_board_set[0]
                        clone_board_set.remove(board)
                        print("Removed")
                        
                        #print("No solve - column")

        
    print(solution)
    
    flat_solution = []
    for row in solution:
        for item in row:
            flat_solution.append(item)
            
    print(flat_solution)
    
    unmarked_total = 0
    for element in flat_solution:
        if element not in marked_numbers:
            unmarked_total += element
    
    print(unmarked_total)
    
    final_guess = marked_numbers.pop()
    
    return (unmarked_total * final_guess)
    

    
#test = bingo_run("test.txt")

#test = sol_b("test.txt","test numbers.txt")
experimental = sol_b("input.txt", "input numbers.txt")
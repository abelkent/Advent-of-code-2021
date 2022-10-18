# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:33:27 2022

@author: abelw
"""

def sol_a(filepath):
    
    with open(filepath) as file:
        data = file.readlines()
        grid = []
        for line in data:
            local_line = []
            for element in line.strip("\n"):
                local_line.append(int(element))
            
            grid.append(local_line)
    
    
    
    def get_neighbours_positions(row_idx,col_idx):
        
        neighbours = ["A","B","C","D","E","F","G","H"]
    
        #Top Row
        if row_idx == 0:
            neighbours[0], neighbours[1],neighbours[2] = None,None,None
        else:
            neighbours[0] = [row_idx-1, col_idx-1]
            neighbours[1] = [row_idx-1, col_idx]
            neighbours[2] = [row_idx-1, col_idx+1]
            
        #Bottom row
        if row_idx == 9:
            neighbours[5], neighbours[6], neighbours[7] = None, None, None
        else:
            neighbours[5] = [row_idx+1, col_idx-1]
            neighbours[6] = [row_idx+1, col_idx]
            neighbours[7] = [row_idx+1, col_idx+1]
        
        #Left col
        if col_idx == 0:
            neighbours[0], neighbours[3], neighbours[5] = None, None, None
        else:
            if neighbours[0] != None:
                neighbours[0] = [row_idx-1, col_idx-1]
            neighbours[3] = [row_idx, col_idx-1]
            if neighbours[5] != None:
                neighbours[5] = [row_idx+1, col_idx-1]
        
        #Right col
        if col_idx == 9:
            neighbours[2], neighbours[4], neighbours[7] = None, None, None
        else:
            if neighbours[2] != None:
                neighbours[2] = [row_idx-1, col_idx+1]
            neighbours[4] = [row_idx, col_idx+1]
            if neighbours[7] != None:
                neighbours[7] = [row_idx+1, col_idx+1]
        
        
        if None in neighbours:
            while None in neighbours:
                neighbours.remove(None)
        
        return(neighbours)

    
    def increment_grid():
        for row_idx in range(10):
            for col_idx in range(10):
                grid[row_idx][col_idx] += 1


    flash_points = []    
    
    def flash_check():
        #Check which points are going to flash and increment neighbours
        new_flash = False
        for row_idx in range(10):
            for col_idx in range(10):
                if (grid[row_idx][col_idx] > 9) and ([row_idx, col_idx] not in flash_points):
                    flash_points.append([row_idx,col_idx])
                    new_flash = True
                    for neighbour in get_neighbours_positions(row_idx, col_idx):
                        grid[neighbour[0]][neighbour[1]] += 1
        if new_flash == True:
            flash_check()

    total_flashes = 0

    def flash_reset():
        for point in flash_points:
            grid[point[0]][point[1]] = 0
        

    
    def step():
        increment_grid()
        flash_check()
        flash_reset()
        nonlocal total_flashes
        nonlocal flash_points
        total_flashes += len(flash_points)
        flash_points = []
        
    
    for i in range(100):
        step()
    return(total_flashes)
    
def sol_b(filepath):

    with open(filepath) as file:
        data = file.readlines()
        grid = []
        for line in data:
            local_line = []
            for element in line.strip("\n"):
                local_line.append(int(element))
            
            grid.append(local_line)
    
    
    
    def get_neighbours_positions(row_idx,col_idx):
        
        neighbours = ["A","B","C","D","E","F","G","H"]
    
        #Top Row
        if row_idx == 0:
            neighbours[0], neighbours[1],neighbours[2] = None,None,None
        else:
            neighbours[0] = [row_idx-1, col_idx-1]
            neighbours[1] = [row_idx-1, col_idx]
            neighbours[2] = [row_idx-1, col_idx+1]
            
        #Bottom row
        if row_idx == 9:
            neighbours[5], neighbours[6], neighbours[7] = None, None, None
        else:
            neighbours[5] = [row_idx+1, col_idx-1]
            neighbours[6] = [row_idx+1, col_idx]
            neighbours[7] = [row_idx+1, col_idx+1]
        
        #Left col
        if col_idx == 0:
            neighbours[0], neighbours[3], neighbours[5] = None, None, None
        else:
            if neighbours[0] != None:
                neighbours[0] = [row_idx-1, col_idx-1]
            neighbours[3] = [row_idx, col_idx-1]
            if neighbours[5] != None:
                neighbours[5] = [row_idx+1, col_idx-1]
        
        #Right col
        if col_idx == 9:
            neighbours[2], neighbours[4], neighbours[7] = None, None, None
        else:
            if neighbours[2] != None:
                neighbours[2] = [row_idx-1, col_idx+1]
            neighbours[4] = [row_idx, col_idx+1]
            if neighbours[7] != None:
                neighbours[7] = [row_idx+1, col_idx+1]
        
        
        if None in neighbours:
            while None in neighbours:
                neighbours.remove(None)
        
        return(neighbours)

    
    def increment_grid():
        for row_idx in range(10):
            for col_idx in range(10):
                grid[row_idx][col_idx] += 1


    flash_points = []    
    
    def flash_check():
        #Check which points are going to flash and increment neighbours
        new_flash = False
        for row_idx in range(10):
            for col_idx in range(10):
                if (grid[row_idx][col_idx] > 9) and ([row_idx, col_idx] not in flash_points):
                    flash_points.append([row_idx,col_idx])
                    new_flash = True
                    for neighbour in get_neighbours_positions(row_idx, col_idx):
                        grid[neighbour[0]][neighbour[1]] += 1
        if new_flash == True:
            flash_check()

    total_flashes = 0

    def flash_reset():
        for point in flash_points:
            grid[point[0]][point[1]] = 0
        

    
    def step():
        increment_grid()
        flash_check()
        flash_reset()

        
    
    index = 0
    while True:
        index = index + 1
        step()
        if len(flash_points) == 100:
            break
        else:
            flash_points = []
        
    return index

test = sol_b("test.txt")
experimental = sol_b("input.txt")
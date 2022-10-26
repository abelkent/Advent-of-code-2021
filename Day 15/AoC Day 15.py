# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:12:20 2022

@author: abelw
"""
import time

def sol_a(filepath):
    
    with open(filepath) as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]
        board = [ [int(x) for x in line] for line in data]
    

    #point = [Y][X]
    
    def recursive_pathfinder(current_location, visited_points, current_risk):
        #print(visited_points)
        
        def get_all_neighbours(point):
            #             Top , Bottom , Left , Right
            neighbours = [None, None, None, None]
            
            #Along top row
            if point[0] != 0:
                neighbours[0] = [point[0]-1,point[1]]
            
            #Along bottom row
            if point[0] != len(board)-1:
                neighbours[1] = [point[0]+1, point[1]]
            
            #Along left wall
            if point[1] != 0:
                neighbours[2] = [point[0], point[1]-1]
            
            if point[1] != (len(board[0])-1):
                neighbours[3] = [point[0], point[1]+1]
        
        
            while None in neighbours:
                neighbours.remove(None)
            
            #print(neighbours)
            
            return(neighbours)
        
        
        def get_valid_neighbours(neighbours):
            valid_neighbours = []
            
            for neighbour in neighbours:
                if neighbour not in visited_points:
                    valid_neighbours.append(neighbour)
            
            return(valid_neighbours)
        
                
        def check_current_point():
            time.sleep(.1)
            local_risk = board[current_location[0]][current_location[1]] + current_risk
            
            local_neighbours = get_all_neighbours(current_location)
            valid_local_neighbours = get_valid_neighbours(local_neighbours)
            #print(valid_local_neighbours)
            
            if current_location == [len(board),len(board[0])-1]:
                print("REACHED END")
                return local_risk
            
            elif len(valid_local_neighbours) == 0:
                print("NO VALID NEIGHBOURS")
                return 500000
            
            else:
                paths = []
                new_visited_points = list(visited_points)
                new_visited_points.append(current_location)
                for neighbour in valid_local_neighbours:
                    local_path_score = recursive_pathfinder(neighbour, new_visited_points, local_risk)
                    paths.append(local_path_score)
            
            
            if len(paths) == None:
                print("WTF")
            
            else:
            
                print(paths)
                return min(paths)
        
        check_current_point()
            
        
        
    recursive_pathfinder([0,0],[],0)
        #Reaches end
        #Runs out of places to go

test = sol_a("test.txt")
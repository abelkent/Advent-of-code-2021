# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:06:08 2022

@author: abelw
"""
import time

#God am I sick of pathfinding, return to later

def sol_a(filepath):
    
    with open(filepath) as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]
        data = [[x for x in line.strip()] for line in data]
    

    def get_value(point):
        return int(data[point[0]][point[1]])

    print(get_value([0,0]))
    
    def get_all_neighbours(point, visited_points):
        
        neighbours  = [None, None, None, None]
        #Top
        if point[0] != 0:
            neighbours[0] = [point[0]-1,point[1]]
        
        #Bottom
        if point[0] != len(data)-1:
            neighbours[1] = [point[0]+1,point[1]]
        
        #Left
        if point[1] != 0:
            neighbours[2] = [point[0],point[1]-1]
        
        #Right
        if point[1] != len(data[0])-1:
            neighbours[3] = [point[0],point[1]+1]
        
        #Removes blank spaces from edge of board
        while None in neighbours:
            neighbours.remove(None)
        
        
        #Removes previously visited points
        valid_neighbours = []
        for neighbour in neighbours:
            if neighbour not in visited_points:
                valid_neighbours.append(neighbour)
        
        return(valid_neighbours)
    
    def pathfinder(point, goal, current_risk, previously_visited):
        
        new_risk = current_risk + get_value(point) #Calculates new risk
        
        #Reaches goal
        if point == goal:
            print(new_risk)
            return new_risk
    
        #Has run out of places to go
        neighbours = get_all_neighbours(point, previously_visited)
        if len(neighbours) == 0:
            return None
        
        #Checks other paths and return minimum
        new_path_values = []
        visited_including_current = list(previously_visited)
        visited_including_current.append(point)
        for neighbour in neighbours:
            new_path_values.append(pathfinder(neighbour, goal, new_risk, visited_including_current))
        print(new_path_values)
        
        
        time.sleep(1)
    
    pathfinder([0,0],[0,5], 0, [])
          
test = sol_a("test.txt")
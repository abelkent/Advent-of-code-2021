# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 16:03:58 2022

@author: abelw
"""

def sol_a(filepath):
    
    with open(filepath) as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]

    #Get map
    def map_maker(array):
        cave_map = dict()
        for line in array:
            origin, destination = line.split("-")
            
            if origin not in cave_map:
                cave_map[origin] = []
                
            if destination not in cave_map:
                cave_map[destination] = []
            
            cave_map[origin].append(destination)
            cave_map[destination].append(origin)
            
        return(cave_map)
    
    #Recursive function
    def path_finder(origin, path, cave_map):
        #Reached end
        if origin == "end":
            return 1
        
        #Revisit small cave
        elif (origin.lower() == origin) and (origin in path):
            return 0
    
        #Continue on
        else:
            new_path = list(path)
            new_path.append(origin)
            
            total = 0
            for destination in cave_map[origin]:
                total += path_finder(destination, new_path, cave_map)
            
            return total
    
    cave_map = map_maker(data)
    test = path_finder("start",[],cave_map)
    print(test)

def sol_b(filepath):
    
    with open(filepath) as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]

    #Get map
    def map_maker(array):
        cave_map = dict()
        for line in array:
            origin, destination = line.split("-")
            
            if origin not in cave_map:
                cave_map[origin] = []
                
            if destination not in cave_map:
                cave_map[destination] = []
            
            cave_map[origin].append(destination)
            cave_map[destination].append(origin)
            
        return(cave_map)
    
    #Recursive function
    def path_finder(origin, path, cave_map, small_cave_flag):
        #Reached end
        if origin == "end":
            return 1
        
        #Revisit small cave
        elif (origin.lower() == origin) and (origin in path):
            #If not revisited any before
            if (origin != "start") and (small_cave_flag == False):
                small_cave_flag = True
                new_path = list(path)
                new_path.append(origin)
                
                total = 0
                for destination in cave_map[origin]:
                    total += path_finder(destination, new_path, cave_map, small_cave_flag)
                
                return total
            #Have revisited one before
            else:
                return 0
                
                
                    
                    
            
            #Allowed
            
            
            #Forbidden
    
        #Continue on
        else:
            new_path = list(path)
            new_path.append(origin)
            
            total = 0
            for destination in cave_map[origin]:
                total += path_finder(destination, new_path, cave_map, small_cave_flag)
            
            return total
    
    cave_map = map_maker(data)
    test = path_finder("start",[],cave_map,False)
    print(test)


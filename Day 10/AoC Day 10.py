# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:02:37 2022

@author: abelw
"""

def sol_a(filepath):
    
    with open(filepath) as file:
        data = file.readlines()
    
    open_characters = ["(","[","{","<"]
    close_characters = [")","]","}",">"]
    pairs = zip(open_characters, close_characters)
    corruption_map = zip(close_characters, [3, 57, 1197, 25137])
    corruption_map = dict(corruption_map)
    open_and_close = dict(pairs)

    total_corrupt = []

    for line in data:
        stack = []    
        for element in line:
            if element in open_characters:
                stack.append(open_and_close.get(element))
            elif element in close_characters:
                if stack[-1] == element:
                    stack.pop(-1)
                else:
                    total_corrupt.append(element)
                    break
    
    total_corruption = 0
    for element in total_corrupt:
        total_corruption += corruption_map.get(element)
        
    return(total_corrupt, total_corruption)

def sol_b(filepath):
    with open(filepath) as file:
        data = file.readlines()
    
    open_characters = ["(","[","{","<"]
    close_characters = [")","]","}",">"]
    open_and_close = dict(zip(open_characters, close_characters))
    corruption_map = dict(zip(close_characters, [1,2,3,4]))
    
    
    corrupted_lines = []
    for line in data:
        stack = []    
        for element in line:
            if element in open_characters:
                stack.append(open_and_close.get(element))
            elif element in close_characters:
                if stack[-1] == element:
                    stack.pop(-1)
                else:
                    corrupted_lines.append(line)
                    break
    
    for corrupted in corrupted_lines:
        if corrupted in data:
            data.remove(corrupted)
    
    total_missing = []
    
    for line in data:
        missing_characters = []    
        for element in line:
            if element in open_characters:
                missing_characters.append(open_and_close.get(element))
            elif element in close_characters:
                if missing_characters[-1] == element:
                    missing_characters.pop(-1)
        missing_characters.reverse()
        total_missing.append(missing_characters)
        
    corruption_scores = []
    
    for character_set in total_missing:
        corruption_score = 0
        for character in character_set:
            corruption_score *= 5
            corruption_score += corruption_map.get(character)
        corruption_scores.append(corruption_score)
    
    corruption_scores.sort()
    
    mid_index = round(len(corruption_scores)/2)
    median = corruption_scores[mid_index]
            
    
    
    return(median, corruption_scores)
test = sol_b("test.txt")
experimental = sol_b("input.txt")
        
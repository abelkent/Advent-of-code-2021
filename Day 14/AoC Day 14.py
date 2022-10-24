# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:21:10 2022

@author: abelw
"""

def sol_a(chains_filepath, template_filepath):
    with open(chains_filepath) as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]
    
    with open(template_filepath) as file:
        template = file.read()
        template = template.strip("\n")
    
    reaction_dict = dict()
    
    for line in data:
        reactants, product = line.split(" -> ")
        output = [reactants[0], product, reactants[1]]
        output = "".join(output)
        reaction_dict[reactants] = output
    
    def iterate():
        nonlocal template
        new_template = ""
        print(len(template))
        for index in range(0, len(template)-1):
            pair = "".join([template[index],template[index+1]])
            reaction = reaction_dict[pair]
            #print(reaction[:2])
            #print(new_template)
            if index == (len(template)-2):
                new_template = new_template + reaction
            else:
                new_template = new_template + reaction[:2]
        
        template = new_template
    
    for x in range(40):
        iterate()
        
    template_split = ([*template])
    letter_set = set([*template])
    letter_counts = []
    for letter in letter_set:
        letter_counts.append(template_split.count(letter))
    
    return((max(letter_counts)) - min(letter_counts))



def sol_b(chains_filepath, template_filepath):
    with open(chains_filepath) as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]
    
    with open(template_filepath) as file:
        template = file.read()
        template = template.strip("\n")
    
    reaction_dict = dict()
    
    for line in data:
        reactants, product = line.split(" -> ")
        output = [reactants[0], product, reactants[1]]
        output = "".join(output)
        reaction_dict[reactants] = output
    
    def iterate():
        nonlocal template
        new_template = ""
        print(len(template))
        for index in range(0, len(template)-1):
            pair = "".join([template[index],template[index+1]])
            reaction = reaction_dict[pair]
            #print(reaction[:2])
            #print(new_template)
            if index == (len(template)-2):
                new_template = new_template + reaction
            else:
                new_template = new_template + reaction[:2]
        
        template = new_template
    
    for x in range(40):
        iterate()
        
    template_split = ([*template])
    letter_set = set([*template])
    letter_counts = []
    for letter in letter_set:
        letter_counts.append(template_split.count(letter))
    
    return((max(letter_counts)) - min(letter_counts))
        
    
        
        
#test = sol_a("test chains.txt", "test template.txt")
experimental = sol_a("input chains.txt", "input template.txt")
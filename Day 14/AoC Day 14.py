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
    reaction_count = dict()
    raw_element_count = dict()
    
    for line in data:
        reactants, product = line.split(" -> ")
        if reactants not in reaction_count:
            reaction_count[reactants] = 0
        
        product_1 = "".join([reactants[0],product])
        product_2 = "".join([product, reactants[1]])
        #print(product_1, product_2)
        reaction_dict[reactants] = [product_1, product_2]
        
        for letter in reactants:
            if letter not in raw_element_count:
                raw_element_count[letter] = 0
    
    
    #Initial count
    for index in range(0, len(template)-1):
        reactants = template[index:index+2]
        reaction_count[reactants]+= 1
    
    for letter in template:
        print(letter)
        raw_element_count[letter] += 1
        
    def iterate():
        nonlocal reaction_dict
        nonlocal reaction_count
        nonlocal raw_element_count
        new_reaction_count = dict(reaction_count)
        #print(reaction_count)
        
        for pair in reaction_count:
            current_count = reaction_count[pair]
            #print(current_count)
            products = reaction_dict[pair]
            for chemical in products:
                new_reaction_count[chemical]+= current_count
            new_reaction_count[pair] -= current_count
            new_letter = products[1][0]
            raw_element_count[new_letter] += current_count
            #print(new_letter)
                

        #print(new_reaction_count)
        reaction_count = new_reaction_count
                
        
    for count in range(40):
        iterate()
            
    
    values = raw_element_count.values()
    return( max(values) - min(values))
    
        
    
        
        
#test = sol_a("test chains.txt", "test template.txt")
experimental = sol_b("input chains.txt", "input template.txt")
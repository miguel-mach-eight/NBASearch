# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:30:22 2021
 
@author: Miguel
"""

import json
import requests

def to_number(A):
    
    B = int(A)
    
    return B
        

def search(Number):
    response = requests.get("https://mach-eight.uc.r.appspot.com/")

    data = json.loads(response.text)
    PLAYERS = data["values"]

    answer_list = []

    for player1 in PLAYERS:
    
        raw_height = player1['h_in']
        height_1 = to_number(raw_height)
    
        PLAYERS.remove(player1)
        for player2 in PLAYERS:
        
            raw_height = player2['h_in']
            height_2 = to_number(raw_height)
        
            result = height_1 + height_2
        
            if result == Number:
                par = (player1['first_name'] + ' ' + player1['last_name'] + ' & ' + 
                       player2['first_name'] + ' ' + player2['last_name'])
            
                answer_list.append(par)
        
    return answer_list

def executer():
    Number = int(input("insert your integer: "))
    result = search(Number)
    
    return result
    
if __name__=="__main__":
    
    result = executer()
    stop_here = len(result)
    
    while stop_here == 0:
    
        print("No matches found, please try with a new number \n\n")
    
        result = executer()
        stop_here = len(result)
        
    print(result)
    
            
        
    
        
        
    


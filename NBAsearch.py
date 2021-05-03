# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:30:22 2021
 
@author: Miguel
"""

import json
import requests
import collections

        

def search(Number):
    response = requests.get("https://mach-eight.uc.r.appspot.com/")

    data = json.loads(response.text)
    PLAYERS = data["values"]

    d = collections.defaultdict(list)
    for player in players:
        d[int(player['h_in'])].append(player['first_name'] + " " + player['last_name'])

    return [player + " & " + other
        for height in d
            if total - height in d
                for other in d[total - height]
                    for player in d[height]
                        if player < other
    ]

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
    
            
        
    
        
        
    


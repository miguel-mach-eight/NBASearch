# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:30:22 2021
 
@author: Miguel
"""

import json
import requests
import collections
import time

def search(Number):
    response = requests.get("https://mach-eight.uc.r.appspot.com/")

    data = json.loads(response.text)
    PLAYERS = data["values"]
    
    PLAYERS = sorted(PLAYERS, key=lambda k: k['h_in'])
    
    lo, hi = 0, len(PLAYERS) - 1
    
    answer_list = []
    
    special_case = False
    
    start_time = time.time()
    
    while lo < hi:
        
        player1 = PLAYERS[lo]
        player2 = PLAYERS[hi]
        player3 = PLAYERS[lo+1]
        player4 = PLAYERS[hi-1]
        
        total = int(player1['h_in']) + int(player2['h_in'])
        
        if total == Number:
            pair = (player1['first_name'] + ' ' + player1['last_name'] + ' & ' + 
                       player2['first_name'] + ' ' + player2['last_name'])
            
            answer_list.append(pair)  
            
            if special_case == True:
                hi += 1
                lo += 1
                special_case == False
                
            if player1['h_in'] == player3['h_in']:
                if player2['h_in'] == player4['h_in']:
                    special_case = True
                    hi -= 1
                    
            elif player1['h_in'] == player3['h_in']:
                lo += 1
            
            elif player2['h_in'] == player3['h_in']:
                hi -= 1
            
            else:
                lo += 1
                hi -= 1
        
        elif total < Number:
            lo += 1
        
        else:
            hi -= 1
    
    elapsed_time = time.time() - start_time
    print('elapsed time = ', elapsed_time, 's')
    
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
    
            
        
    
        
        
    


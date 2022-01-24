# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 19:41:31 2022

@author: prajwal
"""
import requests
import json

url = "https://s3.amazonaws.com/open-to-cors/assignment.json"



r = requests.get(url).text

d  = json.loads(r)

temp = [] #dictionary data structure to store fetched JSON
    
for p_id, p_info in d.items():
    #print("\nPerson ID:", p_info)
    temp = p_info
    
    
#res = sorted(temp.items(), key = lambda x: x[1]['popularity'])
#print(res)
#print(*res, sep = "\n")
    
for p_id, p_info in temp.items():
    #print("\nPerson ID:", p_id)
    
    for key in p_info:
        if(key == 'title' or key == 'price'):
            print(key + ':', p_info[key])       #title,price
        
    
    
#print(r.json())


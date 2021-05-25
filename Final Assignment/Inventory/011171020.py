# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HUWkoXf5exu6SUcK4niPQBgRJ9BqvCD_
"""

import numpy as np

m = 11 #Maximum capacity
n= 5 #review length

begining_inventory= 3
total_demand= 0
ending_inventory= 0
shortage_quantity= 0
order_quantity= 8  
days_until_order_arrives= 2
arr_ending_inventory=[]
arr_days=[]
shortage_count=0


for cycle in range(10):
  print("Cycle no: ",cycle)
  for day in range (1,n+1):
    print("Day no: ", day)

    ##order arrives code: 
    days_until_order_arrives=days_until_order_arrives-1
    if(days_until_order_arrives==-1):
      begining_inventory= begining_inventory+ order_quantity
    

    daily_demand= np.random.choice(a=[0,1,2,3,4],p=[0.10,0.25,0.35,0.21,0.09])
    total_demand = daily_demand + shortage_quantity
    if total_demand> begining_inventory:
      shortage_quantity= total_demand-begining_inventory
      ending_inventory=0
      shortage_count=shortage_count+1

    else:
      ending_inventory= begining_inventory-total_demand
      shortage_quantity=0
    
    print("Begining Inventory: ",begining_inventory)
    print("Daily Demand: ",daily_demand)
    print("Ending Inventory: ",ending_inventory)
    print("Shortage Quantity: ",shortage_quantity)

    arr_ending_inventory.append(ending_inventory)
    arr_days.append(str(cycle) +":"+str(day) )
    begining_inventory=ending_inventory

    ##Review code (Task-1)
    #when day==n: , then you have to place an order. order_quantity; days_until_order_arrives (randomly)
    if day ==n:
      days_until_order_arrives= np.random.choice(a=[1,2,3],p=[0.6,0.3,0.1])
      order_quantity= m-ending_inventory
    print()


#average_ending_inventory
print("Average ending enventory", sum(arr_ending_inventory)/(n*(cycle+1)))
#number of days shortage occurs
print("Number of days shortage happend", shortage_count)
#ending inventory vs days graph:

import math
import random
import matplotlib.pyplot as plt
plt.plot(arr_days, arr_ending_inventory)
plt.rcParams["figure.figsize"] = (20,3)
plt.xlabel("Days") 
plt.ylabel("Ending Inventory of Each day") 
plt.show()
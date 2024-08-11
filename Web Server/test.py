# the code that works so far {}_{}


import csv
import json
import random
import requests
import time


RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

id  = input('Please Enter ID no: ')
filepath = 'purchases_user/'+str(id)+'.json'
with open(filepath, 'r') as file:
    data = json.load(file)
file.close()
totalPrice = 0
for item in data:
    line = item['Name'] + 'No:'+item['Quantity']
    totalPrice += float(item['Cost'])
    print(line)
print('Total Price:$',totalPrice)

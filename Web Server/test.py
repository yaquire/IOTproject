# the code that works so far {}_{}


import csv

from Cython.Compiler.TypeSlots import lenfunc

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"
# def choseingItem(data):
#     for i in range(len(data)):
#         print(i,':',data[i]['Name'])
#
#     chose = int(input('Please Enter Item chosen:'))
#     name = data[chose]['Name']
#     #print (name)
#     print('-'*50)
#     return name
#
# def writeCart(name):
#     name = name
#     # print(name)
#     data = []
#     filepath = "Web Server/purchases.csv"
#     with open(filepath, mode="r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             data.append(row)
#
#     rangeNo = []
#     number = 0
#     for i in range(len(data)):
#         dictName = data[i]['Name']
#         if name == dictName:
#             # print(i,'In dict')
#             rangeNo.append(i)
#             number = i
#         else:
#             rangeNo.append('Not in Data')
#     # print('RangeNo' , rangeNo)
#
#     i =0
#     hasInteger = any(isinstance(x, int) for x in rangeNo)
#     for x in rangeNo:
#         if type(x) == int:
#             i = x
#     # print(RED,hasInteger,RESET)
#     if hasInteger is False:
#         row = {}
#         row['Name'] = name
#         row["Quantity"] = 1
#         data.append(row)
#     elif hasInteger is True:
#         print('The index of the item is:',i)
#         quant = int(data[i]['Quantity'])
#         quant += 1
#         data[i]['Quantity'] = quant
#     else:
#         print(RED + 'ERROR' + RESET)
#
#     # print('--' * 50)
#     # print(data)
#     with open(filepath, mode="w", newline="") as file:
#         fieldnames = ["Name", "Quantity"]
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#
#         writer.writeheader()  # Write the header row
#
#         for person in data:
#             writer.writerow(person)
#
#     ####
#     # print(CYAN + str(data) + RESET)
#
#     datas = []
#     with open(filepath, mode="r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             datas.append(row)
#     print(MAGENTA + str(datas) + RESET)
#     return ()
#
#
# #THIS IS FOR THE TEST
# atat = []
# filepath = "Web Server/data.csv"
# with open(filepath, mode="r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         atat.append(row)
#
# while True:
#     name = choseingItem(atat)
#     swrite = writeCart(name)

# def priceNTotal():
purchaseData = []
storeData = []

try: purchasePath = "Web Server/purchases.csv"
except FileNotFoundError:
    print('Wrong Directory')
else: purchasePath = "purchases.csv"

with open(purchasePath, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        purchaseData.append(row)


try: storePath = "Web Server/data.csv"
except FileNotFoundError:
    print('Wrong Dir')
else: storePath = "data.csv"

with open(storePath, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        storeData.append(row)

for row in storeData:
    #print(MAGENTA, row, RESET)

    name = row["Name"]
    number = row["Quantity"]
    price = row["Price"]

    for i in range(len(purchaseData)):
        if purchaseData[i]['Name'] == name:
            print('Adding Price')
            purchaseData[i]['Price'] = price
        else:
            print('ERROR')


print("-" * 50)
print(RED, purchaseData, RESET)

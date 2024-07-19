import csv

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[0m'


def choseingItem(data):
    for i in range(len(data)):
        print(i,':',data[i])

    chose = int(input('Please Enter Item chosen:'))
    name = data[chose]['Name']
    #print (name)
    return name

def writeCart(name):
    name = name
    # print(name)
    data = []
    filepath = "purchases.csv"
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    rangeNo= []
    number = 0
    for i in range(len(data)):
        dictName = data[i]['Name']
        if name == dictName:
            #print(i,'In dict')
            rangeNo.append(i)
            number = i
        else:
            rangeNo.append('Not in Data')
    #print('RangeNo' , rangeNo)

    hasInteger = any(isinstance(x,int) for x in rangeNo)
    #print(RED,hasInteger,RESET)
    if hasInteger is False:
        row = {}
        row['Name'] = name
        row["Quantity"] = 1
        data.append(row)
    elif hasInteger is True:
        quant = int(data[i]['Quantity'])
        quant+=1
        data[i]['Quantity'] = quant
    else:
        print(RED+'ERROR'+RESET)

    #print('--' * 50)
    #print(data)
    with open(filepath, mode="w", newline="") as file:
        fieldnames = ["Name", "Quantity"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()  # Write the header row

        for person in data:
            writer.writerow(person)

    ####
    #print(CYAN + str(data) + RESET)

    datas = []
    filepath = "purchases.csv"
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            datas.append(row)
    #print(MAGENTA + str(datas) + RESET)
    return ()


#THIS IS FOR THE TEST
atat = []
filepath = "data.csv"
with open(filepath, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        atat.append(row)

#name = choseingItem(atat)
name = 'The Honoresd One'
swrite = writeCart(name)



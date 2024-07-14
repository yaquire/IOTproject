import csv

data = []
with open("Web Server/data.csv", mode="r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data.append(row)

for item in data:
    print(item)

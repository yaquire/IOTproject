import csv

data = []
with open("data.csv", mode="r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data.append(row)

# print(data)

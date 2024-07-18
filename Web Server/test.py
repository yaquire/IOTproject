import csv


def writeCart(name):
    name = name
    # print(name)
    data = []
    filepath = "Web Server/purchases.csv"
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
        # print(name)
        for row in data:
            rowName = row["Name"]
            # print(rowName)
            if rowName == name:
                # print("in")
                quantity = int(row["Quantity"])
                quantity += 1
                # print(name, quantity)
                row["Quantity"] = quantity
    with open(filepath, mode="w", newline="") as file:
        fieldnames = ["Name", "Quantity"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()  # Write the header row

        for person in data:
            writer.writerow(person)
    return ()


name = "Inifity Stones"
swrite = writeCart(name)


print("-" * 50)

import sqlite3

def get_data(name_of_file):
    infile = open(name_of_file, "r")
    data = infile.read().strip().split("\n")
    return [x.split(",") for x in data]

buns = get_data("files/BUNS.txt")
cakes = get_data("files/CAKES.txt")
loaves = get_data("files/LOAVES.txt")

db = sqlite3.connect("inventory_database.db")

for item in buns:
    db.execute("INSERT INTO Product(ProductCode, Name, Type, Location, Price) VALUES(?, ?, ?, ?, ?)", (item[0], item[1], "Bun", item[2], item[3]))
    db.execute("INSERT INTO Bun(ProductCode, PiecesPerPackage) VALUES(?, ?)", (item[0], item[4]))
for item in cakes:
    db.execute("INSERT INTO Product(ProductCode, Name, Type, Location, Price) VALUES(?, ?, ?, ?, ?)", (item[0], item[1], "Cake", item[2], item[3]))
    db.execute("INSERT INTO Cake(ProductCode, ServingSize, Shape) VALUES(?, ?, ?)", (item[0], item[4], item[5]))
for item in loaves:
    db.execute("INSERT INTO Product(ProductCode, Name, Type, Location, Price) VALUES(?, ?, ?, ?, ?)", (item[0], item[1], "Loaf", item[2], item[3]))
    db.execute("INSERT INTO Loaf(ProductCode, Weight) VALUES(?, ?)", (item[0], item[4]))

db.commit()
db.close()
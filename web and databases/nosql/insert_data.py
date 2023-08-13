import pymongo

infile = open("INVENTORY_SERIAL.txt", "r")
contents = infile.read().strip().split("\n")
data = []
for line in contents:
    serial, name, type, purchase_price, selling_price, quantity = line.strip().split("\t")
    data.append({"Serial_No": serial,
                 "Name": name,
                 "Type": type,
                 "Purchase_Price": purchase_price,
                 "Selling_Price": selling_price,
                 "Quantity": quantity})

client = pymongo.MongoClient("127.0.0.1", 27017)
client.drop_database("OUTLETS")
db = client.get_database("OUTLETS")
coll = db.get_collection("GEM")
coll.insert_many(data)
client.close()

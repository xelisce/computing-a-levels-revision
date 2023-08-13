import pymongo

client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.get_database("OUTLETS")
coll = db.get_collection("GEM")

data = [x for x in coll.find()]
bad_data = []

for line in data:
    serial = line["Serial_No"]
    name = line["Name"].replace(" ", "")
    if not(len(serial) == 4 and serial[0].isdigit() and serial[1].isalpha() and serial[2].isalpha() and serial[3].isdigit() and name.isalnum() and line["Quantity"].isdigit() and int(line["Quantity"]) > 0):
        bad_data.append(line)
        coll.delete_one({'Serial_No': serial})
    
print(bad_data)

client.close()
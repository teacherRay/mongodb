from pymongo import MongoClient 

client = MongoClient("mongodb+srv://Raymondo:M0ng0DB2019@cluster0-jotax.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

db = client.get_database('Ramones')

dblist = client.list_database_names()
if "Ramones" in dblist:
  print("The database exists.")

mycol = db["Albums"]
x = mycol.find_one()
print(x)

print("The collection name is : ", db.list_collection_names())

records = db.Albums
list(db.Albums.find())




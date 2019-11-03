from pymongo import MongoClient 

client = MongoClient("mongodb+srv://Raymondo:M0ng0DB2019@cluster0-jotax.mongodb.net/test?retryWrites=true&w=majority")

db = client.get_database('Ramones')

records = db.Albums

#records.count_documents({})
list(records.find())




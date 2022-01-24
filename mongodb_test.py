from pymongo import MongoClient 
url = "mongodb+srv://admin:admin@cluster0.6yidr.mongodb.net/pytech"
client = MongoClient(url)
db = client.PyTech 
print(db.list_collection_names())

from pymongo import MongoClient
import pandas as pd


df = pd.read_csv("cars.csv")


data = df.to_dict(orient='records')

# replace 'my_user', 'my_password', and 'my_database' with your own values
client = MongoClient('mongodb+srv://rootguvi:rootguvi@cluster0.u37z9wj.mongodb.net/test')

# replace 'my_collection' with the name of your collection
collection = client.my_database.my_collection

# insert the data into the collection
collection.insert_many(data)
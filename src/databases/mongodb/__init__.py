from pymongo import MongoClient
from os import environ
client = MongoClient(environ['MONGODB_URI'])

db = client[environ['MONGODB_NAME']]

chat = db['chats']

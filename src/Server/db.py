from pymongo import MongoClient

from Config.config import mongo_uri

conn = MongoClient('mongodb+srv://root:root@cluster0.91g9e.mongodb.net/BohemiaDatabase?retryWrites=true&w=majority')
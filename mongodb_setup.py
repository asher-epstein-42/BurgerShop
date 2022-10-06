import pymongo
from consts import mongo_uri

mongo_client = pymongo.MongoClient(mongo_uri)

# create collections
hamburger_db = mongo_client["food_db"]  # db
reviews = hamburger_db["reviews"]  # col
orders = hamburger_db["orders"]  # col
users = hamburger_db["users"]  # col
workers = hamburger_db["workers"]  # col

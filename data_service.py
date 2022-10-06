import re
from datetime import datetime as dt
from bson.objectid import ObjectId

from mongodb_setup import reviews, orders, users, workers  # importing the collections of the db
from consts import email_regex


# Data service for users:

def register_user(name: str, email: str, password: str, address: str):
    new_user = {
        "name": name,
        "register_time": dt.now(),
        "email": email,
        "password": password,
        "address": address,
    }
    users.insert_one(new_user)


def validate_email(email):
    return re.fullmatch(email_regex, email)



def search_email_db(email):
    check_if_email_in_db = users.find_one({"email": email})
    return check_if_email_in_db


def login_user(email: str, password: str):
    search_user_db = users.find_one({"email": email, "password": password})
    return search_user_db


def add_review(review: str):
    new_review = {
        "review": review,
        "time": dt.now(),
    }
    reviews.insert_one(new_review)


def add_order(account: str, order: str):
    new_order = {"Email": account,
                 "order": order,
                 "time": dt.now()}
    orders.insert_one(new_order)
    print(f'You ordered {order}')
    print("thank you for your order!")


def change_address(new_address, email):
    user = users.find_one({"email": email})
    old_address = {"address": user["address"]}
    updated_address = {"$set": {"address": new_address}}
    users.update_one(old_address, updated_address)


# Data service for workers:

def register_worker(name: str, password: str):
    new_worker = {"name": name,
                  "password": password,
                  "registered_time": dt.now()}
    workers.insert_one(new_worker)


def login_worker(name, password):
    search_worker_db = workers.find_one({"name": name, "password": password})
    return search_worker_db


def show_orders_worker():
    all_orders = orders.find()
    print([order for order in all_orders])


def delete_order(order_id):
    _id = ObjectId(order_id)
    order_to_delete = {"_id": _id}
    orders.delete_one(order_to_delete)


def show_reviews():
    all_reviews = reviews.find()
    print([review for review in all_reviews])

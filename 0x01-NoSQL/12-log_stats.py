#!/usr/bin/env python3
"""
Provide some details about Nginx logs from MongoDB
"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """
    Prototype: def log_stats(mongo_collection, option=None):
    Provide some stats about Nginx logs stored in MongoDB
    """
    lists = {}
    if option:
        va = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {va}")
        return

    res = mongo_collection.count_documents(lists)
    print(f"{res} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(nginx_collection, method)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)

from .settings import S
from typing import Dict
from pymongo import MongoClient

client = MongoClient(S.mongo_dsn)

db=client[S.mongo_db_name]
coll=db[S.mongo_coll_name]



def insert_doc(doc:Dict, duplicates:bool=False):
    """Insert a new document in the collection

    Parameters
    ----------
    doc : Dict
        doc to be inserted
    duplicates : bool, optional
        If False, before inserting the doc it checks if 
        the last inserted is already updated, by default False.
        Sometimes we can read many times the same value, it is not
        necessary to insert it many times.
    """
    return coll.insert_one(doc).inserted_id
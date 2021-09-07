from .settings import S, log
from typing import Dict, Optional
from pymongo import MongoClient, DESCENDING
from time import time

client = MongoClient(S.mongo_dsn)

db = client[S.mongo_db_name]
coll = db[S.mongo_coll_name]


def insert_doc(doc: Dict, duplicates: bool = False, dup_seeker: Optional[Dict] = None):
    """Insert a new document in the collection, 

    Parameters
    ----------
    doc : Dict
        doc to be inserted
    dup_seeker: Dict, optional
        Before inserting the doc we can checks if
            the last inserted (from same provider and same symbol)
            is already updated.
            Sometimes we can read many times the same value, it is not
            necessary to insert it many times.

        Dictionary with following keys:
           pk: list of fields to use as primary key
           value: name of the field to compare with inserting doc

    """

    if dup_seeker:  # None or empty dict
        qry = {k: doc[k] for k in dup_seeker["pk"]}

        if coll.find_one(qry, sort=[("ts", DESCENDING)]) is not None:
            log.debug(
                "Conflict on %s symbol %s, same value as previous one. Data ignored",
                doc.get("provider"),
                doc.get("symbol"),
            )
            #Exiting without any more actions
            return None

    doc["ts"] = time()
    return coll.insert_one(doc).inserted_id

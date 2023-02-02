from app.core.db import get_db
from bson.json_util import dumps
import json
db= get_db()



def select_one(table,query=None,is_json=False):
    if query is None:
        return False
    else:
        if is_json:
            return json.loads(dumps(db[table].find_one(query)))
        return db[table].find_one(query)


def select_all(table,is_json=False):
    if is_json:
        items=list(db[table].find({}))
        return {table:json.loads(dumps(items))}
    return db[table].find({})
import datetime

from trpg.const import *

db = dict()
db['meta'] = {
    'start_time': datetime.datetime.now()
}


def reset():
    global db
    db = dict()
    db['meta'] = {
        'start_time': datetime.datetime.now()
    }


def set(k, v):
    global db
    db[k] = v


def get(k):
    global db
    if k in db:
        return db[k]
    else:
        if k in ['pc', 'bind', 'mod']:
            db[k] = {}
            return db[k]
        elif k in ['kp']:
            db[k] = None
            return db[k]
        else:
            return None

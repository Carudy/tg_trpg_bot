import shelve

DB_FILE = './data'


def reset():
    with shelve.open(DB_FILE, flag='c') as db:
        for k in db:
            del db[k]
        db['pc'] = {}
        db['bind'] = {}
        db['mod'] = {}
        db['kp'] = None


def set(k, v):
    with shelve.open(DB_FILE, flag='c') as db:
        db[k] = v


def get(k):
    with shelve.open(DB_FILE, flag='c') as db:
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

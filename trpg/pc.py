from trpg.const import *


class PC:
    def __init__(self, d):
        self.attr = {}
        for k in d:
            self.attr[k] = d[k]

    def __getitem__(self, item):
        if item in self.attr.keys():
            return self.attr[item]
        if item in attr_set:
            i = attr_trans_id[item]
            for k in attr_trans[i]:
                if k in self.attr.keys():
                    return self.attr[k]
        raise Exception('No such attr!')

    def __setitem__(self, item, val):
        self.attr[item] = val

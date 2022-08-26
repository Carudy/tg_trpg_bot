from trpg.const import *


class PC(dict):
    def __init__(self, d):
        for k in d:
            self[k] = d[k]

    def __getitem__(self, item):
        if item in self.keys():
            return self[item]
        if item in attr_set:
            i = attr_trans_id[item]
            for k in attr_trans[i]:
                if k in self.keys():
                    return self[k]
        raise Exception('No such attr!')

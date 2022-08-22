import random
import db
import requests
import json
import re

trans_list = {
    'str': '力量',
    'con': '体质',
    'siz': '体型',
    'dex': '敏捷',
    'app': '外貌',
    'int': '智力',
    'pow': '意志',
    'edu': '教育',
    'luck': '幸运',
    # 'san': '理智',
    'shan': '闪避',
    'fight': '斗殴',
    'hide': '潜行',
    'cure': '急救',
    'coc': '神秘学',
    'hunman': '人类学',
    'see': '侦查',
    'hear': '聆听',
    'say': '话术',
    'fear': '恐吓',
    'love': '魅惑',
    'mind': '心理学',
    'lib': '图书馆',
}


class TGBot:
    def __init__(self) -> None:
        self.cmd_list = {
            'rd', 'add_pc', 'rm_pc', 'set', 'ra', 'kp',
            'bind_pc', 'show_pc', 'reset',
        }

    def call(self, update, cmd):
        return getattr(self, f'{cmd[0]}')(update, cmd[1:])

    def rd(self, update, cmd):
        res = f'{update.effective_user.username} diced '
        for r in cmd:
            r = int(r)
            if r <= 1:
                raise Exception('Wrong boarder.')
            n = random.randint(1, r)
            res += f'{n} / {r} '
        return res

    def kp(self, update, cmd):
        if len(cmd) and cmd[0] == 'rm':
            db.set('kp', None)
            return "KP removed."
        now = db.get('kp')
        if now is None:
            db.set('kp', update.effective_user.id)
            return f"{update.effective_user.username} has been the KP."
        else:
            return f"Already has KP."

    def reset(self, update, cmd):
        db.reset()
        return "ALL DATA RESETED."

    def show_pc(self, update, cmd):
        pc = db.get('pc')
        res = ''
        if not len(cmd):
            for k in pc:
                res += f'{k}: {pc[k]["sex"]}\n'
        else:
            now = pc[cmd[0]]
            res = cmd[0] + '\n'
            for k, v in now.items():
                res += f'{k}: {v}\t'
        if not res:
            return "Fail to find PC."
        return res

    def rm_pc(self, update, cmd):
        pc = db.get('pc')
        if cmd[0] in pc:
            del pc[cmd[0]]
            db.set('pc', pc)
            return "PC removed."
        else:
            return "Fail to find PC."

    def add_pc(self, update, cmd):
        if cmd[0] == 'maoye':
            url = 'https://maoyetrpg.com/api/rolecard/share?&name=rolecard'
            r = requests.post(url, data=json.dumps({'chartid': cmd[1]}))
            r = json.loads(r.content)['data'][0]
            res = {
                'hp': r['hp']['total'],
                'mp': r['mp']['total'],
                'name': r['name']['chartname'],
                'age': r['name']['ages'],
                'sex': r['name']['sex'],
                'san': r['san']['have'],
            }
            print(r)
            p = r['touniang'].strip('.st').strip()
            a = re.findall(r'[0-9]+', p)
            b = re.split(r'[0-9]+', p)
            b = [i if '/' not in i else i.split('/')[0] for i in b]
            for k, v in zip(b, a):
                res[k] = v
            pc = db.get('pc')
            pc[res['name']] = res
            db.set('pc', pc)
            return f"PC {res['name']} is uploaded from maoye."
        else:
            return "Unkown"

    def bind_pc(self, update, cmd):
        binds = db.get('bind')
        pcs = db.get('pc')
        pc_name = cmd[0]
        if pc_name not in pcs:
            return "Fail to find PC."
        uid = update.effective_user.id
        if pc_name not in binds:
            binds[pc_name] = uid
            db.set('bind', binds)
            return "Bind successfully."
        else:
            if binds[pc_name] == uid:
                return "Already bind to you!"
            else:
                return "Already bind to other pl!"

    def ra(self, update, cmd):
        binds = db.get('bind')
        pcs = db.get('pc')
        pc_name = pc = None
        for _name, uid in binds.items():
            if uid == update.effective_user.id:
                pc_name = _name
                pc = pcs[_name]
                break
        if pc is None:
            return "Fail to find your PC."
        n = random.randint(1, 100)
        attr = trans_list[cmd[0]] if cmd[0] in trans_list else cmd[0]
        b = int(pc[attr])
        if n < 3:
            r = '竟然是大成功耶！'
        elif n <= b / 5:
            r = '极难成功！'
        elif n <= b / 2:
            r = '困难成功！'
        elif n <= b:
            r = '成功！'
        elif n >= 96:
            r = '哇哦，大失败！'
        else:
            r = '失败咧！'
        return f'{pc_name} {attr} diced {n} / {b}, {r}'

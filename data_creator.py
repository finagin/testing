# -*- coding: utf-8 -*-

import random
import json


class DataCreator:
    def __init__(self, file_name, valid_login, valid_password, kol=3, length=15):
        self.chars = '1234567890qazwsxedcrfvtgbyhnujmikolp'
        self.data = {
            'auth': [],
            'issues': {'title': '', 'description': ''}
        }

        for i in range(kol):
            self.data["auth"].append({'login': '', 'password': ''})
            for j in range(length):
                self.data['auth'][i]['login'] += random.choice(self.chars)
                self.data['auth'][i]['password'] += random.choice(self.chars)
        self.data["auth"].append({'login': '', 'password': ''})
        self.data['auth'][len(self.data['auth']) - 1]['login'] += valid_login
        self.data['auth'][len(self.data['auth']) - 1]['password'] += valid_password

        for i in range(length):
            self.data["issues"]["title"] += random.choice(self.chars)
            self.data["issues"]["description"] += random.choice(self.chars)

        f = open(file_name + '.json', 'w')
        f.write(json.dumps(self.data))
        f.close()


class DataRead:
    def __init__(self, file_name):
        f = open(file_name + '.json', 'r')
        self.data = json.loads(f.read())

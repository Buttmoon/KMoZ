import json
from random import randint
import re


class Agents:
    all = []
    def __init__(self) -> None:
        jsonfile =  open("./user_agents/__data__.json", encoding="UTF-8")
        self.all = json.load(jsonfile)
        pass
    def get_random_mobile(self):
        regx_android =  re.compile(r'.+Android.+')
        regx_iphone =  re.compile(r'.+iPhone.+')
        list =  [ _a for _a in self.all if regx_android.match(_a) ]
        list.append([ _a for _a in self.all if regx_iphone.match(_a) ])
        rand_index =  randint(0, len(list))
        return list[rand_index]
    
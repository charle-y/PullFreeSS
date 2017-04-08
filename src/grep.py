#! /usr/bin/python3.5
#version 0.1
import json
from collections import OrderedDict  
from HandleProtocal import ishadowsocks

happy = ishadowsocks()
with open("gui-config.json", "r") as s:
    j = json.load(s, object_pairs_hook=OrderedDict)
    j["configs"] = happy.get()
    with open("gui-config.json", "w") as n_c:
        try:
            json.dump(j, n_c, indent = 2)
            print("写入成功")
        except:
            print("写入失败")



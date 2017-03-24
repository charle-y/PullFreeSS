#! /usr/bin/python3.5
#version 0.1
import json
from HandleProtocal import ishadowsocks

happy = ishadowsocks()
with open("gui-config.json", "r") as s:
    j = json.load(s)
    j["configs"] = happy.get()
    with open("gui-config.json", "w") as n_c:
        try:
            json.dump(j, n_c, 'indent')
            print("写入成功")
        except:
            print("写入失败")



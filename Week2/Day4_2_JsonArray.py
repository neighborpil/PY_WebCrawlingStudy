"""
JSON은 list와 dictionary로 이루어져 있다
"""

import json
input = """
[
    {
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    },
    {
        "id" : "009",
        "x" : "7",
        "name" : "Bill"
    }
]
"""

info = json.loads(input) # string을 읽어서 parsing해준다
print("User Count: ", len(info))
for item in info:
    print("Name: ", item["name"])
    print("ID: ", item["id"])
    print("Attribute: ", item["x"])

import json
data = """{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 123 432 432"
    },
    "email" : {
        "hide" : "yes"
    }
}
"""

info = json.loads(data) # dict 반환
print('Name: ', info["name"])
print('Hide: ', info["email"]["hide"])
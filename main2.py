import json
a = {
        "people" : [
            {
                "name" : "john",
                "age" : 23,
                "height" : 82/12
            },
            {
                "name" : 'eric',
                "age" : 31,
                "height" : 6
            },
            {
                "name" : "will",
                "age" : 25,
                "height" : 5.75
            }
            ]
        }
print(json.dumps(a, indent = 3, sort_keys = False, separators = ("-- ", "== ")))
with open("people.json", "w") as f:
    f.write(json.dumps(a, indent = 3, sort_keys = False, separators = ("-- ", "== ")))
with open("people.json", "w") as f:
    f.write(json.dumps(a, indent = 3))
with open("people.json", "r") as f:
    new = json.loads(f.read())
print(new)

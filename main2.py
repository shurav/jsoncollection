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
f.close()
print(new)
new["networths"] = [
            {
                "name" : "john",
                "nw" : 200*10**3
            },
            {
                "name" : "eric",
                "nw" : 60*10**3
            },
            {
                "name" : "will",
                "nw" : 90*10**3
            }
            ]
with open("people.json", "w") as g:
    g.write(json.dumps(new, indent = 3))
with open("people.json", "r") as g:
    includeNet = json.loads(g.read())
g.close()
print(includeNet)

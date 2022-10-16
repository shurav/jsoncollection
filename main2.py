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
g = open("people.json", "w")
g.write(json.dumps(new, indent = 3))
g = open("people.json", "r")
includeNet = json.loads(g.read())
g.close()
print(includeNet)
h = open("people.json", "w")
new["hometowns"] = [
    {
        "name" : "john",
        "hometown" : "ny"
    },
    {
        "name" : "eric",
        "hometown" : "la"
    },
    {
        "name" : "will",
        "hometown" : "sioux falls"
    }
    ]
h.write(json.dumps(obj = new, indent = 3))
h = open("people.json", "r")
print(json.loads(s = h.read())["hometowns"])
h.close()
i = open("people.json", "w")
for z in new:
    for j in range(len(new["people"])):
        if(new["people"][j]["name"] == "will"):
            new["people"][j]["hasSSN"] = False
            break
        new["people"][j]["hasSSN"] = True
print(new)
i.write(json.dumps(obj = new, indent = 3))
i.close()

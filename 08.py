obj = {
    "name": "Aptech",
    "location": 'Nayapalli',
    "course": ["Python", "MySQL", "Power BI"]
}

print(obj)

print(obj["name"])

print(obj["location"])

print(obj["course"])

print(obj["course"][0])

print(obj["course"][1])

print(obj["course"][2])


print(obj.keys())


if True:
    print("True")
else:
    print("False")
    
for i in range(5):
    print(i)
    
def add(a, b):
    return a + b
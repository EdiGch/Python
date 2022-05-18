import json

json_string = '''
    {
        "students": [
            {
                "id": 1,
                "name": "Tim",
                "age": 21,
                "full-time": true
            },
            {
                "id": 2,
                "name": "Tom",
                "age": 21,
                "full-time": false
            }
        ]
    }
'''
# Zwraca dict
data = json.loads(json_string)
print(type(data))
print(data)
print(data.get('students'))

# Zwraca stringa
data = json.dumps(data, indent=2)
print(type(data))
print(data)

# Odczyt jsona z pliku
with open("data/students.json", "r") as f:
    data = json.load(f)

print(data)

with open("data/students_w.json", "w") as f:
    json.dump(data, f)


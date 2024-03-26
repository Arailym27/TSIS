import json
x =  '{ "name":"ARai", "age":17, "city":"Almaty"}'
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])


import json
#Python(dict):
x = {
  "name": "Arai",
  "age": 17,
  "city": "Almaty"
}
#JSON:
y = json.dumps(x)
print(y)
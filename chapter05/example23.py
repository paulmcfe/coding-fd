person = {
    "name": "Alice",
    "age": 30,
    "is_student": False
}
print(person["age"])
person["age"] = 31
person["email"] = "alice@somewhere.com"
del person["is_student"]
for key in person:
    print(key)
for key, value in person.items():
    print(key, "=", value)

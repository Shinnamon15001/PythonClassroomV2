phonebook = {"Anirach": "777-7777", "Mickey": "777-2222", "Donald": "777-3333", "Pluto": "777-4444"}

heroesdict = {}
heroesdict["Hulk"] = "888-1111"
heroesdict["Ironman"] = "888-2222"
print(heroesdict.get("Hulk", "key not found"))
print(heroesdict.get("Hulk", "key not found"))

for key, value in phonebook.items():
    print(key, value)

print(phonebook.keys())
print(phonebook.values())

print(phonebook.pop("Mick", "Element not found"))
print(phonebook.pop("Mickey", "Element not found"))
print(phonebook)
print(phonebook.popitem())
print(phonebook)
phonebook.clear()
print("After clear")
print(phonebook)
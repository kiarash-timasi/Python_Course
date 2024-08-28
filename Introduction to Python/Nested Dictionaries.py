nested_dict = {
    "person1": {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    },
    "person2": {
        "name": "Bob",
        "age": 25,
        "city": "Los Angeles"
    }
}

print(nested_dict)

# Accessing elements in a nested dictionary
print(nested_dict["person1"]["name"])
print(nested_dict["person2"]["city"])

# Adding a new person
nested_dict["person3"] = {
    "name": "Charlie",
    "age": 35,
    "city": "Chicago"
}

nested_dict["person1"]["age"] = 31
print(nested_dict)

# Removing an element
del nested_dict["person2"]["city"]
print(nested_dict)

# Loop through keys and values
for person, details in nested_dict.items():
    print(f"{person}:")
    for key, value in details.items():
        print(f"  {key}: {value}")
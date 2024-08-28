# Example dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(my_dict)

# Accessing values
print(my_dict["name"])
print(my_dict["age"])
print(my_dict.get("name"))
print(my_dict.get("city"))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# Adding a new key-value pair
my_dict["email"] = "alice@example.com"

# Updating an existing key's value
my_dict["age"] = 26

# removing items of dictionary
del my_dict["city"]

# Loop through keys
for key in my_dict:
    print(key)

# Loop through values
for value in my_dict.values():
    print(value)

# Loop through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Using update() method
my_dict.update({"city": "Los Angeles", "phone": "123-456-7890"})
print(my_dict)


from collections import defaultdict
d = {'a': 1, 'b': 2}
d = defaultdict(lambda: "Key not found")
d.update({'a': 1, 'b': 2})
print(d['c'])  # Output: Key not found
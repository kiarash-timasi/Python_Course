"""
In Python, the json module provides a convenient way to work
with JSON (JavaScript Object Notation) data. JSON is a popular data
format used for data interchange between systems, especially in web applications.
"""
import json
# Python dictionary
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
# Convert to JSON string
json_string = json.dumps(data)
print(json_string)
# Writing JSON to a file
with open('data.json', 'w') as file:
    json.dump(data, file)
# Reading JSON from a File
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
#Parsing JSON Strings
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data)
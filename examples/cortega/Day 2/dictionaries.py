#Accessing Values:
#You can access dictionary values using their keys.

my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing a value by key
name = my_dict["name"]
print(name)  # Output: Alice

# Using get() method (returns None if key is not found)
age = my_dict.get("age")
print(age)  # Output: 25

# If key doesn't exist, get() can return a default value
country = my_dict.get("country", "USA")
print(country)  # Output: USA


#Adding and Updating Items:
#You can add new key-value pairs or update existing ones by simply assigning a value to a key.


# Adding a new key-value pair
my_dict["country"] = "USA"
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA'}

# Updating an existing key
my_dict["age"] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}


#Removing Items:
#You can remove items from a dictionary using methods like pop(), popitem(), or del.


# Remove an item by key
my_dict.pop("city")
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'country': 'USA'}

# Remove the last inserted item
my_dict.popitem()
print(my_dict)  # Output: {'name': 'Alice', 'age': 26}

# Delete a key-value pair
del my_dict["age"]
print(my_dict)  # Output: {'name': 'Alice'}

# Clear all items
my_dict.clear()
print(my_dict)  # Output: {}

#Looping through a Dictionary:
#You can loop over the keys, values, or both using different methods.


# Loop through keys
for key in my_dict:
    print(key)

# Loop through values
for value in my_dict.values():
    print(value)

# Loop through both keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")


    
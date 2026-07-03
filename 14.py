# Implement a function that takes a list of dictionary entries representing users (with fields like name, age, and city) and groups them into a nested dictionary structured by city.

users = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "London"},
    {"name": "Charlie", "age": 35, "city": "New York"},
    {"name": "Diana", "age": 28, "city": "Chicago"},
    {"name": "Evan", "age": 40, "city": "London"}
]


def group_by_city(users):
    grouped_data = {}
    for user in users:
        city = user["city"]
        
        if city not in grouped_data:
            grouped_data[city] = []
            
        grouped_data[city].append(user)
    
    return grouped_data    
        

if __name__ == "__main__":
    result = group_by_city(users)
    for city, people in result.items():
        print(f"{city} ({len(people)} user{'s' if len(people) != 1 else ''}):")
        for person in people:
            print(f"  - {person['name']} (age {person['age']})")
        print()

# Detailed dictionary explanation:
#
# A dictionary in Python is a collection of key-value pairs. Each key is unique,
# and each key maps to one value. You can think of a dictionary like a labeled box
# where each label (the key) points to a stored item (the value).
#
# Example:
#   {'New York': [user1, user2], 'London': [user3, user4]}
#
# Here, the dictionary has:
#   - keys: 'New York', 'London', 'Chicago'
#   - values: lists of user dictionaries for each city
#
# In this code:
#   grouped_data = {}
# starts with an empty dictionary.
#
# For each user record:
#   city = user['city']
# reads the user's city string, such as 'London'. This is a single value
# that describes one user's location.
#
# Then:
#   if city not in grouped_data:
#       grouped_data[city] = []
# creates a new empty list for that city if the city is not already a key.
#
# Finally:
#   grouped_data[city].append(user)
# adds the full user dictionary to the list stored under that city key.
#
# So the difference is:
#   - user['city'] is a city name taken from one record. It is a string.
#   - grouped_data[city] is the list of all users who share that city.
#     It is a value inside the dictionary, not the key itself.
#
# The dictionary structure after grouping looks like this:
# {
#     'New York': [
#         {'name': 'Alice', 'age': 30, 'city': 'New York'},
#         {'name': 'Charlie', 'age': 35, 'city': 'New York'}
#     ],
#     'London': [
#         {'name': 'Bob', 'age': 25, 'city': 'London'},
#         {'name': 'Evan', 'age': 40, 'city': 'London'}
#     ],
#     'Chicago': [
#         {'name': 'Diana', 'age': 28, 'city': 'Chicago'}
#     ]
# }
#
# Keys are used to find values quickly. For example, grouped_data['London']
# gives you the list of users who live in London.



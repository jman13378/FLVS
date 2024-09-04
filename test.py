from random import randrange
items = [
    {"name": "rusty sword"},  # add other options
    {"name": "stone"},
    {"name": "wood"},
    {"name": "leaf"},
    {"name": "iron"},
]
while True:
    itemToFind = items[randrange(len(items))]
    print(itemToFind)
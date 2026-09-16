# Lists => mutable
my_list: list = [1, True, "text", [1, 2, 3]]
people: list[str] = ["Bob", "James", "Tom"]  # type => list; content type => str
print(people[0])  # Bob
print("Original:", people)  # Original: ['Bob', 'James', 'Tom']

people.append("Jeremy")  # ['Bob', 'James', 'Tom', 'Jeremy']
people.remove("Bob")  # ['James', 'Tom', 'Jeremy']
people.pop()  # ['James', 'Tom'] => we popped the last element
people[0] = "Charlotte"
print(people)  # ['Charlotte', 'Tom']
people.insert(1, "Timothy")  # ['Charlotte', 'Timothy', 'Tom']
people.clear()  # []

# Tuples => immutable
items: tuple = 1, True, "Text"  # we don't have to insert any parentheses but we can
# (1, ) => use comma if you have a tuple of one element
print(type(items))  # <class 'tuple'>
new_tuple: tuple = ()  # empty tuple
coordinates: tuple[float, float] = 1.5, 2.5
# should be an annotation for each element in the correct order

# Sets => no duplicates, no guaranteed order, mutable
elements: set = {99, True, "Bob"}
elements.add("James")  # {'James', True, 99, 'Bob'}
elements.remove("Bob")  # {True, 'James', 99}
elements.pop()  # {99, 'James'} => random popped, 'cause no guaranteed order
elements.clear()  # set()
empty: set = set()  # set()

# Frozensets => exactly the same as regular sets, but immutable
things: frozenset = frozenset({99, True, "Bob"})

# Dictionaries # key: value
users: dict = {}  # empty dict
users: dict = {"Bob": 1}  # a Key and a Value pair
# users: dict = {1: "Bob"}  # you can also use it as 1 is a key, Bob is a value
users: dict = {1: "Bob", 2: "Luigi"}
print(users[2])  # Luigi => 2 is a key, Luigi is a value
print(users.get(3))  # None => If the key is not found, None is returned

users[3] = "Mario"  # add/modify element by key
print(users)  # {1: 'Bob', 2: 'Luigi', 3: 'Mario'}
users[1] = "James"  # modify/add element by key
print(users)  # {1: 'James', 2: 'Luigi', 3: 'Mario'}
users.pop(2)  # delete an element by key
print(users)  # {1: 'James', 3: 'Mario'}
del users[3]  # another way to delete an element by key
print(users)  # {1: 'James'}
users.clear()  # completely clear the dictionary
print(users)  # {}

weather: dict = {
    "time": "12:00",
    "weather": {"morning": "rain", "evening": "more rain"},
}
print(weather["time"])  # 12:00
print(weather["weather"])  # {'morning': 'rain', 'evening': 'more rain'}
print(weather["weather"]["morning"])  # rain

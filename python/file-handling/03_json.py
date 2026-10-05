import json

# 'null' instead of 'None' in json
# only "" double quotation marks

file_path: str = "output/data.json"

# --- --- load (load file and convert into python dict)
with open(file_path, "r") as file:
    data: dict = json.load(file)  # converts json file into python dictionary
    print(data)
    # {'name': 'Mario', 'age': 33, 'friends': ['Luigi', 'Toad'], 'other_info': None}

# --- --- loads (load string and convert into python dict)
my_json: str = """{
    "name": "Mario",
    "age": 33,
    "friends": ["Luigi", "Toad"],
    "other_info": null
}"""

data: dict = json.loads(my_json)  # converts json String into python dictionary
print(data)
# {'name': 'Mario', 'age': 33, 'friends': ['Luigi', 'Toad'], 'other_info': None}

# --- --- dump (creates json(if it doesn't exist),
# converts python dict into json and writes it into json file)

data: dict = {"name": "Bob", "age": 43, "job": None}

with open("output/new_json.json", "w") as file:
    json.dump(data, file)

# --- --- dumps (gets json, converts it into string)
    json_format: str = json.dumps(data)
    print(json_format)  # {"name": "Bob", "age": 43, "job": null}
    print(type(json_format))  # <class 'str'>

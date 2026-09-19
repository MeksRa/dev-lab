print(bool([]))  # False  => the same as: {};[];();'';0... and other empty values
print(bool(None))  # False
print(bool(200))  # True

users: dict = {1: "Mario", 2: "Luigi", 3: "James"}
#  users = {}
if users:  # it checks if users empty => 0 => False, or not => 1 => True
    # print(users.items()) # dict_items([(1, 'Mario'), (2, 'Luigi'), (3, 'James')])
    # print(users.values()) # dict_values(['Mario', 'Luigi', 'James'])
    # print(users.keys()) # dict_keys([1, 2, 3])
    for k, v in users.items():
        print(k, v, sep=": ")
else:
    print("No data found...")

# bool
is_connected: bool = True
has_money: bool = False
print(int(True))  # 1
print(int(False))  # 0
print(True + True)  # 2
if is_connected:  # if True:
    print("There is internet!")

# None => Nothing.
no_value: None = None
print(no_value)  # None
print(type(no_value))  # <class 'NoneType'>

users: dict = {1: "Mario", 2: "Luigi"}
# print(users[3])  # KeyError => If the key is not found, raise a KeyError
print(users.get(3))  # None => If the key is not found, None is returned

# Union type
# str | None  # means both of these types are acceptable ( str and None )
possible_user: str | None = users.get(3)
print(possible_user)

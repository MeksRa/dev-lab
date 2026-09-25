user = {"name": "Alex", "role": "admin", "level": 10}
# ============================================================== #
# Read
print(user["name"])  # Alex  # or KeyError if key doesn't exist
print(user.get("age", "Key doesn't exist"))  # Key doesn't exist
# ============================================================== #
# Add / Change
user["age"] = 30  # create or change
print(user.get("age", "Key doesn't exist"))  # 30
user.update({"role": "superadmin", "city": "Kyiv", "name": "Alex"})
print(user)
# {'name': 'Alex', 'role': 'superadmin', 'level': 10, 'age': 30, 'city': 'Kyiv'}
# ============================================================== #
# Remove
del user["role"]  # remove a key  # or KeyError if key doesn't exist
print(user.pop("level", None))  # safely removes a key, returns its value
user.clear()  # completely clears the dictionary
# ============================================================== #
# Get collections (for loops)
user = {"player": "Destroyer", "Role": "Paladin", "Ability": "Bubble", "Buttons": 2}
print(user.keys())  # dict_keys(['player', 'Role', 'Ability', 'Buttons'])
print(user.values())  # dict_values(['Destroyer', 'Paladin', 'Bubble', 2])
print(user.items())
# dict_items([('player', 'Destroyer'), ('Role', 'Paladin'), ('Ability', 'Bubble'), ('Buttons', 2)])
# ============================================================== #
# Check
print("Yes") if "player" in user else "No"  # Yes
# ============================================================== #


# -- -- Shopping Cart Analyzer -- --


def analyze_cart(cart: dict[str, float]) -> dict:
    total = sum(cart.values())
    count = len(cart.keys())
    expensive = max(cart, key=cart.__getitem__)
    # can't use "cart.get" here, cuz we can get "None"; "min/max" don't want it
    cheap = min(cart, key=cart.__getitem__)
    return {
        "Total": total,
        "Items count": count,
        "Most expensive": expensive,
        "Cheapest": cheap,
    }


# -- -- Group transactions -- --


def group_transactions(transactions: list[dict]) -> dict[str, dict]:
    result = {}
    for tx in transactions:
        cat = tx["category"]
        # if key not in tx, we should use tx.get("category", "Other").
        # "if 'category' in tx and 'amount' in tx:" -> this is how we would check it
        amount = tx["amount"]

        if cat not in result:
            result[cat] = {"total": amount, "count": 1}
        else:
            result[cat]["total"] += amount
            result[cat]["count"] += 1
    return result


# -- -- Count Words -- --


def count_words(words: list[str]) -> dict[str, int]:
    result = {}
    for word in words:
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1

    return result


# -- -- Student Average -- --


def get_student_average(data: dict, student_name: str) -> float:
    student_profile: dict = data[student_name]
    # {"grades": [4, 5, 5, 4], "city": "Kyiv"}
    grades_list: list = student_profile["grades"]
    # [4, 5, 5, 4]
    average = sum(grades_list) / len(grades_list)
    return average


# -- -- User activity analysis -- --
def get_active_user_stats(data: dict[str, dict]) -> dict:
    result = {}
    for profile in data.values():
        if profile["is_active"]:
            name: str = profile["name"]
            hours: float = profile["minutes_spent"] / 60
            result[name] = hours
    return result


def main() -> None:
    cart = {
        "Laptop": 1200.0,
        "Mouse": 25.0,
        "Keyboard": 75.0,
        "Monitor": 300.0,
    }

    print(analyze_cart(cart))  # 1
    # -- -- -- -- -- -- -- -- -- --

    transactions = [
        {"category": "Food", "amount": 12.5},
        {"category": "Tech", "amount": 150.0},
        {"category": "Food", "amount": 40.0},
        {"category": "Tech", "amount": 30.0},
        {"category": "Transport", "amount": 5.0},
    ]

    print(group_transactions(transactions))  # 2
    # -- -- -- -- -- -- -- -- -- --

    words = ["apple", "banana", "apple", "orange", "banana", "apple"]

    print(count_words(words))  # 3
    # -- -- -- -- -- -- -- -- -- --

    students_data = {
        "Alex": {"grades": [4, 5, 5, 4], "city": "Kyiv"},
        "Elena": {"grades": [5, 5, 5], "city": "Odesa"},
    }
    print(get_student_average(students_data, "Alex"))  # 4
    print(get_student_average(students_data, "Elena"))  # 4
    # -- -- -- -- -- -- -- -- -- --

    users = {
        "user_1": {"name": "Alex", "is_active": True, "minutes_spent": 120},
        "user_2": {"name": "Elena", "is_active": False, "minutes_spent": 15},
        "user_3": {"name": "Dmytro", "is_active": True, "minutes_spent": 300},
        "user_4": {"name": "Ivan", "is_active": False, "minutes_spent": 0},
    }

    print(get_active_user_stats(users))  # 5
    # -- -- -- -- -- -- -- -- -- --


if __name__ == "__main__":
    main()

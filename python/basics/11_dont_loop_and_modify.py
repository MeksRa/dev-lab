# Don't modify a list while you're looping through this list
# Instead of this use a temporary list and then transfer changes

people: list[str] = ["Anna", "Bob", "Chris", "David", "Fred"]  # Main list
new_people: list[str] = []  # Temporary list


def bad_practice():
    for person in people:
        print(f" - {person}, {people.index(person)}")
        if person == "Bob":
            print(f"Removing: {person}")
            people.remove("Bob")
    print(people)  # ['Anna', 'Chris', 'David', 'Fred']


#  - Anna, 0
#  - Bob, 1
# Removing: Bob
#  - David, 2
#  - Fred, 3
# => As you can see, we lost Chris, that's a bad practice to modify while looping.


def good_practice():
    for person in people:
        print(f" - {person}, {people.index(person)}")
        if person == "Bob":
            print(f"Removing: {person}")
            continue
        new_people.append(person)
    print(new_people)  # ['Anna', 'Chris', 'David', 'Fred']


#  - Anna, 0
#  - Bob, 1
# Removing: Bob
#  - Chris, 2
#  - David, 3
#  - Fred, 4
# => As you can see, we've found Chris, thanks to temporary list.


# bad_practice()
# good_practice()

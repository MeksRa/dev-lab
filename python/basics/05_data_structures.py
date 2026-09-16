my_list: list = [1, True, "text", [1, 2, 3]]
people: list[str] = ["Bob", "James", "Tom"]  # type => list; content type => str
print(people[0])  # Bob
print("Original:", people)  # Original: ['Bob', 'James', 'Tom']
people.append("Jeremy")  # ['Bob', 'James', 'Tom', 'Jeremy']
people.remove("Bob")  # ['James', 'Tom', 'Jeremy']
people.pop()  # ['James', 'Tom'] => we popped the last element
people[0] = "Charlotte"
print(people)  # ['Charlotte', 'Tom']
people.insert(1, 'Timothy')  # ['Charlotte', 'Timothy', 'Tom']
people.clear()
print(people)
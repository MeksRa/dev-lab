name: str = input("Enter a main character name: ").strip().capitalize()
hero_class: str = input("Enter a class/profession (e.g., knight, mage): ").strip().lower()
verb_a: str = input("Enter an action/hobby (e.g., fight, run): ").strip().lower()
verb_b: str = input("Enter a past tense verb (e.g., defeated, escaped): ").strip().lower()
trophy: str = input("Enter an epic prize/noun: ").strip().lower()
enemy: str = input("Enter a funny enemy/boss: ").strip().lower()
year: str = input("Enter a year (e.g., 2007): ")
age: str = input("Enter a two-digit number: ")

story: str = f"""
---------------------------------------------------------------------
The Legend of {name.upper()}!!!
This is the legendary tale of {name}, a surprisingly competent {hero_class}
who secretly loved to {verb_a} when nobody was watching.

One fateful day, {name} fearlessly {verb_b} the terrifying {enemy.upper()}
and won a shiny {trophy} as the ultimate prize.
The crowd went wild, and even the local bards were speechless!

Fast forward to today, it is {year}: {name} is now {int(age) * 2 + int(age)} years old, resting
comfortably and living on a fat pension, retired from all crazy adventures.

However, rumors say that whenever a new {enemy.upper()} appears,
{name} quietly reaches for that legendary {trophy}...
---------------------------------------------------------------------
"""
print(story)

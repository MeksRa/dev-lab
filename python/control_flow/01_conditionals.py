age: int = 30
if age >= 21:
    print("You may enter the club!")
else:
    print("You're not allowed in...")


# Order matters!
if age >= 21:  # 1
    print("You are an adult")
elif age >= 18:  # 2
    print("You are a young adult")
elif age > 12:  # 3
    print("You are a teenager")
else:
    print("Unknown age")


weather: str = "clear"
if weather == "clear":
    print("It is a nice day!")
elif weather == "cloudy":
    print("The weather could be better")
elif weather == "rainy":
    print("What an Awful day!")
else:
    print("Unknown weather")


# Shorthands  !!! Readability should always come first !!!
number: int = 0
if number > 0:  # long version
    result = "Above 0"
else:
    result: str = "0 and below"

result: str = "above 0" if number > 0 else "0 and below"  # short version
print(result)


condition: bool = True
var: str = "True" if condition else "False"  # short version
# u can leave out '== True' in the 'if condition'

if condition:  # long version
    var: str = "True"
else:
    var: str = "false"
print(var)


# Difference between several 'if' and 'if-elif' chains

score: int = 85
# Only the first matching condition executes
if score >= 80:
    print("Grade: B")  # This runs
elif score >= 70:
    print("Grade: C")  # Skipped
elif score >= 60:
    print("Grade: D")  # Skipped

# Every condition is checked independently; multiple blocks can execute
if score >= 80:
    print("10% Discount")  # This runs
if score >= 70:
    print("5% Discount")  # This runs
if score >= 60:
    print("2% Discount")  # This runs

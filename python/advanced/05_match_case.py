# match case (Python 3.10+)

status: int = 200

match status:
    case 200:
        print("Connected!")
    case 403:
        print("Forbidden...")
    case 404:
        print("Not Found...")
    case _:  # as an 'else' statement
        print("Unknown...")

# -------------

while True:
    user_input: str = input("Enter a command: ")
    command: list[str] = user_input.split()
    # >> find image.png
    # print(command)  # ['find', 'image.png']

    match command:
        case "find", *images:
            print(f"Finding: {images}...")
        case "enlarge", image, amount:  # u can consider it as a list
            print(f"You enlarged {image} by {amount}x")
        case "rename", image, new_name if len(new_name) > 3:
            print(f'"{image}" was renamed to "{new_name}"')
        case "download", *images:
            print(f"Downloading: {images}...")
        case "x" | "delete", *images:
            print(f"Deleting: {images}...")
        case _:  # as an 'else' statement
            print("Command now found...")

# Output:
#
# >> find cat.jpg banana.png
# Finding: ['cat.jpg', 'banana.png']...
#
# >> enlarge cat.jpg 20
# You enlarged cat.jpg by 20x
#
# >> rename cat.jpg kitty.jpg
# "cat.jpg" was renamed to "kitty.jpg"
#
# >> rename cat.jpg kit
# Command now found...
#
# and so on...
# -------------

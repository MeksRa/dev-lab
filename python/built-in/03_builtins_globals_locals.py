global_1 = "global_1"
global_2 = "global_2"

# Best practice for outputting global variables
for key, value in globals().copy().items():
    if not key.startswith("__"):  # filter system globals
        print(f"{key}: {value}")


# Best practice for outputting local variables
def show_locals():
    local_1 = "local_1"
    for key, value in locals().copy().items():
        if not key.startswith("__"):
            print(f"{key}: {value}")

    print(locals())


show_locals()

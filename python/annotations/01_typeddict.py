from typing import NotRequired, Required, TypedDict

# --------

Vote = TypedDict(
    "Vote",  # Type name
    {  # dict w keys and their types
        "for": int,
        "against": int,
        "topic": Required[str],  # means you must specify the key "topic"
    },
    total=True,  # "True" here means u should specify all the keys: "for", "against", "topic"
)

vote: Vote = {"for": 100, "against": 200, "topic": "More money for everyone"}

# --------


class UserProfile(TypedDict):
    username: str
    email: str
    age: NotRequired[int]  # Not required to specify


# U can create w/o key "age" thanks to NotRequired[int]
profile: UserProfile = {"username": "dev_guy", "email": "dev@example.com"}

# --------

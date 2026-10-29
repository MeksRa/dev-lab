# 01) Indicate that this is an internal variable.
# Better not to mess with it directly from the outside 'cuz it might change.
# ._variable
# 02) Use name mangling to protect against overwriting
# .__variable
# (instance._ClassName__variable) -> a way to use it

# ================
# 01) non public ._variable
# ================


class SessionManager:
    def __init__(self, username):
        self.username = username  # Public: safe to use anywhere
        self._session_token = (
            "abc123xyz"  # Internal convention: "Please, don't touch from outside"
        )

    def get_token(self):
        # Internal method can easily use the internal variable
        return self._session_token


# --- Testing single underscore behavior ---
user_session = SessionManager("Alice")

# 1. Public attribute works as expected:
print("Username:", user_session.username)  # Output: Alice

# 2. Python DOES NOT block access!
# Unlike __, there is no Name Mangling. The name stays exactly '_session_token'.
print(
    "Internal token (accessed directly):", user_session._session_token
)  # Output: abc123xyz

# 3. You can even modify it from the outside without any errors:
user_session._session_token = "hacked_token_999"
print("Modified token:", user_session.get_token())  # Output: hacked_token_999


# ================
# 02) Name mangling (.__variable)
# ================


class BankAccount:
    def __init__(self, owner, base_balance):
        self.owner = owner
        # Mangled to: _BankAccount__balance
        self.__balance = base_balance

    # Mangled method: _BankAccount__validate
    def __validate(self):
        return "Base bank security check OK"

    def get_base_balance(self):
        # The parent class calls its own mangled method safely
        print(f"[{self.owner}] Parent check: {self.__validate()}")
        return self.__balance


class CreditAccount(BankAccount):
    def __init__(self, owner, base_balance, credit_limit):
        super().__init__(owner, base_balance)
        # Same name '__balance', but safely mangled to: _CreditAccount__balance
        # It does NOT overwrite the parent's __balance!
        self.__balance = credit_limit

    # Mangled method: _CreditAccount__validate
    # It has the same name, but Python renames it, so it doesn't break the parent!
    def __validate(self):
        return "Credit history and risk check OK"

    def get_credit_balance(self):
        # The child class calls its own mangled method
        print(f"[{self.owner}] Child check: {self.__validate()}")
        return self.__balance


# users

alice_account = CreditAccount(owner="Alice", base_balance=500, credit_limit=5000)
bob_account = CreditAccount(owner="Bob", base_balance=100_000_400, credit_limit=40_000)

# --- Testing and printing the actual results ---
print("--- Operations ---")
users = [alice_account, bob_account]
for user in users:
    base_val = user.get_base_balance()
    print(f"-> Base Balance output: {base_val}")
    credit_val = user.get_credit_balance()
    print(f"-> Credit Limit output: {credit_val}")
    print("---" * 10)

# --- Operations ---
# [Alice] Parent check: Base bank security check OK
# -> Base Balance output: 500
# [Alice] Child check: Credit history and risk check OK
# -> Credit Limit output: 5000
# ------------------------------
# [Bob] Parent check: Base bank security check OK
# -> Base Balance output: 100000400
# [Bob] Child check: Credit history and risk check OK
# -> Credit Limit output: 40000
# ------------------------------

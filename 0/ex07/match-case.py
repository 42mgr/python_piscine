from dataclasses import dataclass


# Setup: A simple class to demonstrate Object Matching
@dataclass
class User:
    name: str
    role: str


def system_processor(command):
    match command:
        # 1. LITERALS & OR (|)
        # Matches specific strings. The '|' acts as an 'or'.
        case "start" | "go" | "run":
            print("System started.")

        # 2. SEQUENCE + TYPE GUARD + UNPACKING
        # Matches a list of 2 items where the second is an integer.
        # "action" captures the first item.
        case [action, value] if isinstance(value, int):
            print(f"Action: {action}, Value: {value * 2}")

        # 3. THE "REST" OPERATOR (*) + LIST COMPREHENSION
        # Matches "filter" followed by ANY number of items.
        # '*files' captures all remaining items into a list.
        case ["filter", *files]:
            # Using a List Comp to process the captured data
            clean_files = [f.lower() for f in files if f.endswith(".txt")]
            print(f"Text files found: {clean_files}")

        # 4. MAPPING (DICT) PATTERN + CAPTURE
        # Matches a dictionary that HAS specific keys.
        # It ignores extra keys in the dict (unlike lists, which must be exact).
        case {"type": "error", "code": c, "msg": m}:
            print(f"Error {c}: {m}")

        # 5. CLASS / OBJECT PATTERN
        # Matches a User object specifically with role="admin".
        # 'n' captures the name.
        case User(name=n, role="admin"):
            print(f"Welcome Admin {n}!")

        # 6. WILDCARD (The 'Else')
        # Matches anything not caught above. Always put this last.
        case _:
            print("Unknown command format.")


# --- TEST CASES ---
system_processor("go")  # Case 1
system_processor(["resize", 50])  # Case 2
system_processor(
    ["filter", "A.TXT", "img.png", "test.txt", "bla.txt"]
)  # Case 3
system_processor(
    {"type": "error", "code": 404, "msg": "Not Found", "time": 1200}
)  # Case 4
system_processor(User(name="Alice", role="admin"))  # Case 5
system_processor(["bad", "command"])  # Case 6

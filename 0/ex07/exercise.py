# Basic transformation
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list([x**2 for x in numbers]))

# Multiple If conditions (Implicit AND)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print([x for x in numbers if x % 2 == 0 if x > 4])

# Simple Filter
names = ["John", "Paul", "George", "Ringo", "Eric", "Mick"]
print(list([name for name in names if (len(name) == 4)]))

# Cleaning Mixed Data
data = ["apple", 42, "banana", None, "cherry", 7.5]
print(list([x.upper() for x in data if isinstance(x, str)]))

# Tennary Operator (if-else)
input = range(1, 11)
print(list(["Even" if x % 2 == 0 else "Odd" for x in input]))

# Set Comprehension
unique_chars = {c.upper() for c in "Mississippi"}  # {'M', 'I', 'S', 'P'}

# Nested Comprehension (Flattening data)
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print([i for j in matrix for i in j])
for j in matrix:  # first
    for i in j:  # second
        print(i, end=", ")  # result
print()
# Create a grid
grid = [[0 for _ in range(3)] for _ in range(3)]
print(grid)

# Dictionary Comprehension (Key-Value mapping)
words = ["apple", "banana", "cherry", "apricot", "date"]
print({x: len(x) for x in words if not x.startswith("a")})

# Pairing two lists into Dictionary
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
result = {name: score for name, score in zip(names, scores)}
print(result)

# Inverse Dictionary
MORSE_CODE_DICT = {"a": "...", "b": "---"}
print({v: k for k, v in MORSE_CODE_DICT.items()})

# Generator Expressions (memory efficiency) -> return iteratorggV
text = "ab"
## Aborts when first check is false
boolean = all(char.lower() in MORSE_CODE_DICT for char in text)
print(boolean)
## Create entire string
text = " ".join(MORSE_CODE_DICT[char] for char in text)
print(text)

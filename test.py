# For loop iterating over a list
fruits = ["apple", "banana", "cherry"]

# For loop with dictionary
person = {"name": "John", "age": 30, "city": "NYC"}
for key in person:
    print(f"{key}: {person[key]}")

# For loop with items() for dictionaries
for key, value in person.items():
    print(f"{key}: {value}")

# Nested for loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# For loop with else
for i in range(3):
    print(i)
else:
    print("Loop completed")

# For loop with break
for i in range(10):
    if i == 5:
        break
    print(i)

# For loop with continue
for i in range(5):
    if i == 2:
        continue
    print(i)

# List comprehension (compact for loop)
squares = [x**2 for x in range(5)]
print(squares)

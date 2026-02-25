# zip() - combines multiple iterables element-wise
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list3 = [10, 20, 30]

# Basic zip example
for num, letter in zip(list1, list2):
    print(f"{num} -> {letter}")

# zip with multiple iterables
for num, letter, val in zip(list1, list2, list3):
    print(f"{num}, {letter}, {val}")

# Convert zip to list
combined = list(zip(list1, list2))
print(combined)  # [(1, 'a'), (2, 'b'), (3, 'c')]


# enumerate() - adds index to iterable elements
fruits = ["apple", "banana", "cherry"]

# Basic enumerate example
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# enumerate with custom start index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# Unpack enumerate as list of tuples
indexed_fruits = list(enumerate(fruits))
print(indexed_fruits)  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]


# Combining zip and enumerate
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for idx, (name, age) in enumerate(zip(names, ages)):
    print(f"{idx}: {name} is {age} years old")

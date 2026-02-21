# List methods
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()  # Sorts in place
reversed_list = list(reversed(numbers))
count = numbers.count(1)  # Count occurrences
index = numbers.index(4)  # Find index

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]

# Iteration
for item in fruits:
    print(item)

# List unpacking
a, b, c = [1, 2, 3]

# Copying lists
original = [1, 2, 3]
shallow_copy = original.copy()
deep_copy = original[:]

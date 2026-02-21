# Tuple Examples and Methods in Python

# 1. Creating Tuples
empty_tuple = ()
single_element = (42,)  # Note: comma is required for single element
multiple_elements = (1, 2, 3, 4, 5)
mixed_types = (1, "hello", 3.14, True)
nested_tuple = (1, (2, 3), (4, 5, 6))
from_list = tuple([1, 2, 3])

# 2. Accessing Elements
tup = (10, 20, 30, 40, 50)
print(tup[0])  # 10 (first element)
print(tup[-1])  # 50 (last element)
print(tup[1:3])  # (20, 30) (slicing)

# 3. Tuple Methods (only 2 methods available)
# count() - returns number of occurrences
numbers = (1, 2, 3, 2, 4, 2)
print(numbers.count(2))  # 3

# index() - returns index of first occurrence
print(numbers.index(3))  # 2
print(numbers.index(2))  # 1

# 4. Tuple Operations
tup1 = (1, 2)
tup2 = (3, 4)
print(tup1 + tup2)  # (1, 2, 3, 4) (concatenation)
print(tup1 * 3)  # (1, 2, 1, 2, 1, 2) (repetition)
print(2 in tup1)  # True (membership)
print(len(tup1))  # 2 (length)

# 5. Tuple Unpacking
a, b, c = (1, 2, 3)
print(a, b, c)  # 1 2 3

# With different number of variables using *
x, *y, z = (1, 2, 3, 4, 5)
print(x, y, z)  # 1 [2, 3, 4] 5

# 6. Iterating through Tuples
for item in (1, 2, 3):
    print(item)

# With enumerate
for index, value in enumerate(("a", "b", "c")):
    print(index, value)

# 7. Tuple Comprehension (returns a generator, not tuple)
gen = (x * 2 for x in range(5))
print(tuple(gen))  # (0, 2, 4, 6, 8)

# 8. Comparing Tuples
print((1, 2) == (1, 2))  # True
print((1, 2) < (1, 3))  # True (lexicographic)

# 9. Converting to Tuple
print(tuple("abc"))  # ('a', 'b', 'c')
print(tuple(range(3)))  # (0, 1, 2)

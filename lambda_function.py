from functools import reduce

# 1. Simple lambda - square a number
square = lambda x: x**2
print(square(5))  # Output: 25

# 2. Lambda with multiple parameters
add = lambda x, y: x + y
print(add(3, 7))  # Output: 10

# 3. Lambda with map() - convert temperatures
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, celsius))
print(fahrenheit)  # Output: [32.0, 50.0, 68.0, 86.0]

# 4. Lambda with filter() - get even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]

# 5. Lambda with sorted() - sort by second element
pairs = [(1, "one"), (3, "three"), (2, "two")]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]

# 6. Lambda with reduce() - sum all numbers
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

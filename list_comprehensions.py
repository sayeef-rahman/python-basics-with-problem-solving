# traditional way to create a list
numbers = [1, 2, 3, 4]
squares = []

for n in numbers:
    squares.append(n * n)

print(squares)

# using list comprehensions
squares_comp = [n * n for n in numbers]
print(squares_comp)

# filtering with list comprehensions
even_squares = [n * n for n in numbers if n % 2 == 0]
print(even_squares)

# Modify While Filtering
modified_squares = [n * n + 1 for n in numbers if n % 2 != 0]
print(modified_squares)


# If-Else Inside Comprehension
even_odd_squares = [n * n if n % 2 == 0 else n * n + 1 for n in numbers]
print(even_odd_squares)

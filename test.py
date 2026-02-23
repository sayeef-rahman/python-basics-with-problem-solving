# For loop with continue
for i in range(5):
    if i == 2:
        continue
    print(i)

# List comprehension (compact for loop)
squares = [x**2 for x in range(5)]
print(squares)

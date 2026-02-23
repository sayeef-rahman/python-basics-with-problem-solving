# For loop iterating over a list
fruits = ["apple", "banana", "cherry"]

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

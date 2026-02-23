# Basic examples with range
print("Basic for loop with range:")
for i in range(5):
    print(i)

# range with start, stop, step
print("Range with start, stop, step:")
for i in range(1, 10, 2):
    print(i)

# iteration over a list
print("For loop iterating over a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# using strings in for loop
print("For loop iterating over a string:")
for char in "hello":
    print(char)

# using dictionaries in for loop
print("For loop with dictionary:")
person = {"name": "John", "age": 30, "city": "NYC"}
for key in person:
    print(f"{key}: {person[key]}")

# For loop with items() for dictionaries
print("For loop with items():")
for key, value in person.items():
    print(f"{key}: {value}")

# nested for loops
print("Nested for loops:")
categories = ["Fruit", "Vegetable"]
foods = ["Apple", "Carrot", "Banana"]
for category in categories:
    for food in foods:
        print(f"{category}: {food}")

# For loop with enumerate (index and value)
print("For loop with enumerate:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")


# For loop with else
print("For loop with else:")
for i in range(5):
    print(i)
else:
    print("Loop completed without break")


# For loop with break
print("For loop with break:")
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This will not be printed because of break")


# List comprehension (compact for loop)
print("List comprehension:")
squares = [x**2 for x in range(10)]
print(squares)

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

# nested for loops
print("Nested for loops:")
categories = ["Fruit", "Vegetable"]
foods = ["Apple", "Carrot", "Banana"]
for category in categories:
    for food in foods:
        print(f"{category}: {food}")

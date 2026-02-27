# Dictionary Examples in Python

# 1. Creating a dictionary
person = {"name": "John", "age": 30, "city": "New York"}
print(person)

# 2. Empty dictionary
empty_dict = {}
print(empty_dict)

# 3. Accessing values
print(person["name"])
print(person.get("age"))

# 4. Adding new key-value pairs
person["email"] = "john@example.com"
print(person)

# 5. Updating values
person["age"] = 31
print(person)

# 6. Removing items
del person["city"]
print(person)

person.pop("email")
print(person)

# 7. Dictionary methods
print(person.keys())
print(person.values())
print(person.items())

# 8. Checking if key exists
if "name" in person:
    print("Name exists")

# 9. Iterating through dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# 10. Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# 11. Nested dictionary
students = {
    "student1": {"name": "Alice", "grade": "A"},
    "student2": {"name": "Bob", "grade": "B"},
}
print(students["student1"]["name"])

# 12. Copying dictionary
student_copy = students.copy()
print(student_copy)

# 13. Clear dictionary
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print(temp_dict)

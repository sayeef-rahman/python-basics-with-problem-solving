# tuples are like lists but they are immutable (cannot be changed after creation)
# they are defined using parentheses instead of square brackets


empty_tuple = ()
programming_languages = ("Python", "Java", "C++")
number_tuple = (1, 2, 3, 4, 5)
mixed_tuple = (1, "hello", 3.14, True)
print(empty_tuple)  # Output: ()
print(programming_languages)  # Output: ('Python', 'Java', 'C++')
print(number_tuple)  # Output: (1, 2, 3, 4, 5)
print(mixed_tuple)  # Output: (1, 'hello', 3.14, True)
print(
    f"Length of programming_languages tuple: {len(programming_languages)}"
)  # Output: 3

developer = "Jessica"
tuple(developer)  # ('J', 'e', 's', 's', 'i', 'c', 'a')

# finding item in tuple
print("Python" in programming_languages)  # Output: True
print("Ruby" in programming_languages)  # Output: False


# unpacking tuples
a, b, c = programming_languages
print(a)  # Output: Python
print(b)  # Output: Java
print(c)  # Output: C++


# nested tuples
nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple)  # Output: (1, (2, 3), (4, 5, 6))
print(nested_tuple[0])  # Output: 1

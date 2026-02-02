# All type of python variables with examples

# 1. Integer variable
a = 10  # Integer variable
print("Integer a:", a, type(a))  # type() function is used to get the data type

# 2. Float variable
b = 3.14  # Float variable
print("Float b:", b, type(b))

# 3. String variable
myName = "Sayeef Rahman"  # String variable
print("String :", myName, type(myName))

# 4. Boolean variable
isValid = True  # Boolean variable
isInvalid = False
print("Boolean isValid & isInvalid:", isValid, isInvalid, type(isValid))

# 5. NoneType Variable
nothing = None  # NoneType variable
print("NoneType nothing:", nothing, type(nothing))

# 6. complex assignment
complexNum = 2 + 3j  # Complex variable
print("Complex:", complexNum, type(complexNum))

# 7. Multiple assignments
x, y, z = 1, 2.5, "Hello"  # Multiple assignments
print("Multiple assignments x,y,z:", x, y, z)


# 8. same object/value
p = q = r = 10
print("Same object/value p,q,r:", p, q, r)
print("IDs of p,q,r:", id(p), id(q), id(r))  # IDs will be same

# 9. Tuple unpacking. Tuples are immutable ordered collections, like (4, 5).
coordinate = (4, 5)
x2, y2 = coordinate  # tuple unpacking
print("Tuple unpacking x2,y2:", x2, y2)

# 10. Set: An unordered collection of unique elements which are mutable, like {4, 2, 0}.
setExample = {4, 2, 0}
setExample.add(3)
print("Set example:", setExample, type(setExample))

# 11. Dictionary: A collection of key-value pairs which is mutable, like {"name": "Alice", "age": 30}.
dictExample = {"name": "Alice", "age": 30}
dictExample["city"] = "New York"
print("Dictionary example:", dictExample, type(dictExample))

# 12. List: An ordered collection of elements which is mutable, like [1, 2, 3].
listExample = [1, 2, 3]
listExample.append(4)
print("List example:", listExample, type(listExample))

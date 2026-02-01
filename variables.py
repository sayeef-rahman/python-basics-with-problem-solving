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

# complex assignment
complexNum = 2 + 3j  # Complex variable
print("Complex:", complexNum, type(complexNum))

# Multiple assignments
x, y, z = 1, 2.5, "Hello"  # Multiple assignments
print("Multiple assignments x,y,z:", x, y, z)


# same object/value
p = q = r = 10
print("Same object/value p,q,r:", p, q, r)
print("IDs of p,q,r:", id(p), id(q), id(r))  # IDs will be same

import math

numberOne = 10
numberTwo = 5
int_number = 42
float_number = 3.14


# Basic arithmetic operations
print(f"Addition: {numberOne} + {numberTwo} = {numberOne + numberTwo}")
print(f"Subtraction: {numberOne} - {numberTwo} = {numberOne - numberTwo}")
print(f"Multiplication: {numberOne} * {numberTwo} = {numberOne * numberTwo}")
print(f"Division: {numberOne} / {numberTwo} = {numberOne / numberTwo}")
print(f"Floor Division: {numberOne} // {numberTwo} = {numberOne // numberTwo}")
print(f"Modulus (Remainder): {numberOne} % {numberTwo} = {numberOne % numberTwo}")
print(f"Exponentiation: {numberOne} ** {numberTwo} = {numberOne ** numberTwo}")

# integer & float operations

print(f"Int + Float: {int_number} + {float_number} = {int_number + float_number}")
print(f"Type: {type(int_number + float_number)}")

# math module examples
print(f"Square root: sqrt(4)= { math.sqrt(4)}")
print(f"Power: pow(2,3)={math.pow(2,3)}")
print(f"Ceiling: ceil(4.3) = {math.ceil(4.3)}")
print(f"Floor: floor(4.9) = {math.floor(4.9)}")
print(f"Absolute: abs(-10) = {abs(-10)}")
print(f"Pi: {math.pi}")
print(f"e: {math.e}")
print(f"Factorial: factorial(5) = {math.factorial(5)}")

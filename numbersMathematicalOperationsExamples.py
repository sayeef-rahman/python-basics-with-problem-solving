import math

a = 10
b = 3

# ===== NUMBER TYPE CONVERSION =====
print("\n=== NUMBER TYPE CONVERSION ===")

str_num = "42"
float_str = "3.14"

print(f"String to Int: int('42') = {int(str_num)}")
print(f"String to Float: float('3.14') = {float(float_str)}")
print(f"Int to Float: float(10) = {float(10)}")
print(f"Float to Int: int(9.9) = {int(9.9)}")

# ===== BUILT-IN FUNCTIONS =====
print("\n=== BUILT-IN FUNCTIONS ===")

numbers = [5, 2, 8, 1, 9]

print(f"Sum: sum({numbers}) = {sum(numbers)}")
print(f"Min: min({numbers}) = {min(numbers)}")
print(f"Max: max({numbers}) = {max(numbers)}")
print(f"Length: len({numbers}) = {len(numbers)}")
print(f"Average: {sum(numbers) / len(numbers)}")

# ===== ROUNDING =====
print("\n=== ROUNDING ===")

num = 3.14159

print(f"Round to 2 decimals: round({num}, 2) = {round(num, 2)}")
print(f"Round to nearest int: round({num}) = {round(num)}")

# ===== NEGATIVE NUMBERS =====
print("\n=== NEGATIVE NUMBERS ===")

neg = -15

print(f"Absolute value: abs({neg}) = {abs(neg)}")
print(f"Negative of 10: {-10}")

# ===== COMPARISON OPERATIONS =====
print("\n=== COMPARISON OPERATIONS ===")

x, y = 10, 20

print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} > {y}: {x > y}")
print(f"{x} <= {y}: {x <= y}")
print(f"{x} >= {y}: {x >= y}")

import math

a = 10
b = 3


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

# Python Sets - Examples with Methods & Numerical Operations

# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {1, 2, 3}

print("Original Sets:")
print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"set3: {set3}")

# Set Methods
print("\n--- SET METHODS ---")

# add()
set1.add(6)
print(f"add(6): {set1}")

# remove() - raises error if not found
set1.remove(6)
print(f"remove(6): {set1}")

# discard() - no error if not found
set1.discard(10)
print(f"discard(10): {set1}")

# pop() - removes arbitrary element
s = {1, 2, 3}
removed = s.pop()
print(f"pop(): removed {removed}, remaining {s}")

# clear()
s_copy = {10, 20, 30}
s_copy.clear()
print(f"clear(): {s_copy}")

# copy()
set_copy = set1.copy()
print(f"copy(): {set_copy}")

# Numerical Operations
print("\n--- NUMERICAL OPERATIONS ---")

# Union (|)
print(f"set1 | set2: {set1 | set2}")
print(f"set1.union(set2): {set1.union(set2)}")

# Intersection (&)
print(f"set1 & set2: {set1 & set2}")
print(f"set1.intersection(set2): {set1.intersection(set2)}")

# Difference (-)
print(f"set1 - set2: {set1 - set2}")
print(f"set1.difference(set2): {set1.difference(set2)}")

# Symmetric Difference (^)
print(f"set1 ^ set2: {set1 ^ set2}")
print(f"set1.symmetric_difference(set2): {set1.symmetric_difference(set2)}")

# Subset (<=)
print(f"set3 <= set1: {set3 <= set1}")
print(f"set3.issubset(set1): {set3.issubset(set1)}")

# Superset (>=)
print(f"set1 >= set3: {set1 >= set3}")
print(f"set1.issuperset(set3): {set1.issuperset(set3)}")

# Disjoint
print(f"set1.isdisjoint(set2): {set1.isdisjoint(set2)}")

# In-place operations
print("\n--- IN-PLACE OPERATIONS ---")
s_a = {1, 2, 3}
s_b = {3, 4, 5}

s_a.update(s_b)
print(f"update(): {s_a}")

s_a = {1, 2, 3}
s_a.intersection_update(s_b)
print(f"intersection_update(): {s_a}")

s_a = {1, 2, 3}
s_a.difference_update(s_b)
print(f"difference_update(): {s_a}")

s_a = {1, 2, 3}
s_a.symmetric_difference_update(s_b)
print(f"symmetric_difference_update(): {s_a}")

# Other useful methods
print("\n--- OTHER METHODS ---")
print(f"len(set1): {len(set1)}")
print(f"max(set1): {max(set1)}")
print(f"min(set1): {min(set1)}")
print(f"sum(set1): {sum(set1)}")
print(f"2 in set1: {2 in set1}")
print(f"10 not in set1: {10 not in set1}")

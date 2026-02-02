from typing import List, Dict, Optional

# 5. Common built-in collection types
frozen = frozenset([1, 2, 3])  # frozenset (immutable)
bts = b"bytes"  # bytes (immutable)
ba = bytearray(b"bytes")  # bytearray (mutable)
rng = range(5)  # range object

print(
    "Collections types:",
    type(frozen),
    type(bts),
    type(ba),
    type(rng),
)

# 8. Type hints (annotations)

age: int = 30
scores: List[int] = [100, 90]
config: Dict[str, str] = {"env": "prod"}
maybe_name: Optional[str] = None

print("Hints:", age, scores, config, maybe_name)

# 9. Dynamic typing and conversion
val = "123"
print(type(val), val)
val_int = int(val)
val_float = float(val)
print(type(val_int), val_int, type(val_float), val_float)

# 10. Global and local scope
GLOBAL_VAR = "global"


def outer():
    outer_var = "outer"

    def inner():
        nonlocal outer_var
        global GLOBAL_VAR
        outer_var = "changed by inner"
        GLOBAL_VAR = "changed globally"

    inner()
    return outer_var


print("Scope before:", GLOBAL_VAR)
print("outer returned:", outer())
print("Scope after:", GLOBAL_VAR)


# 11. Assigning functions and classes to variables
def greet(name: str) -> str:
    return f"Hello, {name}!"


fn = greet
print("Function via var:", fn("Bob"))


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.name!r})"


Cls = Person
p = Cls("Eve")
print("Class via var:", p)

# 12. Deleting variables
temp = 999
print("temp exists:", temp)
del temp
try:
    print(temp)
except NameError:
    print("temp deleted")

# 13. Numeric literals examples
big = 1_000_000
hex_num = 0xFF
bin_num = 0b1010
exp = 1.2e3

print("Literals:", big, hex_num, bin_num, exp)

# 14. Immutability demonstration with tuple of lists vs list of tuples
tt = ([1, 2], [3, 4])
tt[0].append(99)  # inner lists mutable
print("tuple with mutable elements:", tt)

ll = [(1, 2), (3, 4)]
# ll[0].append(5)  # would error: tuple has no append
print("list with immutable elements:", ll)

# 15. Final summary print of types
examples = {
    "bytes": bts,
}
for k, v in examples.items():
    print(f"{k:7}: {v!r} (type={type(v).__name__})")

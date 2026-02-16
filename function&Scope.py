"""
function&Scope.py

Concise examples of Python functions and scope (LEGB), covering:
- *args, **kwargs
- lambda
- nested functions and closures
- nonlocal and global
- recursive function
- higher-order functions
- generator (brief)
"""

# Lambda example
square = lambda x: x * x


# Recursive function example
def factorial(n: int) -> int:
    """Compute factorial recursively."""
    if n < 0:
        raise ValueError("Negative factorial is undefined")
    return 1 if n in (0, 1) else n * factorial(n - 1)


# Higher-order functions: functions as arguments and return values
def apply_twice(func, x):
    return func(func(x))


def make_adder(n):
    def adder(x):
        return x + n

    return adder


# Generator example (keeping scope example minimal)
def count_up_to(n):
    """Generator that yields 0..n-1. Shows function scope for local variables."""
    i = 0
    while i < n:
        yield i
        i += 1


if __name__ == "__main__":

    # LEGB demo
    print("LEGB:", lego_demo())

    # Recursion
    print("factorial(5):", factorial(5))

    # Higher-order
    print("apply_twice (square) on 2:", apply_twice(square, 2))
    add10 = make_adder(10)
    print("add10(5):", add10(5))

    # Generator
    print("count_up_to 3:", list(count_up_to(3)))

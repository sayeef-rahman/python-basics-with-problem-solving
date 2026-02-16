"""
function&Scope.py

Concise examples of Python functions and scope (LEGB), covering:
- basic functions, annotations, docstring
- positional, keyword, default args
- mutable default pitfall and fix
- *args, **kwargs
- lambda
- nested functions and closures
- nonlocal and global
- recursive function
- higher-order functions
- generator (brief)
"""


# Mutable default argument pitfall
def append_bad(item, target=[]):
    """Demonstrates the mutable default pitfall."""
    target.append(item)
    return target


# Correct approach for mutable defaults
def append_good(item, target=None):
    """Use None as default and create new list when needed."""
    if target is None:
        target = []
    target.append(item)
    return target


# *args and **kwargs usage
def summarize(*args, **kwargs):
    """Show positional and keyword arguments."""
    return {"args": args, "kwargs": kwargs}


# Lambda example
square = lambda x: x * x


# Nested function / closure example
def power_factory(exp):
    """Return a function that raises x to the given exp (closure captures exp)."""

    def power(x):
        return x**exp

    return power


# nonlocal example
def counter_factory():
    """Create a counter that keeps state via nonlocal variable."""
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


# global example
GLOBAL_TALLY = 0


def use_global(delta=1):
    """Modify a global variable (not recommended in general)."""
    global GLOBAL_TALLY
    GLOBAL_TALLY += delta
    return GLOBAL_TALLY


# LEGB demonstration
X = "global X"


def lego_demo():
    X = "enclosing X"

    def inner():
        X = "local X"
        return X  # returns local

    return inner(), X, globals()["X"]


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

    # Mutable default pitfall
    print("append_bad:", append_bad(1))
    print("append_bad again:", append_bad(2))  # shows shared list
    print("append_good:", append_good(1))
    print("append_good again:", append_good(2))

    # *args and **kwargs
    print("summarize:", summarize(1, 2, a=3, b=4))

    # Lambda and square
    print("square(5):", square(5))

    # Closure
    cube = power_factory(3)
    print("cube(3):", cube(3))

    # nonlocal counter
    c = counter_factory()
    print("counter:", c(), c(), c())

    # global usage
    print("use_global:", use_global(), use_global(5))

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

# basic functions
def greeting(name):
    return f"Hello, {name}"


# name_input = input("Enter you name: ")
# print(greeting(name_input))


# Positional, keyword, and default arguments
# All required parameters must be placed before any default arguments. *modifiers allows for any number of additional positional arguments.
def make_sentence(subject, verb="is", *modifiers, punctuation="."):
    """Build a simple sentence."""
    mid = " ".join(modifiers) if modifiers else ""
    return f"{subject} {verb} {mid}".strip() + punctuation


print(make_sentence("Python", "is", "fun", "powerful", punctuation="!"))


# Mutable default argument in wrong way but works
def append_wrong(item, list=[]):
    list.append(item)
    return list


print(append_wrong(1))  # [1]
print(append_wrong(2))  # [1, 2] - unexpected


# mutable default argument in correct way
def append_right(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list


print(append_right(1))
print(append_right(2))


# *args and **kwargs usage. Summarize positional and keyword arguments.
def summarize(*args, **kwargs):
    details = ", ".join(f"{k}={v}" for k, v in kwargs.items())
    return f"Args: {args} \nDetails: {details}"


print(summarize(1, 2, a=3, b=4))


# Lambda example
square = lambda x: x * x
print("square(5):", square(5))


# Nested function / closure example
# Return a function that raises x to the given exp (closure captures exp)
def power_factory(exp):
    def power(x):
        return x**exp

    return power


print("cube(3):", power_factory(3)(3))


# nonlocal example
def local_counter():
    count = 0

    def counter():
        nonlocal count  # Reference the enclosing variable
        count += 1

    counter()
    print(count)


local_counter()


GLOBAL_COUNTER = 0


def global_counter():
    global GLOBAL_COUNTER
    GLOBAL_COUNTER += 2
    return GLOBAL_COUNTER


print("Global counter:", global_counter())

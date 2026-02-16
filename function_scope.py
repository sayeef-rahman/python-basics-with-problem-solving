# basic functions
def greeting(name):
    return f"Hello, {name}"


name_input = input("Enter you name: ")
print(greeting(name_input))


# Positional, keyword, and default arguments
# All required parameters must be placed before any default arguments. *modifiers allows for any number of additional positional arguments.
def make_sentence(subject, verb="is", *modifiers, punctuation="."):
    """Build a simple sentence."""
    mid = " ".join(modifiers) if modifiers else ""
    return f"{subject} {verb} {mid}".strip() + punctuation


print(make_sentence("Python", "is", "fun", "powerful", punctuation="!"))

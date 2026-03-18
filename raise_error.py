# simple example


def check_adult(age):
    if age < 18:
        raise ValueError("Age must be 18 or older.")
    return "You are an adult."


print(check_adult(10))

# raise with try


def check_age(age):
    if age < 0:
        raise ValueError("Age can not be negative!")
    return age


try:
    check_age(-1)
except ValueError as e:
    print(f"Error: {e}")

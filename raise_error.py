# simple example


def check_adult(age):
    if age < 18:
        raise ValueError("Age must be 18 or older.")
    return "You are an adult."


check_adult(10)

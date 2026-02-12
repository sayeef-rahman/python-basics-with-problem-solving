isLogged = True
isAdmin = False
age = 25
isCitizen = False

print(f"3 > 4: {3 > 4}")  # False
print(f"3 < 4: {3 < 4}")  # True
print(f"3 == 4: {3 == 4}")  # False
print(f"4 == 4: {4 == 4}")  # True
print(f"3 != 4: {3 != 4}")  # True
print(f"3 >= 4: {3 >= 4}")  # False
print(f"3 <= 4: {3 <= 4}")  # True

if isAdmin and isLogged:
    print("Welcome Admin")
elif isLogged:
    print("Welcome User")
else:
    print("Please log in")

if age >= 18 and isCitizen:
    print("You are eligible to vote.")
elif age >= 18 and not isCitizen:
    print("You are not a citizen, so you cannot vote.")
elif age < 18 and isCitizen:
    print("You are not old enough to vote.")
elif age < 18 and not isCitizen:
    print("You are not old enough and not a citizen, so you cannot vote.")
else:
    print("You are not eligible to vote.")


# Here are a few falsy values:
# None
# False
# Integer 0
# Float 0.0
# Empty strings ""

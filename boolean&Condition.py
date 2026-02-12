isLogged = True
isAdmin = False
age = 25
isCitizen = True

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
else:
    print("You are not eligible to vote.")

# All type of python string operation including some mostly used methods with examples

message = " Hello World!  \n"  # basic string with whitespace and newline
raw_string = r"C:\new\tests"  # raw string (backslashes not escaped)

# multiline with tab. Use the opposite kind of quotes. That is, if your string contains single quotes, use double quotes to wrap the string, and vice versa.
multi_line = """Line1
Line2\tTabbed"""

print(message)  # prints including newline
print(raw_string)  # prints raw path
print(multi_line)

print("Length of string:", len(message))  # length (counts all chars)
print(message.strip())  # strip whitespace from both ends
print(message.rstrip())  # strip right
print(message.lstrip())  # strip left


# string indexing and slicing.
# Negative indexing is also allowed, so you can get the last character of any string with -1, the second-to-last character with -2, and so on
print("Indexing and Slicing:")
print("message[1]:", message[1])  # index (second character). Starts from [0]
print("message[-1]:", message[-1])  # last character
print("message[1:5]:", message[1:5])  # slice from index 1 to 4
print("message[:5]:", message[:5])  # start to 4
print("message[7:]:", message[7:])  # 7 to end

# string searching and membership
print("'World' in message:", "World" in message)  # membership check
print("message.find('World'):", message.find("World"))  # index of substring or -1
print("message.rfind('l'):", message.rfind("l"))  # last occurrence
print("message.count('l'):", message.count("l"))  # count occurrences
print("message.startswith(' '):", message.startswith(" "))  # startswith
print("message.endswith('\\n'):", message.endswith("\n"))  # endswith (newline)

# case conversions
print("message.upper():", message.upper())  # upper case
print("message.lower():", message.lower())  # lower case
print("message.capitalize():", message.capitalize())  # first char upper, rest lower
print("message.title():", message.title())  # title case
print("message.swapcase():", message.swapcase())  # swap case
print("'ß'.casefold():", "ß".casefold())  # aggressive lowercasing for comparisons

# string methods for checking content
print("message.isalpha():", message.isalpha())  # only letters
print("message.isdigit():", message.isdigit())  # only digits
print("message.isalnum():", message.isalnum())  # alphanumeric
print("message.isspace():", message.isspace())  # only whitespace
print("message.islower():", message.islower())  # all lowercase
print("message.isupper():", message.isupper())  # all uppercase
print(
    "message.isnumeric():", message.isnumeric()
)  # numeric (includes digits and some other numeric chars)
print("message.replace():", message.replace("World", "Python"))  # replace substring
print("message.split():", message.split())  # split on whitespace
print("message.splitlines():", message.splitlines())  # split on lines
print("message.join():", "-".join(["Hello", "World"]))  # join list into string
print("message.startswith(' '):", message.startswith(" "))  # startswith
print("message.endswith('\\n'):", message.endswith("\n"))  # endswith (newline)

# String Fromatting
name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age))  # str.format
print(f"Name: {name}, Age: {age}")  # f-string (preferred)
print("Number: {:06d}".format(42))  # zero pad
print("{:.2f}".format(3.14159))  # float precision


# splitting and joining
csv = "a,b,c,,d"
print(csv.split(","))  # split into list
print(csv.split(",", 2))  # maxsplit
lines = "one\ntwo\r\nthree".splitlines()  # splitlines handles different newlines
print(lines)
parts = ["a", "b", "c"]
print("-".join(parts))  # join list into string


# partitioning
print("key=value".partition("="))  # (before, sep, after)
print("a-b-c".rpartition("-"))  # right partition


# replace and translation
s2 = "apple banana apple"
print(s2.replace("apple", "pear", 1))  # replace first only
trans = str.maketrans("ab", "AB", "n")  # map a->A, b->B, delete n
print("banana".translate(trans))

# alignment and padding
print(
    "hi".center(4, "*")
)  # center with padding using max length of 4 and * as padding character
print("42".zfill(5))  # zero fill for numbers
print("left".ljust(10, "-"))
print("right".rjust(10, "."))

# tabs and expanding
tabbed = "1\t2\t345"
print(tabbed.expandtabs(4))  # expand tabs to spaces

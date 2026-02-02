# stringAllExamples.py
# Compact examples of common Python string operations with short comments.

s = " Hello, World!  \n"  # basic string with whitespace and newline
raw = r"C:\new\tests"  # raw string (backslashes not escaped)
multi = """Line1
Line2\tTabbed"""  # multiline with tab

print(s)  # prints including newline
print(raw)  # prints raw path
print(multi)

# basic properties
print(len(s))  # length (counts all chars)
print(s.strip())  # strip whitespace from both ends
print(s.rstrip())  # strip right
print(s.lstrip())  # strip left

# immutability
# s[0] = "h"                        # TypeError if uncommented

# indexing and slicing
print(s[1])  # index (second character)
print(s[-2])  # last-second char
print(s[1:5])  # slice from index 1 to 4
print(s[:5])  # start to 4
print(s[7:])  # 7 to end
print(s[::2])  # step slicing
print(s[::-1])  # reversed string

# search and membership
print("World" in s)  # membership check
print(s.find("World"))  # index of substring or -1
print(s.rfind("l"))  # last occurrence
# print(s.index("X"))                # would raise ValueError if not found
print(s.count("l"))  # count occurrences
print(s.startswith(" "))  # startswith
print(s.endswith("\n"))  # endswith (newline)

# case conversions
print(s.upper())  # upper case
print(s.lower())  # lower case
print(s.capitalize())  # first char upper, rest lower
print(s.title())  # title case
print(s.swapcase())  # swap case
print("ß".casefold())  # aggressive lowercasing for comparisons

# tests
print("abc".isalpha())  # only letters
print("123".isdigit())  # only digits
print("123.4".isnumeric())  # numeric (False here)
print("abc123".isalnum())  # alnum
print("   ".isspace())  # whitespace only

# formatting
name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age))  # str.format
print(f"Name: {name}, Age: {age}")  # f-string (preferred)
print("Number: {:06d}".format(42))  # zero pad
print("{:.2f}".format(3.14159))  # float precision
# print(f"{'left':<10}|{ 'center':=10 }|{ 'right':>10}")  # alignment

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
print("hi".center(10, "*"))
print("42".zfill(5))  # zero fill for numbers
print("left".ljust(10, "-"))
print("right".rjust(10, "."))

# tabs and expanding
tabbed = "1\t2\t345"
print(tabbed.expandtabs(4))  # expand tabs to spaces

# encoding and bytes
b = s.encode("utf-8")  # str -> bytes
print(b)
print(b.decode("utf-8"))  # bytes -> str

# ord/chr and codepoint info
print(ord("A"), chr(65))  # codepoint functions
print("é".encode("utf-8"))  # multibyte character

# safe repr/ascii
print(repr(s))  # printable representation with escapes
print(ascii("café"))  # ascii escapes non-ascii

# iteration
for i, ch in enumerate("abc"):
    print(i, ch)

# sorting characters
print("".join(sorted("cab")))  # sort characters

# comparison
print("apple" < "banana")  # lexicographical

# useful utilities
print("".isdecimal())  # False: empty string isn't decimal
print("".join(reversed("hello")))  # reverse via reversed()

# partitioning with tuple check in startswith
print("hello".startswith(("h", "H")))  # any of tuple prefixes

# more advanced: template-like replacement with mapping
template = "Hello {name}, balance: {bal:.2f}"
print(template.format_map({"name": "Bob", "bal": 12.5}))

# small examples showing no-ops or edge cases
empty = ""
print(empty or "default")  # fallback using or
print(("").join([]))  # join empty list -> empty string

# demonstrate translate for sanitizer
sanitizer = str.maketrans({"<": "&lt;", ">": "&gt;"})
print("<tag>".translate(sanitizer))

# done

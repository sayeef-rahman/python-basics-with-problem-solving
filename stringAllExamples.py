# stringAllExamples.py
# Compact examples of common Python string operations with short comments.

s = " Hello, World!  \n"  # left sample string with whitespace and newline


# encoding and bytes
b = s.encode("utf-8")  # str -> bytes
print(b)
print(b.decode("utf-8"))  # bytes -> str

# ord/chr and codePoint info
print(ord("A"), chr(65))  # codePoint functions
print("é".encode("utf-8"))  # multiByte character

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

s = " Hello, World!  \n"  # left sample string with whitespace and newline

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

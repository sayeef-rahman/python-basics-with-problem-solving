# All type of python string operation including some mostly used methods with examples

message = " Hello, World!  \n"  # basic string with whitespace and newline
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

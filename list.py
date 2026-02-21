empty_list = []
print(empty_list)
print(type(empty_list))
print(len(empty_list))

fruits_list = ["banana", "guava", "mango", "papaya"]
print(fruits_list)
print(fruits_list[0])  # Accessing first element
print(fruits_list[-1])  # Accessing last element

# string to list
letters_in_banana = list(fruits_list[0])
print(f"letters_in_banana: {letters_in_banana}")

# List concatenation
more_fruits = ["orange", "kiwi"]
all_fruits = fruits_list + more_fruits
print(f"All fruits: {all_fruits}")

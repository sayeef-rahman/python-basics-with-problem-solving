empty_list = []
print(empty_list)
print(type(empty_list))
print(len(empty_list))

fruits_list = ["banana", "guava", "mango", "papaya"]
print(fruits_list)
print(fruits_list[0])  # Accessing first element
print(fruits_list[-1])  # Accessing last element
print(f"fruits list length: {len(fruits_list)}")

# string to list
letters_in_banana = list(fruits_list[0])
print(f"letters_in_banana: {letters_in_banana}")

# List concatenation
more_fruits = ["orange", "kiwi"]
all_fruits = fruits_list + more_fruits
print(f"All fruits: {all_fruits}")

# update fruit list
fruits_list.append("orange")  # inserting one item at the end of the list
fruits_list.extend(["grape", "kiwi"])  # inserting multiple items at the end of the list
fruits_list.insert(1, "blueberry")  # inserting an item at a specific index
print(f"Updated fruits list: {fruits_list}")
# fruits_list[40] = "JavaScript"  # IndexError: list assignment index out of range

# delete an item from the list
fruits_list.remove("blueberry")  # removing an item by value
print(f"Updated fruits list after removing blueberry: {fruits_list}")

# delete an item by index
del fruits_list[0]  # deleting the first item (banana)
print(f"Updated fruits list after deleting first item: {fruits_list}")

# check if an element is inside the list
print("mango" in fruits_list)  # True
print("orange" in fruits_list)  # True

# clear all items from the list
fruits_list.clear()
print(f"Fruits list after clearing: {fruits_list}")

# nested list
nested_list = [[1, 2], [3, 4], [5, 6]]
print(f"Nested list: {nested_list}")
print(f"Accessing first nested list: {nested_list[0]}")
print(f"Accessing second element of first nested list: {nested_list[0][1]}")

# unpacking a list
developers = ["Alice", "Bob", "Charlie"]
dev1, dev2, dev3 = developers
print(f"Developer 1: {dev1}, Developer 2: {dev2}, Developer 3: {dev3}")

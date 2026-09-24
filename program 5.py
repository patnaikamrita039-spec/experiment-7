
numbers_list = [1, 2, 3, 4, 5]
numbers_tuple = (6, 7, 8, 9, 10)

list_strings = list(map(str, numbers_list))
tuple_strings = list(map(str, numbers_tuple))

print("List of strings:", list_strings)
print("Tuple converted to list of strings:", tuple_strings)
